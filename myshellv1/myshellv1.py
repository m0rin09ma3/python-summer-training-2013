import os
import requests
from cmd2 import Cmd

__version__ = '0.1'

class Application(Cmd):
    """
    The main Application class
    """

    def __init__(self):
        Cmd.__init__(self)

    def do_greet(self, line):
        print "Hi, %s" % os.getlogin()

    def do_stock(self, line):
        quote = {'s': line, 'f': 'l1'}
        target_url = 'http://download.finance.yahoo.com/d/quotes.csv'
        r = requests.get(target_url, params=quote)
        #print r.url
        print r.text

if __name__ == '__main__':
    app = Application()
    app.cmdloop()
