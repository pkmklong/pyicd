
from distutils.core import setup

setup(name='pyicd',
      version='1.0dev',
      description='Python utilities for ICD code analysis',
      author='Patrick Long',
      py_modules=['runner'],
      packages=
      ['pyicd',
      'pyicd.path_utils',
      'pyicd.data_utils',
      'pyicd.utils'],
      package_dir = {'': 'src'},
      scripts=['src/pyicd/process_data.py']
      #entry_points = {
       # 'console_scripts': ['pyicd-pull-gems=process_data:main']
        #},
        )
