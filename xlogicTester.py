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
from fuzzyWuzzy import fuzz




df_globe = pd.read_csv('fuzzyCountriesAndRegions.csv')
df_tweets = pd.read_csv('testing4567.csv')
df_result= pd.DataFrame(columns=['sentiment', 'id', 'date', 'text'])


print(df_globe)
print(df_tweets)

word_list = []
for tweetIndex in range(len(df_tweets['text'])):
    word_tokens = word_tokenize(df_tweets['text'][tweetIndex])   
    for token in word_tokens:       
        for name in df_globe['Country']:  
            ratio = fuzz.token_set_ratio(token, name)     
            if ratio >= 90:                                                        
                df_result = df_result.append(df_tweets.iloc[[tweetIndex]])  
                word_list.append(token)

df_result['word'] = word_list


print(df_result)

