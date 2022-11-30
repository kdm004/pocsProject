

# Imports
import tweepy
import json
import csv


# Check Tweepy Version Installed
print(tweepy.__version__)


# Store bearer_token in variable
bearer_token = "Input Bearer Token Here"


client = tweepy.Client(bearer_token=bearer_token)

# Replace with your own search query
query = ' "Qatar" "Beer" place_country:US'           

# Replace with time period of your choice
start_time = '2021-11-20T00:00:00Z'

# Replace with time period of your choice
end_time = '2022-11-20T00:00:00Z'

tweets = client.search_all_tweets(query=query, tweet_fields=['context_annotations', 'created_at', 'geo'], 
                                  
                                  place_fields = ['place_type','geo'], expansions='geo.place_id',
                                  start_time=start_time,
                                  end_time=end_time, max_results=100000)



# Prepare to write to csv file
f = open('tweetData.csv','w')
writer = csv.writer(f)

# Write to csv file
for tweet in tweets.data:
    print(tweet.text)
    print(tweet.created_at)
    writer.writerow(['0', tweet.id, tweet.created_at, tweet.text])

# Close csv file
f.close()