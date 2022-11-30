

# Imports
import tweepy
import json
import csv
import time
from itertools import chain
import pandas as pd

#--------------------------------------------------------------------------------------------------------------------------------------------------
bearer_token = "AAAAAAAAAAAAAAAAAAAAAHIxjgEAAAAAHBtpIV5008WAMdj3Hd2dapo%2BM6k%3DGfV9iH7qSwlBf8UQcODVI6DW0FaoIT6tfodr38XcVR018cGh6v"
client = tweepy.Client(bearer_token=bearer_token)
#--------------------------------------------------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------------------------------------------------------
query = '"is a shithole country" OR "is a shit hole country" place_country:US'        # ' "is a shithole country" OR "is a shit hole country" place_country:US' 
granularity = 'day'
#next_token = None

start_time = '2021-11-01T00:00:00Z' # CHECK THE YEAR
end_time = '2022-11-20T00:00:00Z' # CHECK THE YEAR

counts = tweepy.Paginator(
        client.get_all_tweets_count,
        query=query, 
        start_time=start_time,
        end_time=end_time,
        granularity='day') 
time.sleep(1)
#--------------------------------------------------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------------------------------------------------------
# f = open('countSheet.csv','w')
# writer = csv.writer(f)

# for count in counts:
#     print(count)
#     #writer.writerow([count])
# f.close()
#-------------------------delete after this--------------------------------------------------------------------------------------------------------
tweet_count = []
    
for count in counts:
        tweet_count.append(count.data) # A single count corresponds to a single day. /// We put the start, end, and tweet_count for each day into a list /// We each element of that data into a dataframe

data = list(chain.from_iterable(tweet_count))
df = pd.DataFrame(data).reindex(['start', 'end', 'tweet_count'], axis=1)
print(df)