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

with open('data_files.json','w') as f:
  json.dump(data_files, f)

with open('packages.json', 'w') as f:
  json.dump( find_packages(), f )
      
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
