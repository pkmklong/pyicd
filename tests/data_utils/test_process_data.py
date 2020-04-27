import pytest
import pandas as pd

from pyicd.data_utils.format_data import split_flags

@pytest.mark.parametrize("test_input, expected",
[(1, "0,0,0,0,1"), 
(0, "0,0,0,0,0"),
(101, "0,0,1,0,1")
])
def test_split_flags(test_input, expected):
    assert split_flags(test_input) == expected

@pytest.mark.skip()
def test_format_icd(filename: str):
    pass

@pytest.mark.skip()
def test_format_desc(filename: str, codetype: str, separater: str = ","):
    pass


