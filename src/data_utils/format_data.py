"""
This script read in  ICD9/10 gems and 
descriptions files , run basic formatting, 
and saves the output as csv."
"""

import pandas as pd
import os


def format_icd(filename: str):
    
    df = pd.read_csv("2018_I10gem.txt", 
                     sep="[\s]{1,}",
                     names=["source", "target", "flags"],
                     encoding="latin-1")
    
    save_name = update_file_name(filename)
    df.to_csv(save_name)


def update_file_name(filename: str):

    return f"{filename.split('.')[0]}.csv"


def format_desc(filename: str, codetype: str, separater: str = ","):
    
    df = pd.read_csv(filename,names=[codetype], sep = separater, encoding="latin-1")
    
    df[[codetype, f"{codetype}_desc"]] = df[codetype].str.split(" ", 1, expand=True)
    
    save_name = update_file_name(filename)
    df.to_csv(save_name)


if __name__=="__main__":

    os.chdir("../data/raw_data/gems/")

    format_icd("2018_I10gem.txt")
    format_icd("2018_I9gem.txt")

    format_desc("CMS32_DESC_LONG_DX.txt", "icd9", separater = ",")
    format_desc("icd10cm_codes_2018.txt", "icd10", separater = "//s")
