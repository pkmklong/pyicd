import pandas as pd
import os
import pkg_resources

pd.set_option('display.max_colwidth', 255)

ICD9_PATH =  "src/pyicd/utils/icd9_gems_lookup.csv" #  str(pkg_resources.resource_filename(__name__, "icd9_gems_lookup.csv"))
ICD10_PATH =  "src/pyicd//utils/icd10_gems_lookup.csv" # str(pkg_resources.resource_filename(__name__, "icd10_gems_lookup.csv"))


def set_map_type(df: "pandas.dataframe", flag: str):
    
        return df[df[flag] != 0]
    
    
def icd9_to_icd10(icd_code: str, flag: str = None, show_flags: bool = False):
    print(os.getcwd())

    df = pd.read_csv(ICD9_PATH)
    
    if flag:
        df = set_map_type(df, flag)
    
    df["description"] = df["description"].str.upper()
    
    df = df[df["source"] == icd_code].loc[:,["source",
                                            "icd10",
                                            "description",
                                            "approximate",
                                            "no map", 
                                            "combination",
                                            "scenario",
                                            "choice list"]]
    if not show_flags:
        
        df = df.drop(["approximate", "no map","combination", "scenario","choice list"], 
                     axis = 1)
        
    return df


def icd10_to_icd9(icd_code: str, flag: str = None, show_flags: bool = False):
    
    df = pd.read_csv(ICD10_PATH)
    
    if flag:
        df = set_map_type(df, flag)
        
    df["description"] = df["description"].str.upper()  
    
    df = df[df["source"] == icd_code].loc[:,["source",
                                            "icd9",
                                            "description",
                                            "approximate",
                                            "no map", 
                                            "combination",
                                            "scenario",
                                            "choice list"]]
    if not show_flags:
        
        df = df.drop(["approximate", "no map","combination", "scenario","choice list"], 
                     axis = 1)
                                                                
    return df

def search_icd10(search_term: str, flag: str = None,):

    df = pd.read_csv(ICD9_PATH)
    
    if flag:
        df = set_map_type(df, flag)
    
    df["description"] = df["description"].str.upper()
    
    df = \
    df[df["description"].str.contains(search_term.upper())]. \
    loc[:,["icd10", "description", "approximate",
           "no map", "combination", "scenario", "choice list"]]. \
    drop_duplicates()

    return df


def search_icd9(search_term: str, flag: str = None):

    df = pd.read_csv(ICD10_PATH)
    
    if flag:
        df = set_map_type(df, flag)
    
    df["description"] = df["description"].str.upper()
    
    df = df[df["description"].str.contains(search_term.upper())]. \
    loc[:,["icd9", "description", "approximate",
           "no map", "combination", "scenario", "choice list"]]. \
    drop_duplicates()

    return df


