"""
This module provides functionality to:
1. read in  ICD9/10 gems and descriptions files
2. run basic formatting, 
3. save  the output as csv.
"""

import pandas as pd
import os


def split_flags(flags: int):
    """
    Fill missing GEMS flags with zero
    """
    return ",".join(str(flags).zfill(5))


def format_flags(df):
    """
    Format flags to align with CMS standards
    i.e. 5 GEMS flag types
    """
    
    df.flags = df.flags.apply(split_flags)
    
    flag_types = ["approximate",
                  "no map",
                  "combination",
                  "scenario",
                  "choice list"]
    
    df[flag_types] = \
    pd.DataFrame(df.flags.str.split(",",expand=True).values,
                 columns = flag_types)
    
    df.drop(["flags"], axis = 1, inplace = True)
    
    return df



def format_icd(filename: str):
    
    df = pd.read_csv(filename, 
                     sep="[\s]{1,}",
                     names=["source", "target", "flags"],
                     encoding="latin-1", engine="python")
    
    df = format_flags(df)

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


