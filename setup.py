# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in Juggling_management/__init__.py
from Juggling_management import __version__ as version

setup(
	name='Juggling_management',
	version=version,
	description='a',
	author='Robin',
	author_email='robin.rosenstock@t-online.de',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
