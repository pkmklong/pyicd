"""
This run  pytest for  gems converter utils.
"""
import pytest
import pandas as pd
from pyicd.utils.icd_tools import icd9_to_icd10


#@pytest.mark.skip(reason="not yet implemented.")
def test_icd9_to_icd10():
    
    df_result = icd9_to_icd10(icd_code = "59972", flag = "approximate"). \
    reset_index(drop=True)
    df_expected = pd.DataFrame(
        {
            "source":["59972", "59972", "59972"],
            "icd10":["R311", "R3121", "R3129"],
            "description":[
                     "BENIGN ESSENTIAL MICROSCOPIC HEMATURIA",
                     "ASYMPTOMATIC MICROSCOPIC HEMATURIA",
                     "OTHER MICROSCOPIC HEMATURIA"
                    ]
        }
    )
    pd.testing.assert_frame_equal(df_result, df_expected)
       

@pytest.mark.skip(reason="not yet implemented.")
def test_to_icd9(icd_code: str):
    pass
