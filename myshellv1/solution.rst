myshellv1
==========

Prerequisite
-------------

I installed *requests* and *cmd2* modules for this assignment in my 'virt1' environment.

.. code-block::

    (virt1) $ yolk -l
    Python          - 2.7.5        - active development (/usr/lib/python2.7/lib-dynload)
    beautifulsoup4  - 4.2.1        - active
    cmd2            - 0.6.5.1      - active 
    lxml            - 3.2.1        - active
    pip             - 1.3.1        - active
    requests        - 1.2.3        - active
    setuptools      - 0.6c11       - active
    wsgiref         - 0.1.2        - active development (/usr/lib/python2.7)
    yolk            - 0.4.3        - active

    $ python myshellv1.py

A link to the `source code`_.

.. _source code: https://github.com/m0rin09ma3/python-summer-training-2013/blob/master/myshellv1/myshellv1.py

Sample output:
---------------

.. code-block::

    (Cmd) greet
    Hi, m0rin09ma3
    (Cmd) stock GOOG
    910.68

Explanation
------------

In the Application class, there are 2 methods (do_greet() for greeting, do_stock() for getting quotes from specified url)

.. code-block:: python

    def do_greet(self, line):
        print "Hi, %s" % os.getlogin()

    def do_stock(self, line):
        quote = {'s': line, 'f': 'l1'}
        target_url = 'http://download.finance.yahoo.com/d/quotes.csv'
        r = requests.get(target_url, params=quote)
        #print r.url
        print r.text

