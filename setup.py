
from distutils.core import setup

setup(name='pyicd',
      version='1.0dev',
      description='Python utilities for ICD code analysis',
      author='Patrick Long',
      py_modules=['runner'],
      packages=['pyicd'],
      package_dir = {'': 'src'}
     )
