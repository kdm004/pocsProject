

# Imports
import tweepy
import json
import csv
from itertools import chain
import pandas as pd
import numpy as np

# Check Tweepy Version Installed
#print(tweepy.__version__)


# Store bearer_token in variable
bearer_token = "AAAAAAAAAAAAAAAAAAAAAHIxjgEAAAAAHBtpIV5008WAMdj3Hd2dapo%2BM6k%3DGfV9iH7qSwlBf8UQcODVI6DW0FaoIT6tfodr38XcVR018cGh6v"


client = tweepy.Client(bearer_token=bearer_token)

# Replace with your own search query
query = ' ("send them back to" OR "send him back to" OR "send her back to" OR "illegals from" OR "illegal aliens from" OR "illegal alien from" OR "illegal immigrants from" OR "illegal immigrant from" OR "illegal criminals from" OR "illegal criminal from" OR "foreign criminals from" OR "foreign criminal from" OR "illegal terrorist from" OR "sending us their criminals" OR "ban people from" OR "deport them" OR "deport people from" OR "deport all these" OR "immigrants from" OR "immigrants" OR "people from") place_country:US -is:retweet' 
          # Triple quotes around a quoted phrase will return the exact phrase. ['word1', 'word2'] gives Tweet with both words. 
                                                                                        # query = ' "is a shithole country" OR "is a shit hole country" place_country:US'   
# Replace with time period of your choice
start_time = '2010-04-06T00:00:00Z' # CHECK THE YEAR  #paginator will not activate until 31 days is passed. 

# Replace with time period of your choice
end_time = '2022-03-11T00:00:00Z' # CHECK THE YEAR

tweets = client.search_all_tweets(query=query, tweet_fields=['context_annotations', 'created_at', 'geo'], # Do I need context_annotations?
                                  
                                  place_fields = ['place_type','geo'], expansions='geo.place_id',
                                  start_time=start_time,
                                  end_time=end_time, max_results=50)




# Prepare to write to csv file
f = open('tweetSheet.csv','w')
writer = csv.writer(f)

# Write to csv file
for tweet in tweets.data:
    print(tweet.text)
    print(tweet.created_at)
    writer.writerow(['0', tweet.id, tweet.created_at, tweet.text])

# Close csv file
f.close()

# # Let's order this into a dataframe, and then put it into a csv. 

#-------------------------------------------------------------------------------------------------------------------------------









# data = list(chain.from_iterable(tweet_count))
# df = pd.DataFrame(data).reindex(['start', 'end', 'tweet_count'], axis=1)
# totalCount = sum(df['tweet_count'])
# avg = np.mean(df['tweet_count'])

# #print(df)
# print('totalcount= ',totalCount)
# print('avg daily count= ',avg)

# df.to_csv('countSheet.csv', index = False)  



# data = []
# for tweet in tweets.data:
# df = pd.DataFrame(tweet
# totalCount = sum(df['tweet_count'])
# avg = np.mean(df['tweet_count'])

# #print(df)
# print('totalcount= ',totalCount)
# print('avg daily count= ',avg)

# df.to_csv('countSheet.csv', index = False)  
