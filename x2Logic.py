
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
import time
from fuzzywuzzy import fuzz






# Read in 'Country' and 'Region' file as a dataframe
globe_df = pd.read_csv('fuzzyCountriesAndRegions.csv')
df_tweets = pd.read_csv('testing4567.csv')




# initialize dataframe filtered for tweets with country or region names mentioned
df_tweetsWithNames = pd.DataFrame(columns=['sentiment', 'id', 'date', 'text'])

for tweetIndex, row in df_tweets.iterrows():
    word_tokens = word_tokenize(df_tweets['text'][tweetIndex])      # tokenize tweet
    for token in word_tokens:               # for each token
        for globeIndex in range(len(globe_df['Country'])):
            if fuzz.token_set_ratio(token, globe_df['Country'][globeIndex]) >= .90:
                df_tweetsWithNames = df_tweetsWithNames.append(df_tweets.iloc[[tweetIndex]])        # I think this line needs to be df_tweetsWithNames = df_tweetsWithNames.append(df_tweets.iloc[[tweetIndex]])


# Sort Tweets by newest to oldest      (Oldest 1000 tweets as a train/test dataset. The rest will be our unevaluated data)
df_tweetsWithNames.sort_values('id')


# Convert df_tweetsWithNames to csv file
df_tweetsWithNames.to_csv('trainingTweetsWithNames.csv', index = False)