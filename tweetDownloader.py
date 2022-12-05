

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

#-------------------------------------------------------------------------------------------------------------------------------
# Store bearer_token in variable
bearer_token = "AAAAAAAAAAAAAAAAAAAAAHIxjgEAAAAAHBtpIV5008WAMdj3Hd2dapo%2BM6k%3DGfV9iH7qSwlBf8UQcODVI6DW0FaoIT6tfodr38XcVR018cGh6v"
client = tweepy.Client(bearer_token=bearer_token, wait_on_rate_limit=True)
# Replace with your own search query
query = ' ("send them back to" OR "send him back to" OR "send her back to" OR "illegals from" OR "illegal aliens from" OR "illegal alien from" OR "illegal immigrants from" OR "illegal immigrant from" OR "illegal criminals from" OR "illegal criminal from" OR "foreign criminals from" OR "foreign criminal from" OR "illegal terrorist from" OR "sending us their criminals" OR "ban people from" OR "deport them" OR "deport people from" OR "deport all these" OR "immigrants from" OR "immigrants" OR "people from") place_country:US -is:retweet' 
# Replace with time period of your choice
start_time = '2010-04-06T00:00:00Z' 
# Replace with time period of your choice
end_time = '2022-12-03T00:00:00Z' 
tweets = tweepy.Paginator(client.search_all_tweets, query=query,
                              tweet_fields=['created_at'], start_time = start_time, end_time = end_time, max_results=100).flatten(limit=1000)
#-------------------------------------------------------------------------------------------------------------------------------
# Clean tweets

#HappyEmoticons
emoticons_happy = set([
    ':-)', ':)', ';)', ':o)', ':]', ':3', ':c)', ':>', '=]', '8)', '=)', ':}',
    ':^)', ':-D', ':D', '8-D', '8D', 'x-D', 'xD', 'X-D', 'XD', '=-D', '=D',
    '=-3', '=3', ':-))', ":'-)", ":')", ':*', ':^*', '>:P', ':-P', ':P', 'X-P',
    'x-p', 'xp', 'XP', ':-p', ':p', '=p', ':-b', ':b', '>:)', '>;)', '>:-)',
    '<3'
    ])

# Sad Emoticons
emoticons_sad = set([
    ':L', ':-/', '>:/', ':S', '>:[', ':@', ':-(', ':[', ':-||', '=L', ':<',
    ':-[', ':-<', '=\\', '=/', '>:(', ':(', '>.<', ":'-(", ":'(", ':\\', ':-c',
    ':c', ':{', '>:\\', ';('
    ])

#Emoji patterns, don't remove them, just define them?
emoji_pattern = re.compile("["
         u"\U0001F600-\U0001F64F"  # emoticons
         u"\U0001F300-\U0001F5FF"  # symbols & pictographs
         u"\U0001F680-\U0001F6FF"  # transport & map symbols
         u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
         u"\U00002702-\U000027B0"
         u"\U000024C2-\U0001F251"
         "]+", flags=re.UNICODE)

#combine sad and happy emoticons
emoticons = emoticons_happy.union(emoticons_sad)

def clean_tweets(tweet):     
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(tweet)
    #after tweepy preprocessing the colon symbol left remain after removing mentions
    tweet = re.sub(r':', '', tweet)
    tweet = re.sub(r'‚Ä¶', '', tweet)
    #replace consecutive non-ASCII characters with a space
    tweet = re.sub(r'[^\x00-\x7F]+',' ', tweet)
    #remove emojis from tweet
    tweet = emoji_pattern.sub(r'', tweet)
    #filter using NLTK library append it to a string
    filtered_tweet = [w for w in word_tokens]    #   filtered_tweet = [w for w in word_tokens if not w in stop_words]
    filtered_tweet = []
    #looping through conditions
    for w in word_tokens:
        #check tokens against stop words , emoticons and punctuations
        if  w not in emoticons and w not in string.punctuation:    #        if w not in stop_words and w not in emoticons and w not in string.punctuation:
            filtered_tweet.append(w)
    fresh_tweet = ' '.join(filtered_tweet)

    return fresh_tweet
#-------------------------------------------------------------------------------------------------------------------------------
# Append tweet information to lists
sentiment_list = []
id_list = []
created_at_list = []
text_list = []
for tweet in tweets:
    sentiment_list.append('0')
    id_list.append(tweet.id)
    created_at_list.append(tweet.created_at)
    text_list.append(tweet.text)
    time.sleep(1)

# Append clean Tweets to a list by calling method on each one                                       # DON'T CLEAN TWEETS UNTIL END? Don't take out stopwords for when you evaluate the tweet.
clean_tweet_list = []
for entry in text_list:
    clean_tweet_list.append(clean_tweets(entry))

#-------------------------------------------------------------------------------------------------------------------------------
# Put lists in a dictionary
tweet_dic = {'sentiment':sentiment_list, 'id':id_list, 'date':created_at_list, 'text':clean_tweet_list}
# Convert dictionary to dataframe
df = pd.DataFrame(tweet_dic, columns = ['sentiment','id','date','text'])

print(df)
df.sort_values('id')                                                       # Sorting by id will also sort from newest to oldest
print('--------------------HelloThere!---------------------')
print(df)
df.to_csv('trainingTweets.csv', index = False)  

#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
# I have edited this file to not remove stopwords. You can replace the lines with the commented our ones to remove them once again if that's necessary.