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



#----------------------------------------------------------------------------------------------
# # if (word contained by tweet_text has a fuzzywuzzy score of .90 when compared to country_entry):
#       if country_region is Europe:
#               append tweet to df_Europe
# Repeat for each region
#----------------------------------------------------------------------------------------------

# Get all substrings of string
# Using list comprehension + string slicing
list_of_substrings = [tweet_text[i: j] for i in range(len(tweet_text))
          for j in range(i + 1, len(tweet_text) + 1)]
#----------------------------------------------------------------------------------------------
# if { (entry in list_of_substrings) vs (country_entry) } has a fuzzywuzzy score of >= .90:
# if country_region is Europe:
#                append tweet to df_europe
# if country_region is Americas:
#                append tweet to df_americas
# if country_region is Sub-Saharan Africa:
#                append tweet to df_subAfrica




