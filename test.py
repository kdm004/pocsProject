

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


bearer_token = "AAAAAAAAAAAAAAAAAAAAAHIxjgEAAAAAHBtpIV5008WAMdj3Hd2dapo%2BM6k%3DGfV9iH7qSwlBf8UQcODVI6DW0FaoIT6tfodr38XcVR018cGh6v"

client = tweepy.Client(bearer_token=bearer_token, wait_on_rate_limit=True)

# Replace with your own search query
query = 'covid -is:retweet'

# Replace the limit=1000 with the maximum number of Tweets you want
for tweet in tweepy.Paginator(client.search_all_tweets, query=query,
                              tweet_fields=['context_annotations', 'created_at'], max_results=100).flatten(limit=1000):
    print(tweet.id)
    time.sleep(1)