# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in mudra/__init__.py
from mudra import __version__ as version

setup(
	name='mudra',
	version=version,
	description='mudra',
	author='Vigneshwaran Arumainayagam',
	author_email='vignesh.this@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
