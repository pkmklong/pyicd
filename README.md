# pyicd (WIP)
A python package with basic utilities for ICD-9-CM and ICD-10-CM analysis.


## Toolkit
<b>Convert between ICD-9-CM and ICD-10-CM using General Equivalency Maps (GEMs)</b>
- Forward and backward ICD mapping
- Filter by GEMs flag type

<b>Lexical ICD-9-CM and ICD-10-CM querying</b>
- Search ICD-9 or ICD-10 codes by clinical keyword 

## About GEMs

<i><b>GEMs</i></b><br>
General Equivalency Maps (GEMs) support the interoperability between ICD-9 and ICD-10 codebases and are maintained by the Centers for Medicare and Medicaid Services (CMS). Multiple mapping types may occur including one-to-one and one-to-many. CMS provides various flags to further characterize these mapping relationships.<br>

<i><b>Forward mapping</i></b><br> Mapping from ICD-9 to ICD-10 codes.<br>

<i><b>Backward mapping</i></b><br> Mapping from ICD-10 to ICD-9 codes.<br>

<i><b>Flag types</i></b><br>
Approximate: Mappings with imperfect correspondence (approximate = 1) or a perfect correspondence (approximate = 0).<br>
No Map: No acceptable GEMs mapping exisits (no map = 1) or one or greater mappings exist (no map = 0).<br>
Combination: Mapping is one-to-many (combination = 1) or one-to-one (combination = 0). <br>
Scenario: Multiple target codes are required to complete mapping (scenario = 1) or multiple target codes are not required (scenario = 0)<br>
Choice list: Used on conjuction with the combination flag to direct alternatives when mappings are one-to-many. If a single combination mapping exists: choice list = 1, if more than one combination mapping exists: choice list = 2, if no combination mapping exists: choice list = 0 <br>

## Examples

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


