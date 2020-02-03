#!/usr/bin/env python3

import pandas as pd
import urllib.request
import zipfile
import os

from pyicd.data_utils.retrieve_data import retrieve_gems_info, unzip_dir
from pyicd.data_utils.format_data import format_icd, format_desc
from pyicd.data_utils.combine_data import add_icd_desc
from pyicd.path_utils.path_variables import PathVariables


def main():
    print(os.getcwd())
    os.chdir(PathVariables.SAVE_PATH)

    retrieve_gems_info(PathVariables.URL_GEMS, "icd10_gems.zip")
    retrieve_gems_info(PathVariables.URL_ICD10, "icd10_descriptions.zip")
    retrieve_gems_info(PathVariables.URL_ICD9, "icd9_descriptions.zip")
    unzip_dir()

    df_icd10= format_icd("2018_I10gem.txt")
    df_icd9 =  format_icd("2018_I9gem.txt")

    df_icd9_desc = format_desc("CMS32_DESC_LONG_DX.txt", "icd9", separater = ",")
    df_icd10_desc = format_desc("icd10cm_codes_2018.txt", "icd10", separater = "//s")

    add_icd_desc(df_icd9, df_icd9_desc,
                df_icd10, df_icd10_desc)


#if __name__=="__main__":
main()
#collect_gems_data()
