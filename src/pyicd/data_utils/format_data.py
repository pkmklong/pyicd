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
                     encoding="latin-1", engine="python")
    return df


def format_desc(filename: str, codetype: str, separater: str = ","):
    
    df = pd.read_csv(filename,names=[codetype], sep = separater, encoding="latin-1")
    
    df[[codetype, "description"]] = df[codetype].str.split(" ", 1, expand=True)
    
    return df


def update_file_name(filename: str):

    return f"{filename.split('.')[0]}.csv"


def join_icd_desc(df_icd,df_desc, key: str):

    df = pd.merge(df_icd, df_desc,
                  left_on = "source",
                  right_on = key)
    return df


