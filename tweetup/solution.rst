tweetup
========

Prerequisite
-------------

I installed *tweepy*, *twython* modules for this assignment in my 'virt1' environment. Also, I registered this application to `<https://dev.twitter.com/apps>`_ in order to make it work on my twitter account. I changed access level from "Read only"(default) to "Read and write".

.. code-block::

    (virt1) $ pip list
    tweepy (2.1)
    twython (3.0.0)

.. code-block::

    (virt1) $ python tweetup.py -h
    usage: tweetup.py [-h] -f FILE -d DESCRIPTION [--version]

    post file & comment to twitter

    optional arguments:
      -h, --help            show this help message and exit
      -f FILE, --file FILE
      -d DESCRIPTION, --description DESCRIPTION
      --version             show program's version number and exit

A link to the `source code`_.

.. _source code: https://github.com/m0rin09ma3/python-summer-training-2013/tree/master/tweetup/tweetup.py

Explanation
------------

This program will ask user to input file and description from command line.
Then prompt user to work on twitter authorization process. After completing all these steps, this program will upload the file.

First of all, my main function

.. code-block:: python

    def main():
        """ 
        0. Check command-line arguments
        1. Get Tokens from twitter
        2. Post image file
        """ 
        cmd_args = check_cmd_args()
        #print cmd_args

        dict_tokens = get_tokens()
        #print dict_tokens

        post_img(cmd_args, dict_tokens)

        return 0


    if __name__ == '__main__':
        sys.exit(main())


Whatever the file you specify with '-f' will be posted with the description you specify with '-d'. Imported *argparse* module.

.. code-block:: python

    def check_cmd_args():
        """ check command linke arguments """
        parser = argparse.ArgumentParser(description='post file & \
                                                      comment to twitter')
        parser.add_argument('-f', '--file', required=True)
        parser.add_argument('-d', '--description', required=True)
        parser.add_argument('--version', action='version',
                            version='%(prog)s 1.0')
        args = parser.parse_args()
        #print(args)

        return args

Next function will ask you to interact with twitter api and authorize you for a posting. As you can see, it asks you to input consumer_key & consumer_secret. Then it will bring up a browser and ask you to authorize your operation. If you click 'Authorize it' button, it will show you 8digits newly created PIN code. Program is waiting for your input("Enter a pin number from twitter.com:"). Please enter the PIN code. you will get an access_key & access_secret. Imported *webbrowser* module.

.. code-block:: python

    def get_tokens():
        """
        Query the user for their consumer key/secret
        then attempt to fetch a valid access token.
        """

        tokens = {}
        tokens['consumer_key'] = raw_input('Consumer key: ').strip()
        tokens['consumer_secret'] = raw_input('Consumer secret: ').strip()
        auth = tweepy.OAuthHandler(tokens['consumer_key'],
                                   tokens['consumer_secret'])

        # Open authorization URL in browser
        webbrowser.open(auth.get_authorization_url())

        # Ask user for verifier pin
        pin = raw_input('Enter a pin number from twitter.com: ').strip()

        # Get access token
        access_token = auth.get_access_token(pin)

        # Give user the access token
        tokens.update({'access_key': access_token.key, 'access_secret': access_token.secret})
        #print '  Key: %s' % access_token.key
        #print '  Secret: %s' % access_token.secret

        return tokens

Finally, aggregates all infromation and post it. you should be able to see your new post on twitter.

.. code-block:: python

    def post_img(cmd_args, tokens):
        """ post file and comment to twitter """
        #print cmd_args.file
        #print cmd_args.description
        twitter = Twython(tokens['consumer_key'], tokens['consumer_secret'],
                          tokens['access_key'], tokens['access_secret'])

        # Updating Status with Image
        photo = open(cmd_args.file, 'rb')
        img_post_status = twitter.update_status_with_media(status=cmd_args.description,
                                                           media=photo)
        #print img_post_status


