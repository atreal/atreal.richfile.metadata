from setuptools import setup, find_packages
import os

version = '1.0.0beta1'

setup(name='atreal.richfile.metadata',
      version=version,
      description="A plugin for atreal.richfile that extracts metadata",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='atreal plone richfile metadata',
      author='atReal',
      author_email='contact@atreal.net',
      url='http://www.atreal.net',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['atreal', 'atreal.richfile'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'hachoir-core==1.2.1',
          'hachoir-parser==1.2.1',
          'hachoir-metadata==1.2.1',
          'atreal.richfile.qualifier',
          'atreal.filestorage.common',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
