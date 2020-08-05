""" 
This is a twitter bot which tweets facts from wikipedia about events that took place around the world in previous years on that day.
Uses tweepy, wikipedia and datetime modules.

TODO:
    1. Provide a url to the tweet with a url shortener

"""

import tweepy
from credentials import *
import datetime
import wikipedia

"""
Twitter authentication credentials. A developer account is needed to accomplish this. Provide your credentials and you can access the twitter API
"""

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth) 
user = api.me()

"""
The function wiki_search takes the argument date, which is obtained using the datetime module. The date is formatted using the strftime function,
for example like this - July_31. This is necessary, as the wikipedia url for each date is in this format. The function uses the wikipedia module
to obtain the correct page. Using two filters, we create the range for which we want to generate a list of facts, which will be tweeted on Twitter.        
"""

def wiki_search(date):
    search = wikipedia.search(date)  #Performs a search on wikipedia for the current date
    page = wikipedia.page(search[0])  #Generates the page for the date we want
    content_list = page.content.splitlines()  #Stores the lines of the page into a list
    start_element = "== Events =="  #The filter which is used as the starting point to generate list of facts to be tweeted
    end_element = "== Births =="  #The filter which is used as the end point to generate list of facts to be tweeted
    try:
        start_index = content_list.index(start_element)+1 
        end_index = content_list.index(end_element)
    except ValueError:
        start_index = None
        end_index = None
    
    content_list = content_list[start_index:end_index] #Sets the list of facts to be between the start and end indices
    facts =  list(filter(None,content_list)) #When using splitlines() method, sometimes whitespace characters are present. This removes them
    tweet(facts)

"""
The tweet method takes the argument facts, which is a list generated in the wiki_search method. It iterates over this list to post tweets about the different facts obtained.
The try/except block is used to filter out tweets which exceed Twitter's 240 character limit.
"""
def tweet(facts):
    for fact in facts:
        fact = "On " + present_date + ", " + fact
        try:
            api.update_status(fact)
        except tweepy.error.TweepError:
            print('Tweet exceeds character limit, ignoring.')

current_date = datetime.datetime.today().strftime('%B_%d')
present_date = datetime.datetime.today().strftime('%B %e')
wiki_search(current_date)
