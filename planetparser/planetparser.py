#!/usr/bin/env python
import sys
import urllib2
import re
from bs4 import BeautifulSoup, SoupStrainer

def main():
    """
    Fetch data from 'planet.fedoraobject.org' and
    output blog-entry-title & blog-entry-author
    """

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

    # extract title & author
    tags_header = SoupStrainer(class_="blog-entry-header")

    soup = BeautifulSoup(html_doc, "lxml", parse_only=tags_header)
    #soup = BeautifulSoup(html_doc, "html.parser", parse_only=tags_header)
    #print soup

    for tag in soup.find_all('a', href=re.compile("http:")):
        print tag.string

    return 0

if __name__ == '__main__':
    sys.exit(main())
