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
#from fuzzywuzzy import fuzz    No longer used. Geotext replaces this. 
from geotext import GeoText


eval_df = pd.read_csv('finalData.csv')
uneval_df = pd.read_csv('finalData_cleaned.csv')
df_newRow = pd.DataFrame(columns=['sentiment', 'id', 'date', 'text'])

# for i in range(len(eval_df)):
#     for j in range(len(eval_df)):
#         if uneval_df['id'][i] == eval_df['id'][j]: # maybe change to  eval_df['id'][j]
           

for i in range(len(eval_df)):
    for j in range(len(uneval_df)):
        if uneval_df['id'][i] == eval_df['id'][j]:
            uneval_df['sentiment'][i] = eval_df['sentiment'][i]
        
            # add this row to the initialized dataframe
            df_newRow.append(uneval_df.iloc[[i]])
        
            # delete row i from uneval_df
            uneval_df = uneval_df.drop(i)

            # concatenate old dataframe with this uneval_df
            uneval_df = pd.concat([df_newRow,df_newRow.loc[:]]).reset_index(drop=True)


            # delete the old row from the initialized dataframe
            df_newRow = df_newRow.drop(0)
        

uneval_df.to_csv('ZZZZZ.csv')
print(eval_df)
print(uneval_df)

#tweets_df.to_csv('finalData_cleaned.csv', index = False)  

# uneval_df = uneval_df.set_index('id')
# uneval_df = uneval_df.reindex(index=eval_df['id'])
# uneval_df = uneval_df.reset_index()




