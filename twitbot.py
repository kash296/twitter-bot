import tweepy
from credentials import *
import datetime
import wikipedia

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth) 
user = api.me()

def wiki_search(date):
    search = wikipedia.summary(date).rstrip()
    tweet(search)

def tweet(phrase):
    api.update_status(phrase)

current_date = datetime.datetime.today().strftime('%B_%d')
wiki_search(current_date)
