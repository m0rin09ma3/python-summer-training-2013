#!/usr/bin/env python
import sys
import feedparser
from optparse import OptionParser

def main():
    """
    Fetch RSS data from 'planet.fedoraobject.org/*.xml' and
    output title & author
    """

    parser = OptionParser()
    parser.set_defaults(rss_format="rss10")
    parser.add_option("-f", "--format", dest="rss_format",
                      help="format: rss10, rss20, or atom", metavar="FORMAT")
    (option, args) = parser.parse_args()
    #print 'RSS format is %s' % option.rss_format

    # fetch data
    s_url = 'http://planet.fedoraproject.org/' + \
            option.rss_format + \
            '.xml'
    f = feedparser.parse(s_url)
    #print 'Total number of post: %d' % len(f)

    if option.rss_format == 'atom': # ATOM
        for a, t in zip( \
            [f.entries[i].author for i in range(len(f))], \
            [f.entries[i].title for i in range(len(f))]):
            print '%s: %s' % (a, t)
    else: # RSS1.0 and RSS2.0
        for i in range(len(f)):
            print f.entries[i].title

    return 0

if __name__ == '__main__':
    sys.exit(main())
