Mount
======

This program takes no command-line argument and output /proc/mount file.

Run the program like::
    
    $ python mount.py

A link to the `source code`_.

.. _source code: https://github.com/m0rin09ma3/python-summer-training-2013/blob/master/mount/mount.py

* line 1

  Sha-Bang

* line 2-3

  Imports modules

* line 5-21

  function 'main'

  - line 6-8

    docstring

  - line 9

    assign a path to a variable called 'mount_file'

  - line 10

    check if the file is regular file and exists

  - line 11

    try block to capture exception when open the file

  - line 16-17

    output file contents to STDOUT and close the file object

* line 23-24

  check top-level script environment and return exit status
