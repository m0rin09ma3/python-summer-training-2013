#!/usr/bin/env python
import sys
import urllib2

def main():
    """
    Get a quote from specified symbols.
    """
    n_argc = len(sys.argv)
    if n_argc < 2:
        print 'please specify symbol and try again.'
        print 'e.g. sharevalue.py GOOG YHOO ...'
        return 1
    #print n_argc

    l_symbol = []
    l_symbol = [ sys.argv[n] for n in range(1, n_argc) ]
    #print l_symbol

    # s_symbol = 's=GOOG&s=YHOO&...'
    s_symbol = ""
    s_symbol = '&'.join( [ 's=' + l_symbol[n] for n in range(n_argc - 1) ] ) 
    #print s_symbol

    s_url = ""
    s_url = 'http://download.finance.yahoo.com/d/quotes.csv?' + \
    s_symbol + \
    '&f=l1'
    #print s_url

    try:
        f = urllib2.urlopen(s_url)
    except urllib2.URLError:
        print 'failed to open url', s_url
    else:
        l_quote = []
        l_quote = f.readlines() # e.g. ['920.24\r\n', '27.04\r\n']
        f.close()
    #print l_quote

    print "%s".ljust(6) % '\t'.join(l_symbol)
    l_quote = [ s.strip() for s in l_quote ]
    print "%6s" % '\t'.join(l_quote)

    return 0

if __name__ == '__main__':
    sys.exit(main())
