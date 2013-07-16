planetparser_rss_v2
====================

Prerequisite
-------------

I installed *feedparser* modules for this assignment in my 'virt1' environment.

.. code-block::

    (virt1) $ yolk -l
    Python          - 2.7.5        - active development (/usr/lib/python2.7/lib-dynload)
    beautifulsoup4  - 4.2.1        - active
    feedparser      - 5.1.3        - active 
    lxml            - 3.2.1        - active
    pip             - 1.3.1        - active
    requests        - 1.2.3        - active 
    setuptools      - 0.6c11       - active
    wsgiref         - 0.1.2        - active development (/usr/lib/python2.7)
    yolk            - 0.4.3        - active

This program will read `RSS1.0`_, `RSS2.0`_, or `ATOM`_ feed and output author and title. Default is RSS1.0.

.. _RSS1.0: http://planet.fedoraproject.org/rss10.xml
.. _RSS2.0: http://planet.fedoraproject.org/rss20.xml
.. _ATOM: http://planet.fedoraproject.org/atom.xml

.. code-block::

    $ python planetparser_rss_v2.py -h
    Usage: planetparser_rss_v2.py [options]

    Options:
      -h, --help            show this help message and exit
        -f FORMAT, --format=FORMAT
                                format: rss10, rss20, or atom

A link to the `source code`_.

.. _source code: https://github.com/m0rin09ma3/python-summer-training-2013/blob/master/planetparser/planetparser_rss_v2.py

Sample output:
---------------

.. code-block::

    Casper: Installation de seeks
    Fedora Indonesia: Mengembalikan Repository Fedora 19 Yang Hilang
    Amit Saha: /proc/cpuinfo on various architectures

Explanation
------------

First of all, setup optionparser

.. code-block:: python

    parser = OptionParser()
    parser.set_defaults(rss_format="rss10")
    parser.add_option("-f", "--format", dest="rss_format",
                     help="format: rss10, rss20, or atom", metavar="FORMAT")
    (option, args) = parser.parse_args()
    #print 'RSS format is %s' % option.rss_format

Retrieve data from URL and store them into a string.

.. code-block:: python

    # fetch data
    s_url = 'http://planet.fedoraproject.org/' + \
            option.rss_format + \
            '.xml'
    f = feedparser.parse(s_url)
    #print 'Total number of post: %d' % len(f)

Retrieve blog author & title

.. code-block:: python

    if option.rss_format == 'atom': # ATOM
        for a, t in zip( \
            [f.entries[i].author for i in range(len(f))], \
            [f.entries[i].title for i in range(len(f))]):
            print '%s: %s' % (a, t)
    else: # RSS1.0 and RSS2.0
        for i in range(len(f)):
            print f.entries[i].title

