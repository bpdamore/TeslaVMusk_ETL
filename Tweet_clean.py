# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Import Dependencies

import pandas as pd


# %%
# Load first set of tweet data from 2010-2017 from the csv file

csv_file = "Resources/ElonTweets_2010-2017.csv"
tweet_data_2010_df = pd.read_csv(csv_file)
tweet_data_2010_df


# %%
# Split the created_at column into Date and Time columns

tweet_data_2010_df[['Date','Time']] = tweet_data_2010_df.created_at.str.split(" ",expand=True,)
tweet_data_2010_df.rename(columns={'text':'Tweet'}, inplace=True)
tweet_data_2010_df


# %%
# Narrow the dataset down to three columns: Date, Time. and Tweet. Remove the extraneous first and last characters that appears in the Tweet column

tweet_data_2010_df = tweet_data_2010_df[["Date","Time", "Tweet"]].copy()
tweet_data_2010_df['Tweet'] = tweet_data_2010_df['Tweet'].str[2:-1]
tweet_data_2010_df
tweet_data_2010_df.dtypes


# %%
# Load second set of tweet data from 2017-2020 from the json file

import json
tweet_list = []
with open("Resources/ElonTweets_2017-2020.jsonl") as json_file:
    json_list = list(json_file)
for json_str in json_list:
    result = json.loads(json_str)
    text = result
    tweet_list.append(text)


# %%
# Create a tweet_text list to isolate only the tweet text of each row
tweet_text = []
for tweet in tweet_list:
    tweet_text.append(tweet['Text'])


# %%
# Create a date_time list to isolate when each tweet was created
date_time = []
for tweet in tweet_list:
    date_time.append(tweet["CreatedAt"])


# %%
# Create a date and time list to separate the date and time for each tweet
date = []
time = []
for x in date_time:
    dt = x
    d,t = dt.split(" at ")
    date.append(d)
    time.append(t)


# %%
# Create a tweet list that breaks each tweet into an individual list item
tweet = []
for y in tweet_text:
    text = y
    tweet.append(text)


# %%
# Combine Date, Time, and Tweet Column into one table

tweet_data_2017_df = pd.DataFrame({'Date':date,'Time':time,'Tweet':tweet})
tweet_data_2017_df


# %%
# Convert Date format to YYYY-MM-DD and Time format to 24 hr so that the format matches the previous dataset

from datetime import datetime
tweet_data_2017_df['Date'] = pd.to_datetime(tweet_data_2017_df['Date']).dt.strftime('%Y-%m-%d')
tweet_data_2017_df['Time'] = pd.to_datetime(tweet_data_2017_df['Time']).dt.strftime('%H:%M:%S')
tweet_data_2017_df.dtypes


# %%
# Combine both tables into one dataset for all tweets from 2010-2020 and drop any duplicates
combined_tweets = pd.concat([tweet_data_2017_df, tweet_data_2010_df])
combined_tweets = combined_tweets.drop_duplicates()
combined_tweets


# %%
# Export to CSV
combined_tweets.to_csv('Resources/ElonTweets_Cleaned.csv')


# %%


