planetparser
=============

Prerequisite
-------------

I installed *beautifulsoup4*, *lxml*, and *requests* modules for this assignment in my 'virt1' environment.

.. code-block::

    (virt1) $ yolk -l
    Python          - 2.7.5        - active development (/usr/lib/python2.7/lib-dynload)
    beautifulsoup4  - 4.2.1        - active
    lxml            - 3.2.1        - active
    pip             - 1.3.1        - active
    requests        - 1.2.3        - active 
    setuptools      - 0.6c11       - active
    wsgiref         - 0.1.2        - active development (/usr/lib/python2.7)
    yolk            - 0.4.3        - active

This program will read `a web page`_ and output blog title and author.

.. _a web page: http://planet.fedoraproject.org

    $ python planetparser_rss.py

A link to the `source code`_.

.. _source code: https://github.com/m0rin09ma3/python-summer-training-2013/blob/master/planetparser/planetparser_rss.py

Sample output:
---------------

.. code-block::

    author:pingou   title:Le blog de pingou - Tag - Fedora-planet
    author:pjp      title:pjp's blog
    author:tuxdna   title:DNA of the TUX

Explanation
------------

In the main function, retrieve data from URL and store them into a string.

.. code-block:: python

    # fetch data
    s_url = 'http://planet.fedoraproject.org'

    # fetch data
    s_url = 'http://planet.fedoraproject.org'

    f = requests.get(s_url)
    html_doc = f.text

Using following filter conditions to retrieve blog title & author

1. extract data under <ul id="people_feeds"> tag
#. extract title & author

.. code-block:: python

    # extract title & author
    tags_header = SoupStrainer(id="people_feeds")

    soup = BeautifulSoup(html_doc, "lxml", parse_only=tags_header)
    #print soup

    for link in soup.select('a[href]'):
        if link.string or link.get('title'): # except 'None' and 'None'
            print "author:%s\ttitle:%s" % (link.string, link.get('title'))

