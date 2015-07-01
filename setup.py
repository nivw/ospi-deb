from setuptools import setup, find_packages
import functools
import os
import platform
import json

_PYTHON_VERSION = platform.python_version()
_in_same_dir = functools.partial( os.path.join, os.path.dirname( __file__ ) )

data_dir=( 'templates', 'static', 'i18n', 'data' )
data_files=[]

for directory in data_dir:
  for root, dirs, files in os.walk( 'ospi/'+directory ):
    for f in files:
      if f.startswith('.') :
        files.remove(f)
    if len(files) and '/.' not in root:
      data_files.append( ( root, [ os.path.join( root, f) for f in files] ))

with open('data_files','w') as f:
  json.dump(data_files, f)
  
with open(_in_same_dir("__version__.py")) as version_file:
  exec(version_file.read()) # pylint: disable=W0122

setup(name='ospi',
      classifiers=[
                    "Programming Language :: Python :: 2.7",
                    "Programming Language :: Python :: 3.4",
      ],
      description='Interval Program for OpenSprinkler Pi',
      license="GPL",
      author='Dan Kimberling',
      author_email='nivwiz@gmail.com',
      version=__version__, # pylint: disable=E0602
      url='https://github.com/Dan-in-CA/OSPi',
      packages=find_packages(exclude=["tests"]),
      data_files=data_files,
      entry_points={
              'console_scripts': [
                      'ospi = ospi:run',
                      ]
              },
      )

"""
                         ('data', glob.glob('ospi/data/*') ),
                         ('blinker', glob.glob('ospi/blinker/*') ),
                         ('static/plugins', glob.glob('ospi/static/plugins/*') ),
                         ('plugins/manifests', glob.glob('ospi/plugins/manifests/*') ),
                         ('i18n/cs_CZ', glob.glob('ospi/i18n/cs_CZ/*') ),
                         ('i18n/fr_FR', glob.glob('ospi/i18n/fr_FR/*') ),
                         ('i18n/es_ES', glob.glob('ospi/i18n/es_ES/*') ),
                         ('i18n/en_US', glob.glob('ospi/i18n/en_US/*') ),
                         ('i18n/de_DE', glob.glob('ospi/i18n/de_DE/*') ),
                         ('i18n/sl_SL', glob.glob('ospi/i18n/sl_SL/*') ),
                         ('i18n', glob.glob('ospi/i18n/*') ),
                         ('templates', glob.glob('ospi/templates/*') ),
                         ('web', glob.glob('ospi/web/*') ),
"""
