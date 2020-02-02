import os


class PathVariables(object):

    SAVE_PATH: str = "./data/raw_data/gems/"
    URL_CMS: str = "https://www.cms.gov/Medicare/Coding/"
    URL_GEMS: str = os.path.join(URL_CMS, "ICD10/Downloads/2018-ICD-10-CM-General-Equivalence-Mappings.zip")
    URL_ICD10: str  = os.path.join(URL_CMS, "ICD10/Downloads/2018-ICD-10-Code-Descriptions.zip")
    URL_ICD9: str =  os.path.join(URL_CMS, "ICD9ProviderDiagnosticCodes/Downloads/ICD-9-CM-v32-master-descriptions.zip")


