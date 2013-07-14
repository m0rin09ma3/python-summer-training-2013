planetparser
=============

Prerequisite
-------------

I installed beautifulsoup4 and lxml modules for this assignment in my 'virt1' environment.

.. code-block::

    (virt1) $ yolk -l
    Python          - 2.7.5        - active development (/usr/lib/python2.7/lib-dynload)
    beautifulsoup4  - 4.2.1        - active
    lxml            - 3.2.1        - active
    pip             - 1.3.1        - active
    setuptools      - 0.6c11       - active
    wsgiref         - 0.1.2        - active development (/usr/lib/python2.7)
    yolk            - 0.4.3        - active

This program will read `a web page`_ and output blog title and author.

.. _a web page: http://planet.fedoraproject.org

    $ python planetparser.py

A link to the `source code`_.

.. _source code: https://github.com/m0rin09ma3/python-summer-training-2013/blob/master/planetparser/planetparser.py

Sample output:
---------------

.. code-block::

    Renich Bon Ciric
    HowTo: Bind10 resolver @ Fedora 19
    Fedora Indonesia
    FAD Klaten 2013; Menuju Klaten Go Online
    Tom 'spot' Callaway
    In Memory of Seth Vidal

Explanation
------------

In the main function, retrieve data from URL and store them into a string.

.. code-block:: python

    # fetch data
    s_url = 'http://planet.fedoraproject.org'

    try:
        f = urllib2.urlopen(s_url)
    except urllib2.URLError:
        print 'failed to open url', s_url
    else:
        html_doc = f.read()
        f.close()
        #print html_doc

Using following filter conditions to retrieve blog title & author

1. extract data under <div class="blog-entry-header"> tag
#. extract string contains '<a href=http:>'

.. code-block:: python

    # extract title & author
    tags_header = SoupStrainer(class_="blog-entry-header")

    soup = BeautifulSoup(html_doc, "lxml", parse_only=tags_header)
    #soup = BeautifulSoup(html_doc, "html.parser", parse_only=tags_header)
    #print soup

    for tag in soup.find_all('a', href=re.compile("http:")):
        print tag.string

