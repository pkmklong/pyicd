"""
This module provides functionality to:
1. retrieves the raw ICD9 and ICD10 GEMs zip files from www.cms.gov
2. unzips them in a target directory.
"""

import pandas as pd
import urllib.request
import zipfile
import os


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
