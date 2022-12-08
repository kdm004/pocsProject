
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
df_empty= pd.DataFrame(columns=['sentiment', 'id', 'date', 'text'])

print(type(df_tweets['text'][0]))



# for tweetIndex in range(len(df_tweets['text'])):                                                         # good
#     word_tokens = word_tokenize(df_tweets['text'][tweetIndex])      # tokenize tweet                     # good
#     for token in word_tokens:               # for each token                                             # good
#         for name in globe_df['Country']:                                                                 # 
#             fuzzRatio = fuzz.token_set_ratio(token, name)                                         
#             if fuzzRatio >= .90:                                                              
#                 df_tweetsWithNames = df_tweetsWithNames.append(df_tweets.iloc[[tweetIndex]])          

# print(df_tweetsWithNames)



for tweetIndex in range(len(df_tweets['text'])):
    word_tokens = word_tokenize(df_tweets['text'][tweetIndex])    # tokenize the sentence
    for token in word_tokens:        # for each token
        for name in globe_df['Country']:  # for each name
            ratio = fuzz.token_set_ratio(token, name)      # compare ratio of token to name
            if ratio >= 90:                                                        # add sentence to list if it contains a name within the name dataframe (Only kevin)
                df_empty = df_empty.append(df_tweets.iloc[[tweetIndex]])         






print(df_empty)




# # Sort Tweets by newest to oldest      (Oldest 1000 tweets as a train/test dataset. The rest will be our unevaluated data)
# df_tweetsWithNames.sort_values('id')
# df_tweetsWithNames.reset_index

# # Convert df_tweetsWithNames to csv file
# df_tweetsWithNames.to_csv('helloThere.csv', index = False)
