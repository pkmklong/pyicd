import pytest
import pandas as pd
from pyicd.data_utils import format_data as form


@pytest.mark.parametrize("test_input, expected",
[(1, "0,0,0,0,1"), 
(0, "0,0,0,0,0"),
(101, "0,0,1,0,1")
])
def test_split_flags(test_input, expected):
    assert form.split_flags(test_input) == expected

    
def test_format_flags():
    df_input = pd.DataFrame({"flags":["10101"]})
    df_expected = pd.DataFrame({"approximate":["1"],
                                "no map":["0"], 
                                "combination":["1"],
                                "scenario":["0"],
                                "choice list":["1"]})
    df_result = form.format_flags(df_input)
    pd.testing.assert_frame_equal(df_result, df_expected)


@pytest.mark.skip()
def test_format_icd(filename: str):
    pass

@pytest.mark.skip()
def test_format_desc(filename: str, codetype: str, separater: str = ","):
    pass


