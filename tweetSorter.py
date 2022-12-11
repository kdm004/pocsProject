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

# There are still some URLs in the tweets since we were looking for URLs that started with https, not http. 

# Read in files to dataFrames
tweets_df = pd.read_csv('tweetSheetGeoText.csv')

initial_tweets=[]
for tweet in tweets_df['text']:
    initial_tweets.append(tweet)


cleaned_tweets = []
for tweet in initial_tweets:
 #   print(type(tweet))
    temp = re.sub(r'http\S+', '', str(tweet))
    temp = re.sub(r'(@\S+) | (#\S+)', r'', temp)
    temp = re.sub(r'\s{2,}', ' ', temp)
    cleaned_tweets.append(temp)

tweets_df['text'] = cleaned_tweets




# Organize dataframe a bit
#tweets_df = tweets_df.reset_index()        # doesn't seem to do anything
#tweets_df = tweets_df.sort_values(by='id')  # Make sure all tweets sorted by 'id' (highest to lowest)
tweets_df = tweets_df.sample(frac=1)         # shuffle tweets


# write tweets_df to a csv
tweets_df.to_csv('finalData_cleaned2.csv', index = False)  








