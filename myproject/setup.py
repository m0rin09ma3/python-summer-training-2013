#!/usr/bin/env python
"""myshell project"""
from setuptools import setup, find_packages
setup(
    name = "m0rin09ma3-myshell",
    version = "0.1",
    packages = find_packages(),

    # Project uses following 2 modules, so ensure that these modules
    # get installed or upgraded on the target machine
    #
    # 'cmd2' - command-line interpreter (CLI) program package
    # 'requests' - HTTP library
    #
    install_requires = ['cmd2>=0.6.5.1','requests>=1.2.3'],

    # metadata for upload to PyPI
    author = "Shungoh Kaetsu",
    author_email = "shungoh.kaetsu@gmail.com",
    description = "This is a test uploading my project to PyPI",
    platforms = ["Linux"],
    license = "PSF",
    url = "https://github.com/m0rin09ma3/python-summer-training-2013/tree/master/myproject",

)
