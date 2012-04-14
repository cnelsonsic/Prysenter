#!/bin/env python
from setuptools import setup, find_packages

setup(name='prysenter',
      version='1.0',
      author='Charles Nelson',
      author_email='cnelsonsic@gmail.com',
      packages=find_packages(),
      url='http://git.io/prysenter',
      license='LICENSE.txt',
      description='A minimal, text-only, terminal-only presentation runner.',
      long_description=open('README.txt').read(),
      classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Education',
        'Topic :: Terminals',
        ],
      install_requires=[
          'colorama >= 0.2.4'
          ]
      )
