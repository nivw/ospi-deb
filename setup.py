from setuptools import setup, find_packages
import functools
import os
import platform
import json

_PYTHON_VERSION = platform.python_version()
_in_same_dir = functools.partial( os.path.join, os.path.dirname( __file__ ) )

project_name='OSPi'
data_dir=( 'templates', 'static', 'i18n', 'data' )
package_data=[]
for directory in data_dir:
  for root, dirs, files in os.walk( os.path.join(project_name, directory) ):
    if len(files) :
      temp_list=root.split('/')
      temp_list.remove(project_name)
      path='/'.join( temp_list )
      package_data.extend( [ os.path.join( path, f) for f in files] )

with open('data_files.json','w') as f:
  json.dump(data_files, f)

with open('packages.json', 'w') as f:
  json.dump( find_packages(), f )

with open('package_data', 'w') as f:
  for s in package_data:
        f.write(s + '\n')
      
with open(_in_same_dir("__version__.py")) as version_file:
  exec(version_file.read()) # pylint: disable=W0122

install_requires = [
  "Adafruit_BBIO",
  ]

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
      package_dir={project_name : project_name },
      package_data={project_name : package_data},
      include_package_data=True,
      install_requires=install_requires,
      entry_points={
              'console_scripts': [
                      'ospi = ospi:run',
                      ]
              },
      )
