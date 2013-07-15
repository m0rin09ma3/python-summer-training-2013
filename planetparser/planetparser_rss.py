#!/usr/bin/env python
import sys
import requests
#import urllib2
from bs4 import BeautifulSoup, SoupStrainer

def main():
    """
    Fetch data from 'planet.fedoraobject.org' and
    output blog-entry-title & blog-entry-author
    """

    # fetch data
    s_url = 'http://planet.fedoraproject.org'

    f = requests.get(s_url)
    html_doc = f.text
#    try:
#        f = urllib2.urlopen(s_url)
#    except urllib2.URLError:
#        print 'failed to open url', s_url
#    else:
#        html_doc = f.read()
#        f.close()
#        #print html_doc

    # extract title & author
    tags_header = SoupStrainer(id="people_feeds")

    soup = BeautifulSoup(html_doc, "lxml", parse_only=tags_header)
    #print soup

    for link in soup.select('a[href]'):
        if link.string or link.get('title'): # except 'None' and 'None'
            print "author:%s\ttitle:%s" % (link.string, link.get('title'))

    return 0

if __name__ == '__main__':
    sys.exit(main())
