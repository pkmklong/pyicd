# pyicd (WIP)
A python package for ICD analysis.


## Basic functionality
- Basic mapping of ICD-9 to ICD-10 codes and ICD-10 or ICD-9 codes using GEMS cross-walks
- Query individual or batches of ICD9 and ICD10 codesets for validity and clinical descriptions
- Check ICD9 or ICD10 hierarchies 
- Search ICD9 or ICD10 codes by keyword and edit distance


## Examples
<b>GEMS mapping</b>

<i>From ICD-9-CM to ICD-10-CM aka “forward mapping”</i>
```python
from pyicd.utils.icd_tools import icd9_to_icd10

icd9_to_icd10("59972")

source  icd10                                description
59972    R311     BENIGN ESSENTIAL MICROSCOPIC HEMATURIA
59972   R3121         ASYMPTOMATIC MICROSCOPIC HEMATURIA
59972   R3129                OTHER MICROSCOPIC HEMATURIA
``` 

<i>From ICD-10-CM to ICD-9-CM aka “backward mapping”</i>

```python
from pyicd.utils.icd_tools import icd10_to_icd9

icd10_to_icd9("R6521")

source   icd9     description
R6521   99592    SEPTIC SHOCK
R6521   78552   SEVERE SEPSIS
```

<b>Find codes by clinical term</b><TO DO>
  
 ```python
from pyicd.utils.icd_tools import search_icd10

search_icd10("fibrillation")

icd10	                    description
I4891	UNSPECIFIED ATRIAL FIBRILLATION
I4901	       VENTRICULAR FIBRILLATION
```


<b>Batch mapping</b><TO DO>

<b>Check ICD hierarchies</b> <TO DO>



## Notice of Non-Affiliation and Disclaimer 
The author of this library is not affiliated, associated, authorized, endorsed by, or in any way officially connected with CMS, or any of its subsidiaries or its affiliates.
