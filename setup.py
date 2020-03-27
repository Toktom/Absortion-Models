﻿# -*- coding: utf-8 -*-
"""
PyAbsorp setup file
=================
@Author: Michael Markus Ackermann
"""

from setuptools import setup

settings = {
    'name': 'PyAbsrop',
    'version': '1.0.0',
    'description': 'Sound absorption coefficient models implemented in Python.',
    'url': 'https://github.com/Toktom/Absorption-Models',
    'author': 'Michael Markus Ackermann',
    'author_email': 'michael_ackermann@outlook.com',
    'license': 'MIT',
    'install_requires': ['numpy', 'scipy'],
    'packages': ['pyabsorp', 'pyabsorp.models']
    }

setup(**settings)
