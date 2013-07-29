#!/usr/bin/env python
import sys
import webbrowser
import tweepy
from twython import Twython
import argparse

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

