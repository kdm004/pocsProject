

# Imports
import tweepy
import json
import csv
import time
from itertools import chain
import pandas as pd
import numpy as np

#--------------------------------------------------------------------------------------------------------------------------------------------------
bearer_token = "AAAAAAAAAAAAAAAAAAAAAHIxjgEAAAAAHBtpIV5008WAMdj3Hd2dapo%2BM6k%3DGfV9iH7qSwlBf8UQcODVI6DW0FaoIT6tfodr38XcVR018cGh6v"
client = tweepy.Client(bearer_token=bearer_token,wait_on_rate_limit = True) # client = tweepy.Client(bearer_token=bearer_token, wait_on_rate_limit = True)
#--------------------------------------------------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------------------------------------------------------
query = ' ("send them back to" OR "send him back to" OR "send her back to" OR "illegals from" OR "illegal aliens from" OR "illegal alien from" OR "illegal immigrants from" OR "illegal immigrant from" OR "illegal criminals from" OR "illegal criminal from" OR "foreign criminals from" OR "foreign criminal from" OR "illegal terrorist from" OR "sending us their criminals" OR "ban people from" OR "deport them" OR "deport people from" OR "deport all these" OR "immigrants from" OR "immigrants" OR "people from") place_country:US -is:retweet' 
start_time = '2010-04-06T00:00:00Z' # CHECK THE YEAR  #paginator will not activate until 31 days is passed. 
end_time = '2022-12-01T00:00:00Z' # CHECK THE YEAR
granularity = 'day'

counts = tweepy.Paginator(
        client.get_all_tweets_count,
        query=query, 
        start_time=start_time,
        end_time=end_time,
        granularity=granularity) 
time.sleep(1)
#--------------------------------------------------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------delete after this--------------------------------------------------------------------------------------------------------
tweet_count = []
    
for count in counts:
        tweet_count.append(count.data) # A single count corresponds to a single day. /// We put the start, end, and tweet_count for each day into a list /// We each element of that data into a dataframe

data = list(chain.from_iterable(tweet_count))
df = pd.DataFrame(data).reindex(['start', 'end', 'tweet_count'], axis=1)
totalCount = sum(df['tweet_count'])
avg = np.mean(df['tweet_count'])

#print(df)
print('totalcount= ',totalCount)
print('avg daily count= ',avg)

df.to_csv('countSheet.csv', index = False)  

