Pyicd documentation
=====================================
A small python utility for basic ICD-9-CM and ICD-10-CM GEMs cross-walking.

About GEMs
^^^^^^^^^^
General Equivalency Maps (GEMs) support the interoperability between ICD-9 and ICD-10 codebases and are maintained by the Centers for Medicare and Medicaid Services (CMS). Multiple mapping types may occur including one-to-one and one-to-many. GEMs provide various flags to further characterize these mapping relationships.

Map between ICD-9-CM and ICD-10-CM
 - Forward mapping: ICD-9 to ICD-10 codes
 - Backward mapping: ICD-10 to ICD-9 codes
 
Filter by map type
 - Approximate: 
     - Imperfect correspondence: approximate = 1
     - Perfect correspondence: approximate = 0
 - No Map: 
     - No acceptable GEMs mapping exists: no map = 1
     - One or greater mappings exist: no map = 0
 - Combination: 
     - Mapping is one-to-many: combination = 1
     - One-to-one: combination = 0
 - Scenario: 
     - Multiple target codes are required to complete mapping: scenario = 1
     - Multiple target codes are not required: scenario = 0
 - Choice list: Used with the combination flag to direct alternatives when mappings are one-to-many
     - A single combination mapping exists: choice list = 1
     - More than one combination mapping exists: choice list = 2
     - No combination mapping exists: choice list = 0

Examples
^^^^^^^^

Installation::

    $ python -m pip install git+https://github.com/pkmklong/pyicd.git

Forward mapping::

    from pyicd.utils.icd_tools import icd9_to_icd10

    icd9_to_icd10(icd_code = "59972", flag = "approximate")

    source  icd10                                description
    59972   R311     BENIGN ESSENTIAL MICROSCOPIC HEMATURIA
    59972  R3121         ASYMPTOMATIC MICROSCOPIC HEMATURIA
    59972  R3129                OTHER MICROSCOPIC HEMATURIA


Backward mapping::

    from pyicd.utils.icd_tools import icd10_to_icd9

    icd10_to_icd9(icd_code = "R6521", show_flags = True)

    source   icd9    description  approximate  no map  combination    scenario  choice list  
    R6521  99592  SEVERE SEPSIS            1       0            1           1            2  
    R6521  78552   SEPTIC SHOCK            1       0            1           1            1          


Search by clinical term::
  
    from pyicd.utils.icd_tools import search_icd10

    search_icd10(search_term = "fibrillation")

    icd10                        description
    I4891    UNSPECIFIED ATRIAL FIBRILLATION
    I4901           VENTRICULAR FIBRILLATION


.. note::
    The author of this library is not affiliated, associated, authorized, endorsed by, or in any way officially connected with Centers for Medicare and Medicaid Services (CMS), or any of its subsidiaries or its affiliates.


.. toctree::
   :maxdepth: 3
   :caption: Contents:

   license



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
