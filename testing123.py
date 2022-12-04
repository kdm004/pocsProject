

# Imports
import tweepy
import json
import csv
from itertools import chain
import pandas as pd
import numpy as np
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string






client = tweepy.Client(bearer_token="AAAAAAAAAAAAAAAAAAAAAHIxjgEAAAAAHBtpIV5008WAMdj3Hd2dapo%2BM6k%3DGfV9iH7qSwlBf8UQcODVI6DW0FaoIT6tfodr38XcVR018cGh6v", wait_on_rate_limit=True)

query = ' ("send them back to" OR "send him back to" OR "send her back to" OR "illegals from" OR "illegal aliens from" OR "illegal alien from" OR "illegal immigrants from" OR "illegal immigrant from" OR "illegal criminals from" OR "illegal criminal from" OR "foreign criminals from" OR "foreign criminal from" OR "illegal terrorist from" OR "sending us their criminals" OR "ban people from" OR "deport them" OR "deport people from" OR "deport all these" OR "immigrants from" OR "immigrants" OR "people from") place_country:US -is:retweet' 

start_time = '2010-04-06T00:00:00Z' # CHECK THE YEAR  #paginator will not activate until 31 days is passed. 
end_time = '2022-12-02T00:00:00Z' # CHECK THE YEAR
tweets = tweepy.Paginator(client.search_all_tweets, query=query,
                              tweet_fields=['created_at'], start_time = start_time, end_time = end_time, max_results=100).flatten(limit=125)
for tweet in tweets:
    print(f"Tweet ID: {tweet.id}\nText: {tweet.text},\nCreated at: {tweet.created_at}\n\n")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# tweets = tweepy.Paginator(client.search_all_tweets(query=query, tweet_fields=['context_annotations', 'created_at', 'geo'], # Do I need context_annotations?
                                
#                                   place_fields = ['place_type','geo'], expansions='geo.place_id',
#                                   start_time=start_time,
#                                   end_time=end_time, max_results=100)).flatten(limit=101)




# tweets= tweepy.Paginator(client.search_all_tweets, query=query,
#                               tweet_fields=['created_at'], max_results=100).flatten(limit=200)