"""
This script retrieves the raw ICD9 and ICD10 GEMs 
zip files from www.cms.gov and unzips them in a
target directory.
"""

import pandas as pd
import urllib.request
import zipfile
import os

# file access vars
SAVE_PATH = "../data/raw_data/gems/"

URL_CMS = "https://www.cms.gov/Medicare/Coding/"

URL_GEMS = os.path.join(URL_CMS, "ICD10/Downloads/2018-ICD-10-CM-General-Equivalence-Mappings.zip")
URL_ICD10  = os.path.join(URL_CMS, "ICD10/Downloads/2018-ICD-10-Code-Descriptions.zip")
URL_ICD9 =  os.path.join(URL_CMS, "ICD9ProviderDiagnosticCodes/Downloads/ICD-9-CM-v32-master-descriptions.zip")


def retrieve_gems_info(url_path: str, file_name: str):
 
    urllib.request.urlretrieve(url_path, file_name)


def unzip_dir():

    for f in os.listdir("."):
       if f.endswith(".zip"):
            try:
                zip = zipfile.ZipFile(f)
                zip.extractall(path=".")
            except OSError as e:
                print(f"file: {f}, error: {e}")


if __name__=="__main__":

    os.chdir(SAVE_PATH)

    retrieve_gems_info(URL_GEMS, "icd10_gems.zip")

    retrieve_gems_info(URL_ICD10, "icd10_descriptions.zip")

    retrieve_gems_info(URL_ICD9, "icd9_descriptions.zip")

    unzip_dir()
