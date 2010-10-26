from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='normaltemplate',
      version=version,
      description="",
      long_description="""port of javascript normaltemplate to python\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='templates',
      author='Tassos Koutsovassilis',
      author_email='tkouts@innoscript.org',
      url='http://www.innoscript.org',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
