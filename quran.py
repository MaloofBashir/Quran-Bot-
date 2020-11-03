import sys
import requests
import tweepy
import time

from daata import *

import os
from os import environ


consumer_key=environ['consumer_key']
consumer_secret=environ['consumer_secret']

key=environ['key']
secret=environ['secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)


api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

while True:
    id=return_tweetid()
    tweets=api.mentions_timeline(id)
    if tweets:
        for i in reversed(range(len(tweets))):
            tw_text=tweets[i].text.translate(non_bmp_map)
            if "ayah" in tw_text.lower():
                twt=tweets[i]
                Last_reply(twt)
                time.sleep(30)
    else:
        time.sleep(30)
