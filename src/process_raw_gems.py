"""
This script processes the raw ICD9 <-> ICD10 GEMs files 
retrieved from  
"""

import pandas as pd
import urllib.request

if __name__=="__main__":

    url_gems = "https://www.cms.gov/Medicare/Coding/ICD10/Downloads/2018-ICD-10-CM-General-Equivalence-Mappings.zip"

    urllib.request.urlretrieve(url_gems, '../data/raw_data/gems/2018-ICD-10-CM-General-Equivalence-Mappings.zip')

    url_descriptions = "https://www.cms.gov/Medicare/Coding/ICD10/Downloads/2018-ICD-10-Code-Descriptions.zip"

    urllib.request.urlretrieve(url_descriptions, '../data/raw_data/gems/2018-ICD-10-Code-Descriptions.zip')

    
