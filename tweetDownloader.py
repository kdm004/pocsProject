

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
#-------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------------
# Store bearer_token in variable
bearer_token = "AAAAAAAAAAAAAAAAAAAAAHIxjgEAAAAAHBtpIV5008WAMdj3Hd2dapo%2BM6k%3DGfV9iH7qSwlBf8UQcODVI6DW0FaoIT6tfodr38XcVR018cGh6v"
client = tweepy.Client(bearer_token=bearer_token, wait_on_rate_limit=True)
# Replace with your own search query
query = ' ("send them back to" OR "send him back to" OR "send her back to" OR "illegals from" OR "illegal aliens from" OR "illegal alien from" OR "illegal immigrants from" OR "illegal immigrant from" OR "illegal criminals from" OR "illegal criminal from" OR "foreign criminals from" OR "foreign criminal from" OR "illegal terrorist from" OR "sending us their criminals" OR "ban people from" OR "deport them" OR "deport people from" OR "deport all these" OR "immigrants from" OR "invading our country" OR "being invaded" OR "invaders" OR "immigrants") place_country:US -is:retweet' 
# Replace with time period of your choice
start_time = '2010-04-06T00:00:00Z' 
# Replace with time period of your choice
end_time = '2022-12-05T00:00:00Z' 
tweets = tweepy.Paginator(client.search_all_tweets, query=query,
                              tweet_fields=['created_at'], start_time = start_time, end_time = end_time, max_results=10).flatten(limit=10)
#-------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------------
# Append tweet information to lists
sentiment_list = []
id_list = []
created_at_list = []
tweet_list = []
for tweet in tweets:
    sentiment_list.append('0')
    id_list.append(tweet.id)
    created_at_list.append(tweet.created_at)
    tweet_list.append(tweet.text)
    time.sleep(1)


# Read in 'Country' and 'Region' file as a dataframe
globe_df = pd.read_csv('fuzzyCountriesAndRegions.csv')

# Append clean Tweets to a list by calling method on each one                                       # DON'T CLEAN TWEETS UNTIL END? Don't take out stopwords for when you evaluate the tweet.
# tweetsWithNames = []

tweet_dic = {'sentiment':sentiment_list, 'id':id_list, 'date':created_at_list, 'text':tweet_list} # changed to text_list from clean_tweet_list
df_tweets = pd.DataFrame(tweet_dic, columns = ['sentiment','id','date','text'])

# initialize dataframe filtered for tweets with country or region names mentioned
df_tweetsWithNames = pd.DataFrame(columns=['sentiment', 'id', 'date', 'text'])

for tweetIndex in range(len(df_tweets)):
    word_tokens = word_tokenize(df_tweets['text'][tweetIndex])      # tokenize tweet
    for token in word_tokens:               # for each token
        for name in globe_df['Country']:
            fuzzRatio = fuzz.token_set_ratio(token, name)
            if fuzzRatio >= .90:
                df_tweetsWithNames = df_tweetsWithNames.append(df_tweets.iloc[[tweetIndex]])


# for sentenceIndex in range(len(df_sentences['sentence'])):
#     word_tokens = word_tokenize(df_sentences['sentence'][sentenceIndex])    # tokenize the sentence
#     for token in word_tokens:        # for each token
#         for name in df_names['name']:  # for each name
#         #if word == 'kevin':
#             ratio = fuzz.token_set_ratio(token, name)      # compare ratio of token to name
#             if ratio >= 90:                                                        # add sentence to list if it contains a name within the name dataframe (Only kevin)
#                 df_empty = df_empty.append(df_sentences.iloc[[sentenceIndex]])                 



# Sort Tweets by newest to oldest      (Oldest 1000 tweets as a train/test dataset. The rest will be our unevaluated data)
df_tweetsWithNames.sort_values('id')


# Convert df_tweetsWithNames to csv file
df_tweetsWithNames.to_csv('trainingTweetsWithNames.csv', index = False)











#-------------------------------------------------------------------------------------------------------------------------------
# Put lists in a dictionary
# tweet_dic = {'sentiment':sentiment_list, 'id':id_list, 'date':created_at_list, 'text':tweetsWithNames} # changed to text_list from clean_tweet_list
# # Convert dictionary to dataframe
# df = pd.DataFrame(tweet_dic, columns = ['sentiment','id','date','text'])

# print(df)
# df.sort_values('id')                                                       # Sorting by id will also sort from newest to oldest
# print('--------------------HelloThere!---------------------')
# print(df)
# df.to_csv('trainingTweetsHELLO.csv', index = False)  

#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
# I have edited this file to not remove stopwords. You can replace the lines with the commented our ones to remove them once again if that's necessary.