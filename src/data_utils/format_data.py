"""
This module provides functionality to:
1. read in  ICD9/10 gems and descriptions files
2. run basic formatting, 
3. save  the output as csv.
"""

import pandas as pd
import os


def format_icd(filename: str):
    
    df = pd.read_csv(filename, 
                     sep="[\s]{1,}",
                     names=["source", "target", "flags"],
                     encoding="latin-1")
    
    save_name = update_file_name(filename)
    df.to_csv(save_name)


def format_desc(filename: str, codetype: str, separater: str = ","):
    
    df = pd.read_csv(filename,names=[codetype], sep = separater, encoding="latin-1")
    
    df[[codetype, f"{codetype}_desc"]] = df[codetype].str.split(" ", 1, expand=True)
    
    save_name = update_file_name(filename)
    df.to_csv(save_name)

    
def update_file_name(filename: str):

    return f"{filename.split('.')[0]}.csv"
