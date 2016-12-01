#!/usr/bin/env python
from setuptools import setup
from setuptools import find_packages

setup(
    name='HPC-Wiki-Wordembeddings',
    version='0.0.1',
    description='Docker container for Gensim and word embeddings based on Wikipedia',
    url='http://dbs.cs.uni-duesseldorf.de',
    author='HHU Duesseldorf',
    author_email='liebeck@cs.uni-duesseldorf.de',
    packages=find_packages(exclude=['tests']),
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
    ],
    install_requires=[]
)
