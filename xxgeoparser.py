

from geotext import GeoText

# places = GeoText("London is a great city, and I love french", aggressive = True) # how do I use aggressive parse?
# print(places.cities)
# print(places.country_mentions)
# # "London"


# GeoText('New York, Texas, and also China').country_mentions
# # OrderedDict([(u'US', 2), (u'CN', 1)])

# tweets_with_mentions = []
# tweet_list=['my friend is from a middle eastern country', 'hello my European friend', 'Hey, meet my friend from Laos', 'hello my South Asian friend!', 'I am from Vermont']


# for tweet in tweet_list:                                                # for each tweet
#     places = GeoText(tweet, aggressive = True).country_mentions         # get the regions mentioned
#     places_list = list(places.keys())                                   # make a list of the regions mentioned
#     print(places_list)                                                  # 
#     if 'Europe' or 'Latin America' or 'North America' or 'Indian Subcontinent' or 'Sub-Saharan Africa' or 'MENA' or 'East Asia' or 'Central Asia' or 'Pacific' in places_list:
#         tweets_with_mentions.append(tweet)
# print(tweets_with_mentions)

tweets_with_mentions = []
tweet_list = ['hello', 'I am iranian', 'Are you from China? or South Africa?', 'Whose dog is that?', 'are you European?', 'I am from Vermont', 'I do not like college football', 'I love lamp']
for tweet in tweet_list:
    places = GeoText(tweet, aggressive = True).country_mentions         # get the regions mentioned
    
    region_list = list(places.keys())
 #   print(region_list)
    for entry in region_list:
        if 'Europe' in entry:
            tweets_with_mentions.append(tweet)
        if 'Latin America' in entry:
            tweets_with_mentions.append(tweet)
        if 'North America' in entry:
            tweets_with_mentions.append(tweet)
        if 'Indian Subcontinent' in entry:
            tweets_with_mentions.append(tweet)
        if 'Sub-Saharan Africa' in entry:
            tweets_with_mentions.append(tweet)
        if 'MENA' in entry:
            tweets_with_mentions.append(tweet)
        if 'East Asia' in entry:
            tweets_with_mentions.append(tweet)
        if 'Central Asia' in entry:
            tweets_with_mentions.append(tweet)
        if 'Pacific' in entry:
            tweets_with_mentions.append(tweet)
print(tweets_with_mentions)



# my_list=['MENA', 'East Asia', 'Europe', 'US']
# for entry in my_list:
#     if 'Europe' in entry:
#         print(entry)
#     if 'Latin America' in entry:
#         print(entry)
#     if 'North America' in entry:
#         print(entry)
#     if 'Indian Subcontinent' in entry:
#         print(entry)
#     if 'Sub-Saharan Africa' in entry:
#         print(entry)
#     if 'MENA' in entry:
#         print(entry)
#     if 'East Asia' in entry:
#         print(entry)
#     if 'Central Asia' in entry:
#         print(entry)
#     if 'Pacific' in entry:
#         print(entry)



# It's not perfect, but this is what we're going to use to filter tweets by country and region.
# We're going to need to find out how to add "region" into it. Maybe we'll do that if we have time.
# We're going to need to find out how to change the output from <country_abbrev> to <country_region>

