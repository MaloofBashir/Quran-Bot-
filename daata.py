import csv
import random
import textwrap
import json
import requests
import tweepy
import time
from requests.exceptions import ConnectionError
from dictionary import *
import os
from os import environ

consumer_key=environ['consumer_key']
consumer_secret=environ['consumer_secret']

key=environ['key']
secret=environ['secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)


api = tweepy.API(auth,wait_on_rate_limit=True)

"""Fetching the text data from the tweet and coverting it into a dictionary"""
def FetchData(string):
    try:
        s=string.replace(',',' ').split()
        t=[]
        r=[]
        for i in s:
            if "=" in i:
                t.append(i)
        for i in t:
            r.append(i.split('='))

        dict={}

        for i in r:
            count=0
            if count%2==0:
                dict[i[0].lower()]=i[1]
                count=count+1
            else:
                dict[i[0]]=i[1]
                count=count+1
        return dict
    except (ValueError,IndexError,KeyError):
        return 0
'''Trauncting the text into the list of strings with each string of length
235 characters'''
text=[]
def TrauncateText(text):
    text=textwrap.wrap(text,235)
    return text

'''return tweet id from the text file'''

def return_tweetid():
    f=open(r"lasttweet.txt")
    tweet_id=f.readline()
    return tweet_id

'''Storing tweet id into the text file'''

def store_tweetid(tweetd_id):
    f=open(r"lasttweet.txt","w")
    f.write(str(tweetd_id))

'''This will reply a list of truncated text to a tweet one by one'''

def reply(text,tweet):
    if text[0]=='Errorr':
        reply_tweet=api.update_status("@"+tweet.user.screen_name+" "+text[1],tweet.id)
        id=reply_tweet.id

    else:
        for i in reversed((range(len(text)))):
            id=tweet.id
            if i==0:
                if len(text)==1:
                    reply_tweet=api.update_status("@"+tweet.user.screen_name+" " +'بسم الله الرحمن الرحيم'+'\n'+ text[i],id)
                    id=reply_tweet.id
                else:
                    no=i+1
                    reply_tweet=api.update_status("@"+tweet.user.screen_name+" T"+str(no)+": "+'بسم الله الرحمن الرحيم'+'\n'+ text[i]+" +",id)
                    id=reply_tweet.id
            elif i != len(text)-1:
                no=i+1
                reply_tweet=api.update_status("@"+tweet.user.screen_name+" T"+str(no)+": "+ text[i]+" +",id)
                id=reply_tweet.id
            else:
                no=i+1
                reply_tweet=api.update_status("@"+tweet.user.screen_name+" T"+str(no)+": "+ text[i],id)
                id=reply_tweet.id



'''This will fetch the text of a particular ayah using API's and will store it
into the list of items '''
def TextData(dict):
        if 's-name' not in dict.keys():
            surah=int(dict['surah'])
        else:
            dict1,dict2=dictionary()
            s1_name=dict['s-name']
            surah=int(dict1[s1_name])

        ayah=int(dict['ayah'])
        if 'ed' not in dict.keys():
            edition='en.ahmedali'
        else:
            if dict['ed']=='urdu':
                edition='ur.ahmedali'
            else:
                edition=dict['ed']


        if surah<=114 and surah>=1:
            full_surah=requests.get('http://api.alquran.cloud/v1/surah/'+str(surah)+'/'+edition)
            full_surah=full_surah.json()
            full_surah=full_surah['data']['ayahs']
            quran_text=full_surah[ayah-1]['text']
            quran_text=textwrap.wrap(quran_text,235)
            return quran_text
        else:
            quran_text=["Error","sorry,we can't interpret your data.Please enter the correct details"]
            return quran_text
'''Doing the whole job of replying,deciphering the whole text
 and replying the tweet with apporopate text'''
def Last_reply(tweet):
    try:
        tweet_text=tweet.text.encode('utf-8')
        tweet_text=tweet_text.decode('unicode-escape')
        dict=FetchData(tweet_text)
        if dict != 0:
            try:
                quran_text=TextData(dict)
            except (KeyError,ValueError,IndexError):
                quran_text=["Error","sorry, we can't interpret your data.please enter the correct details"]
            reply(quran_text,tweet)
            store_tweetid(tweet.id)
            time.sleep(60)
        else:
            quran_text=["Error","sorry, we can't interpret your data.please enter the correct details"]
            reply(quran_text,tweet)
            store_tweetid(tweet.id)
            time.sleep(60)

    except tweepy.TweepError as e:
        print(e.reason)
        time.sleep(60)
    except ConnectionError as e:
        time.sleep(60)
