

from geotext import GeoText

# places = GeoText("London is a great city, and I love french", aggressive = True) # how do I use aggressive parse?
# print(places.cities)
# print(places.country_mentions)
# # "London"


# GeoText('New York, Texas, and also China').country_mentions
# # OrderedDict([(u'US', 2), (u'CN', 1)])

sentences_with_MENA = []
tweet_list=['my friend is from a middle eastern country', 'hello my European friend', 'Hey, meet my friend from Laos']
for tweet in tweet_list:
    places = GeoText(tweet, aggressive = True).country_mentions
    places_list = list(places.keys())
 #   print(places_list)
    if 'MENA' in places_list:
        sentences_with_MENA.append(tweet)
print(sentences_with_MENA)

# It's not perfect, but this is what we're going to use to filter tweets by country and region.
# We're going to need to find out how to add "region" into it. Maybe we'll do that if we have time.
# We're going to need to find out how to change the output from <country_abbrev> to <country_region>
