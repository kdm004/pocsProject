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
from fuzzywuzzy import fuzz


# Read in files to dataFrames
globe_df = pd.read_csv('fuzzyCountriesAndRegions.csv')
tweets_df = pd.read_csv('trainingTweetsHalf1.csv')
tweets_df = pd.read_csv('trainingTweetsHalf2.csv')

# Print initial globe_df
print(globe_df)

# Print unique regions in globe_df
unique_regions = globe_df.Region.unique()
print(unique_regions)

# Print sorted globe_df by 'Region' and reset index
globe_df = globe_df.sort_values(['Region'])
globe_df = globe_df.reset_index()
print(globe_df)



# initialize region dataframes
df_americas = pd.DataFrame(columns=['sentiment', 'id', 'date', 'text'])
df_centralAsia = pd.DataFrame(columns=['sentiment', 'id', 'date', 'text'])
df_eastAsia = pd.DataFrame(columns=['sentiment', 'id', 'date', 'text'])
df_europe = pd.DataFrame(columns=['sentiment', 'id', 'date', 'text'])
df_indianSub = pd.DataFrame(columns=['sentiment', 'id', 'date', 'text'])
df_MENA = pd.DataFrame(columns=['sentiment', 'id', 'date', 'text'])
df_pacific = pd.DataFrame(columns=['sentiment', 'id', 'date', 'text'])
df_southAsia = pd.DataFrame(columns=['sentiment', 'id', 'date', 'text'])
df_subAfrica = pd.DataFrame(columns=['sentiment', 'id', 'date', 'text'])
#--------------------------------------------------------------------------------------------

# For each tweet, get the substrings and...        # might want to get word tokens instead of substrings::::     word_tokens = word_tokenize(tweet)
for tweetIndex in range(len(tweets_df['text'])):
    list_of_substrings = [tweets_df['text'][tweetIndex][i: j] for i in range(len(tweets_df['text'][tweetIndex]))        # Overwrite list_of_substrings with substrings of next Tweet
          for j in range(i + 1, len(tweets_df['text'][tweetIndex]) + 1)]

# For each substring in a tweet, compare it to an entry in the 'Country' column, and add it to a dataframe if the match is >= .90
    for substring in list_of_substrings:
        for globeIndex in range(len(globe_df['Country'])):
            if fuzz.token_set_ratio(substring, globe_df['Country'][globeIndex]) >= .90:

# Add Tweet info to dataframe if it mentions this country or region
                if globe_df['Region'][globeIndex] == 'Americas':
                    df_americas.append(tweets_df.iloc[[tweetIndex]])
               
                if globe_df['Region'][globeIndex] == 'Central Asia':
                    df_centralAsia.append(tweets_df.iloc[[tweetIndex]])

                if globe_df['Region'][globeIndex] == 'East Asia':
                    df_eastAsia.append(tweets_df.iloc[[tweetIndex]])

                if globe_df['Region'][globeIndex] == 'Europe':
                    df_europe.append(tweets_df.iloc[[tweetIndex]])

                if globe_df['Region'][globeIndex] == 'Indian Subcontinent':
                    df_indianSub.append(tweets_df.iloc[[tweetIndex]])

                if globe_df['Region'][globeIndex] == 'MENA':
                    df_MENA.append(tweets_df.iloc[[tweetIndex]])

                if globe_df['Region'][globeIndex] == 'Pacific':
                    df_pacific.append(tweets_df.iloc[[tweetIndex]])

                if globe_df['Region'][globeIndex] == 'South Asia':
                    df_southAsia.append(tweets_df.iloc[[tweetIndex]])

                if globe_df['Region'][globeIndex] == 'Sub-Saharan Africa':
                    df_subAfrica.append(tweets_df.iloc[[tweetIndex]])

# Sort each dataframe by id so it's in order of newest to oldest tweets
df_americas = df_americas.sort_values(['id'])
df_centralAsia = df_centralAsia.sort_values(['id'])
df_eastAsia = df_eastAsia.sort_values(['id'])
df_europe = df_europe.sort_values(['id'])
df_indianSub = df_indianSub.sort_values(['id'])
df_MENA = df_MENA.sort_values(['id'])
df_pacific = df_pacific.sort_values(['id'])
df_southAsia = df_southAsia.sort_values(['id'])
df_subAfrica = df_subAfrica.sort_values(['id'])

# reset the dataframe indices
df_americas = df_americas.reset_index()
df_centralAsia = df_centralAsia.reset_index()
df_eastAsia = df_eastAsia.reset_index()
df_europe = df_europe.reset_index()
df_indianSub = df_indianSub.reset_index()
df_MENA = df_MENA.reset_index()
df_pacific = df_pacific.reset_index()
df_southAsia = df_southAsia.reset_index()
df_subAfrica = df_subAfrica.reset_index()


    

# BLOCK A
    # for entry in list_of_substrings:
        # for country_name in 'Country' column:
            # if (entry vs country_entry) has fuzzyScore >= .90:

# BLOCK B
                # if country_region[country_entry index] == Europe:
                    # append tweet_info to df_Europe
                # if country_region[country_entry index] == Americas:
                    # append tweet_info to df_Americas
                # if ... 

