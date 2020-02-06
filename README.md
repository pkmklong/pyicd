# pyicd (WIP)
A python package for ICD analysis.


## Basic functionality
- Mapping of ICD-9 to ICD-10 codes and ICD-10 or ICD-9 codes using GEMS cross-walks

- Filter GEMS mappings by cross-walk types

- Query individual or batches of ICD9 and ICD10 codesets for validity and clinical descriptions

- Check ICD9 or ICD10 hierarchies 

- Search ICD9 or ICD10 codes by keyword and edit distance


## Examples
<b>GEMS mapping</b>

<i>From ICD-9-CM to ICD-10-CM (forward mapping)</i>

```python
from pyicd.utils.icd_tools import icd9_to_icd10

icd9_to_icd10(icd_code = "59972", map_type = "approximate")

source	icd10	  description	                            approximate	no map	combination	scenario	choice list
59972	  R311	  BENIGN ESSENTIAL MICROSCOPIC HEMATURIA	1	          0	      0          	0        	0
59972	  R3121 	ASYMPTOMATIC MICROSCOPIC HEMATURIA	    1	          0	      0	          0	        0
59972	  R3129	  OTHER MICROSCOPIC HEMATURIA	            1	          0	      0	          0	        0
``` 


<i>From ICD-10-CM to ICD-9-CM (backward mapping)</i>

```python
from pyicd.utils.icd_tools import icd10_to_icd9

icd10_to_icd9(icd_code = "R6521")

source	icd9	  description	    approximate	no map	combination	scenario	choice list
R6521 	99592	  SEVERE SEPSIS	  1	          0	      1	          1	        2
R6521	  78552 	SEPTIC SHOCK	  1	          0	      1	          1	        1
```


<b>Search by clinical term</b><TO DO>
  
 ```python
from pyicd.utils.icd_tools import search_icd10

search_icd10(search_term = "fibrillation")

source	icd10	  description	                      approximate	no map	combination	scenario	choice list
42731	  I4891	  UNSPECIFIED  ATRIAL FIBRILLATION	1	          0	      0	          0	        0
42741 	I4901	  VENTRICULAR FIBRILLATION	        0	          0	      0	          0	        0
```


<b>Batch mapping</b><TO DO>

<b>Check ICD hierarchies</b> <TO DO>



## Notice of Non-Affiliation and Disclaimer 
The author of this library is not affiliated, associated, authorized, endorsed by, or in any way officially connected with CMS, or any of its subsidiaries or its affiliates.

