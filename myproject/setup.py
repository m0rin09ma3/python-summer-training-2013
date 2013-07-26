#!/usr/bin/env python
"""myshell project"""
from setuptools import setup, find_packages
setup(
    name = "m0rin09ma3-myshell",
    version = "0.2",
    packages = find_packages(),

    # Project uses following 2 modules, so ensure that these modules
    # get installed or upgraded on the target machine
    #
    # 'cmd2' - command-line interpreter (CLI) program package
    # 'requests' - HTTP library
    #
    install_requires = [
    #                    'cmd2>=0.6.5.1',
    #                    'requests>=1.2.3',
                        'cmd2',
                        'requests',
                       ],
    #setup_requires = [
    #                    'cmd2>=0.6.5.1',
    #                    'requests>=1.2.3',
    #                   ],
    # testpypi server does not have these modules as of today July 24, 2013
    dependency_links = [
    #                    'https://pypi.python.org/packages/2.7/c/cmd2/cmd2-0.6.5.1-py2.7.egg#md5=ffceb23ec292b757aa6108c154b10d45#egg=cmd2-0.6.5.1',
    #                    'https://pypi.python.org/packages/source/r/requests/requests-1.2.3.tar.gz#md5=adbd3f18445f7fe5e77f65c502e264fb#egg=requests-1.2.3',
                        'https://pypi.python.org/pypi/cmd2',
                        'https://pypi.python.org/pypi/requests',
                       ],

    # metadata for upload to PyPI
    author = "Shungoh Kaetsu",
    author_email = "shungoh.kaetsu@gmail.com",
    description = "This is a test uploading my project to PyPI",
    platforms = ["Linux"],
    license = "PSF",
    url = "https://github.com/m0rin09ma3/python-summer-training-2013/tree/master/myproject",

)
