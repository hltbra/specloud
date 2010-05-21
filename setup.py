from setuptools import setup, find_packages
import sys, os

version = '0.3'
here = os.path.abspath(os.path.dirname(__file__))
long_description = open(os.path.join(here, 'README.rst')).read()

setup(name='specloud',
      version=version,
      description="install nosetests and plugins to ease bdd unit specs",
      long_description=long_description,
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='test bdd nosetests spec unit',
      author='Hugo Lopes Tavares',
      author_email='hltbra@gmail.com',
      url='http://github.com/hugobr/specloud',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'nose',
          # this dependency is not set up properly in PyPI
          #'pinocchio',
          'figleaf',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      specloud = specloud:main
      """,
      )
