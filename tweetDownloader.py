

# Imports
import tweepy
import json
import csv


# Check Tweepy Version Installed
#print(tweepy.__version__)


# Store bearer_token in variable
bearer_token = "AAAAAAAAAAAAAAAAAAAAAHIxjgEAAAAAHBtpIV5008WAMdj3Hd2dapo%2BM6k%3DGfV9iH7qSwlBf8UQcODVI6DW0FaoIT6tfodr38XcVR018cGh6v"


client = tweepy.Client(bearer_token=bearer_token)

# Replace with your own search query
query = '#banimmigrants place_country:US'           # Triple quotes around a quoted phrase will return the exact phrase. ['word1', 'word2'] gives Tweet with both words. 
                                                                                        # query = ' "is a shithole country" OR "is a shit hole country" place_country:US'   
# Replace with time period of your choice
start_time = '2022-11-01T00:00:00Z' # CHECK THE YEAR

# Replace with time period of your choice
end_time = '2022-11-20T00:00:00Z' # CHECK THE YEAR

tweets = client.search_all_tweets(query=query, tweet_fields=['context_annotations', 'created_at', 'geo'], # Do I need context_annotations?
                                  
                                  place_fields = ['place_type','geo'], expansions='geo.place_id',
                                  start_time=start_time,
                                  end_time=end_time, max_results=100)



# tweets = client.search_all_tweets(query=query, tweet_fields=['context_annotations', 'created_at', 'geo'],
#                                   place_fields=['place_type', 'geo'], expansions='geo.place_id', max_results=10)


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



#-------------------------------------------------------------------------------------------------------------------------------








