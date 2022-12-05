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

# Read files
globe_df = pd.read_csv('countriesAndRegions.csv')
tweets_df = pd.read_csv('trainingTweets.csv')

# Filter tweets for those that contain mentions of countries
vals=globe_df.stack().to_list()
tweets_df = tweets_df[tweets_df ['text'].str.contains('|'.join(vals))]


# For case insensitive, replace above block with this:
# vals="({})".format('|'.join(globe_df.stack().str.lower().to_list())) #make all letters lowercase
# tweets_df['matched'] = tweets_df.text.str.lower().str.extract(vals, expand=False)
# tweets_df = tweets_df.dropna()



# Organize dataframe a bit
tweets_df.reset_index()        # doesn't seem to do anything
tweets_df.sort_values(by='id')  # Make sure all tweets sorted by 'id' (highest to lowest)

# Print tweets_df
print(tweets_df)

# write tweets_df to a csv
tweets_df.to_csv('trainingTweets.csv', index = False)  








