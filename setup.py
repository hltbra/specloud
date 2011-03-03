from setuptools import setup, find_packages
import sys, os

version = '0.4.0'
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
          'figleaf',
          'pinocchio',
          # -*- Extra requirements: -*-
      ],
      dependency_links = [
          'http://darcs.idyll.org/~t/projects/pinocchio-latest.tar.gz#egg=pinocchio-dev',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      specloud = specloud:main
      """,
      )

