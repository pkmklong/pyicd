import pandas as pd
import os


def icd9_to_icd10(icd_code: str):

    lookup_table = pd.read_csv("icd9_gems_lookup.csv")


    return lookup_table[lookup_table["source"] == icd_code]

def icd10_to_icd9(icd_code: str):
    
    lookup_table = pd.read_csv("icd10_gems_lookup.csv")

    
    return lookup_table[lookup_table["source"] == icd_code]
    
   
