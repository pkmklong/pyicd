# pyicd

## Functionality
This helper package:

- Querying ICD9 and ICD10 code sets for validity and clinical descriptions
- Basic mapping of ICD-9 to ICD-10 codes and ICD-10 or ICD-9 codes using GEMS cross-walks


## Examples

```python
from pyicd import icd9_to_icd10, icd10_to_icd9

icd9_to_icd10('0010')
icd10    description
A000     Cholera due to Vibrio cholerae 01, biovar cholerae

icd10_to_icd9("A000")
icd9   description
0010   Cholera due to vibrio cholerae
```
