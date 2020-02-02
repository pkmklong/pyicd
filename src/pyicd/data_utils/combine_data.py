import pandas as pd
import os


def read_tables():

    df_icd9 = pd.read_csv("2018_I9gem.csv")
    df_icd10 = pd.read_csv("2018_I10gem.csv")
    df_icd9_desc = pd.read_csv("CMS32_DESC_LONG_DX.csv")
    df_icd10_desc = pd.read_csv("icd10cm_codes_2018.csv")
    
    return df_icd9, df_icd9_desc, df_icd10, df_icd10_desc


def join_icd_desc(df_icd,df_desc, key: str):
    
    df = pd.merge(df_icd, df_desc,
                  left_on = "target",
                  right_on = key) 
    return df


def save_icd_desc_tables(df, df_name: str):
    
    df.to_csv(df_name, index = False)
    


def add_icd_desc(df_icd9, df_icd9_desc, df_icd10, df_icd10_desc):
    
    #df_icd9, df_icd9_desc, df_icd10, df_icd10_desc = read_tables()
    
    df9_lookup = join_icd_desc(df_icd9,
                        df_icd10_desc,
                        key = "icd10")
    
    df10_lookup = join_icd_desc(df_icd10,
                         df_icd9_desc,
                         key = "icd9")
    
    save_icd_desc_tables(df9_lookup, "icd9_gems_lookup.csv")
    save_icd_desc_tables(df10_lookup, "icd10_gems_lookup.csv")
