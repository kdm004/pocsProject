from fuzzyWuzzy import fuzz

# def get_ratio(word):
#     ratio = fuzz.token_set_ratio(word, 'kevin')
#     return ratio


# # Works.
# word_list = ['hello', 'my', 'name', 'is', 'kevin']
# for word in word_list:
#     #if word == 'kevin':
#     ratio = get_ratio(word)
#     if ratio >= 90:
#         print(word)

# Works.

# Convert the lists to dataframes, and see if that works.








# word_list = ['hello', 'my', 'name', 'is', 'kevin']     # apply this logic to tweetDownloader.py
# name_list = ['dave', 'james', 'kevin', 'martha']


# for i in range(len(word_list)):
#     for j in range(len(name_list)):
#     #if word == 'kevin':
#         ratio = fuzz.token_set_ratio(word_list[i], name_list[j])      # need to store fuzz comparison in a variable. 
#         if ratio >= 90:
#             print(word_list[i])

#--------------------------------
import pandas as pd
from nltk.tokenize import word_tokenize

column2_list = ['Justin Reid has been non-existent today No showed after talking Send him back to Ukraine where he clearly belongs', '❌Refer to Native Americans as “ immigrants ” ‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️ https //t.co/VzYgzn4JDi', 'RepJeffries Yeah think 🤔 about who got the jobs 5 millions illegal immigrants DM me if agree', 'RepJeffries Division is way up the stock market is way down people are losing lots of money the Ukraine is getting more corrupt our country is being invaded by illegal immigrants']
sentence_list = ['Justin Reid has been non-existent today No showed after talking Send him back to Ukraine where he clearly belongs', '❌Refer to Native Americans as “ immigrants ” ‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️ https //t.co/VzYgzn4JDi', 'RepJeffries Yeah think 🤔 about who got the jobs 5 millions illegal immigrants DM me if agree', 'RepJeffries Division is way up the stock market is way down people are losing lots of money the Ukraine is getting more corrupt our country is being invaded by illegal immigrants']
sentence_dic = {'sentence':sentence_list, 'column2':column2_list} 
df_sentences = pd.DataFrame(sentence_dic, columns = ['sentence', 'column2'])

name_list = ['dave', 'james', 'Ukraine', 'john']
name_dic = {'name':name_list} 
df_names = pd.DataFrame(name_dic, columns = ['name'])

df_empty = pd.DataFrame(columns=['word'])



#for sentence in df_sentences['sentence']:    # for each sentence



for sentenceIndex in range(len(df_sentences['sentence'])):
    word_tokens = word_tokenize(df_sentences['sentence'][sentenceIndex])    # tokenize the sentence
    for token in word_tokens:        # for each token
        for name in df_names['name']:  # for each name
        #if word == 'kevin':
            ratio = fuzz.token_set_ratio(token, name)      # compare ratio of token to name
            if ratio >= 90:                                                        # add sentence to list if it contains a name within the name dataframe (Only kevin)
                df_empty = df_empty.append(df_sentences.iloc[[sentenceIndex]])



print(df_empty)

           # print(df_words['word'][i])
#--------------------------------


# #for tweetIndex, row in df_tweets.iterrows():
# for tweetIndex in range(len(df_tweets['text'])):
#     word_tokens = word_tokenize(df_tweets['text'][tweetIndex])      # tokenize tweet
#     #for token in word_tokens:               # for each token
#     for i in range(len(word_tokens)):
#         for globeIndex in range(len(globe_df['Country'])):
#             fuzzRatio = fuzz.token_set_ratio(word_tokens[i], globe_df['Country'][globeIndex])
#             if fuzzRatio >= .90:
#                 df_tweetsWithNames = df_tweetsWithNames.append(df_tweets.iloc[[tweetIndex]])







# # Doesn't work.
# word_list = ['hello', 'my', 'name', 'is', 'kevin']
# for word in word_list:
#     #if word == 'kevin':
#     if fuzz.token_set_ratio(word, 'kevin') >= .90:
#         print(word)






