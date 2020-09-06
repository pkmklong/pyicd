[![Documentation Status](https://readthedocs.org/projects/docs/badge/?version=latest)](https://pyicd.readthedocs.io/en/latest/) Check out the [pyicd documentation on ReadTheDocs](https://pyicd.readthedocs.io/en/latest/).<br>
 [![codecov](https://codecov.io/gh/pkmklong/pyicd/branch/master/graph/badge.svg)](https://codecov.io/gh/pkmklong/pyicd)

# pyicd (WIP)
A python package with basic utilities for ICD-9-CM and ICD-10-CM codes.


## Toolkit
<b>Convert between ICD-9-CM and ICD-10-CM using General Equivalency Maps (GEMs)</b>
- Forward and backward ICD mapping
- Filter by GEMs flag type

<b>Lexical ICD-9-CM and ICD-10-CM querying</b>
- Search ICD-9 or ICD-10 codes by clinical keyword 

## About GEMs

<b>GEMs</b><br>
General Equivalency Maps (GEMs) support the interoperability between ICD-9 and ICD-10 codebases and are maintained by the Centers for Medicare and Medicaid Services (CMS). Multiple mapping types may occur including one-to-one and one-to-many. GEMs provide various flags to further characterize these mapping relationships.<br>

<b>Forward mapping</b><br> Mapping from ICD-9 to ICD-10 codes.<br>

<b>Backward mapping</b><br> Mapping from ICD-10 to ICD-9 codes.<br>

<b>Flag types</b><br>
<i>Approximate</i>: Mappings with imperfect correspondence (approximate = 1) or a perfect correspondence (approximate = 0).<br>
<i>No Map</i>: No acceptable GEMs mapping exists (no map = 1) or one or greater mappings exist (no map = 0).<br>
<i>Combination</i>: Mapping is one-to-many (combination = 1) or one-to-one (combination = 0). <br>
<i>Scenario</i>: Multiple target codes are required to complete mapping (scenario = 1) or multiple target codes are not required (scenario = 0)<br>
<i>Choice list</i>: Used on conjuction with the combination flag to direct alternatives when mappings are one-to-many. If a single combination mapping exists: choice list = 1, if more than one combination mapping exists: choice list = 2, if no combination mapping exists: choice list = 0 <br>

## Examples

<i>Installation</i>

    $ python -m pip install git+https://github.com/pkmklong/pyicd.git


<i>Forward mapping</i>

```python
from pyicd.utils.icd_tools import icd9_to_icd10

icd9_to_icd10(icd_code = "59972", flag = "approximate")

source  icd10                                description
59972   R311     BENIGN ESSENTIAL MICROSCOPIC HEMATURIA
59972  R3121         ASYMPTOMATIC MICROSCOPIC HEMATURIA
59972  R3129                OTHER MICROSCOPIC HEMATURIA
``` 

<i>Backward mapping</i>

```python
from pyicd.utils.icd_tools import icd10_to_icd9

icd10_to_icd9(icd_code = "R6521", show_flags = True)

source   icd9    description  approximate  no map  combination    scenario  choice list  
R6521  99592  SEVERE SEPSIS            1       0            1           1            2  
R6521  78552   SEPTIC SHOCK            1       0            1           1            1          
```

<i>Search by clinical term</i>
  
 ```python
from pyicd.utils.icd_tools import search_icd10

search_icd10(search_term = "fibrillation")

icd10                        description
I4891    UNSPECIFIED ATRIAL FIBRILLATION
I4901           VENTRICULAR FIBRILLATION

```





## Notice of Non-Affiliation and Disclaimer 
The author of this library is not affiliated, associated, authorized, endorsed by, or in any way officially connected with Centers for Medicare and Medicaid Services (CMS), or any of its subsidiaries or its affiliates.


