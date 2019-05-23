# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="py-base-resource",
    version="1.0.0",
    description="Python module for file and directory management",
    author="Jhonny Bravo",
    author_email="sanfranceshika5@gmail.com",
    url="https://github.com/JhonnyBravo/py-base-resource.git",
    packages=find_packages(),
    install_requires=[
        "py_status_resource",
        "py_attribute_resource"
    ],
    dependency_links=[
        "git+https://github.com/JhonnyBravo/py-status-resource.git#egg=py_status_resource",
        "git+https://github.com/JhonnyBravo/py-attribute-resource.git#egg=py_attribute_resource"
    ],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ]
)
