## pyicd (WIP)

## Basic functionality

- Query individual or batches of ICD9 and ICD10 codesets for validity and clinical descriptions
- Analyze ICD9 or ICD10 hierarchies 
- Search ICD9 or ICD10 codes by keyword and edit distance
- Basic mapping of ICD-9 to ICD-10 codes and ICD-10 or ICD-9 codes using GEMS cross-walks

## Examples
Basic code queries

```python
from pyicd import icd9_to_icd10

icd9_to_icd10("0010")
``` 
|icd9   |icd10  | description
|:------|:------|:----------------------------------------------------
|0010   |A000   | Cholera due to Vibrio cholerae 01, biovar cholerae

```python
from pyicd import icd10_to_icd9

icd10_to_icd9("A0101")
```

|icd10  |icd9  | description
|:------|:-----|:-------------------------------
|A0101  |0020  | Typhoid fever

Batch code queries <TO DO>

Analyze ICD hierarchies <TO DO>



## Notice of Non-Affiliation and Disclaimer 
The author of this library is not affiliated, associated, authorized, endorsed by, or in any way officially connected with CMS, or any of its subsidiaries or its affiliates.
