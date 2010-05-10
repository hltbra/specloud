from setuptools import setup, find_packages
import sys, os

version = '0.2.5'

setup(name='pyunitbdd',
      version=version,
      description="install nosetests and plugins to ease bdd unit specs",
      long_description=open('README.rst').read(),
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='test bdd nosetests spec unit',
      author='Hugo Lopes Tavares',
      author_email='hltbra@gmail.com',
      url='http://github.com/hugobr/pyunitbdd',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'nose',
          'pinocchio>=0.2',
          'figleaf',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      pyunitbdd = pyunitbdd:main
      """,
      )
