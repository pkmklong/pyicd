import pandas as pd
import os

pd.set_option('display.max_colwidth', 255)


def icd9_to_icd10(icd_code: str):

    lookup_table = pd.read_csv("icd9_gems_lookup.csv")

    return lookup_table[lookup_table["source"] == icd_code].loc[:,["icd10", "description"]]


def icd10_to_icd9(icd_code: str):
    
    lookup_table = pd.read_csv("icd10_gems_lookup.csv")
    
    return lookup_table[lookup_table["source"] == icd_code].loc[:,["icd9", "description"]]  
