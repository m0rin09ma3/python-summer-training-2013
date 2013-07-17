user_finder
============

This program will read /etc/passwd info and output user who can do aproper login.

    $ python user_finder.py

A link to the `source code`_.

.. _source code: https://github.com/m0rin09ma3/python-summer-training-2013/blob/master/user_finder/user_finder.py

Sample output:
---------------

.. code-block::

    ['root', 'm0rin09ma3', 'git']

Explanation
------------

In the main function, use regular expression to filter out users who has /bin/false or /sbin/nologin default shell. Then output the rest of users.

.. code-block:: python

     all_user = pwd.getpwall()
     #print all_user

     notvalid = re.compile('.*/(nologin|false)')
     print [user.pw_name for user in all_user if not notvalid.match(user.pw_s    hell)]

