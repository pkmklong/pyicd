# pyicd (WIP)
A python package for ICD analysis.


## Functionality
<b>Convert between ICD-9-CM and ICD-10-CM using General Equivalency Map (GEMs)</b>
- Forward and backward ICD mapping
- Map by GEMs cross-walk flag type

<b>Lexical ICD-9-CM and ICD-10-CM querying</b>
- Search ICD9 or ICD10 codes by clinical keyword 
- Query ICD codes by Word2Vec imbeddings

## Examples
<b>GEMS mapping</b>

<i>Forward mapping (from ICD-9-CM to ICD-10-CM)</i>

```python
from pyicd.utils.icd_tools import icd9_to_icd10

icd9_to_icd10(icd_code = "59972", flag = "approximate")

source  icd10                                description  approximate  \
59972   R311     BENIGN ESSENTIAL MICROSCOPIC HEMATURIA            1   
59972  R3121         ASYMPTOMATIC MICROSCOPIC HEMATURIA            1   
59972  R3129                OTHER MICROSCOPIC HEMATURIA            1   

      no map  combination  scenario  choice list  
7657       0            0         0            0  
7658       0            0         0            0  
7659       0            0         0            0  
``` 


<i>Backward mapping (from ICD-10-CM to ICD-9-CM)</i>

```python
from pyicd.utils.icd_tools import icd10_to_icd9

icd10_to_icd9(icd_code = "R6521")

source   icd9    description  approximate  no map  combination  \
R6521  99592  SEVERE SEPSIS            1       0            1   
R6521  78552   SEPTIC SHOCK            1       0            1   

       scenario  choice list  
         1            2  
         1            1  
```


<b>Search by clinical term</b>
  
 ```python
from pyicd.utils.icd_tools import search_icd10

search_icd10(search_term = "fibrillation")

source  icd10                        description  approximate  no map  \
42731  I4891    UNSPECIFIED ATRIAL FIBRILLATION            1       0   
42741  I4901           VENTRICULAR FIBRILLATION            0       0   

      combination  scenario  choice list  
            0         0            0  
            0         0            0  
```





## Notice of Non-Affiliation and Disclaimer 
The author of this library is not affiliated, associated, authorized, endorsed by, or in any way officially connected with CMS, or any of its subsidiaries or its affiliates.

