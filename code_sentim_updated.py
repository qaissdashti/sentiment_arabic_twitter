# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 16:23:15 2019

@author: GIGABYTE
"""
import tweepy as tw
import re
import nltk
from collections import Counter
import pandas as pd
import numpy as np
from IPython.display import display
import matplotlib.pyplot as plt
#from textblob import TextBlob
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
#import arabic_reshaper
#from bidi.algorithm import get_display


def search_name(input):
    list_tweets = []
    search = api.search(input)
    for tweet in search:
        tweet_iter = tweet.text
        list_tweets.append(tweet_iter)
    return list_tweets
  

def trans_english(input_here):
    english_tweets = []
    for e in input_here:
        example = TextBlob(e)
        trans = example.translate(to='en')
        english_tweets.append(trans)
    return english_tweets

def analyse_tweets(input_here):
    sentiment = []
    for analysis in input_here:
        print(analysis.sentiment)
        sentiment.append(analysis.sentiment)
    return sentiment

def return_polarity(input_here):
    for sent in input_here:
        if sent[0] > 0.5:
            print('very positive')
        elif sent[0] < 0.5:
            print('positive')
        else:
            print('neutral')
    
def tweet_item(input_here):
    public =  api.search(input_here)
    for tweet in public:
        data_newe = pd.DataFrame(data=[tweet.text for tweet in public], columns=['Tweets'])
    return data_newe 


def new_filtered_search(hashtag):
    #returns a list of tweets showing the text only
    #the param: is the name of the place to search is "gulf bank"
    list_tweets = []
    search = api.search(hashtag + " -filter:retweets")
    for tweet in search:
        tweet_iter = tweet.text
        list_tweets.append(tweet_iter)
    return list_tweets


def concat_tweets(tweet_list):
    #function takes in a list of tweets and joins all the char in one large
    #string then removes the https
    string = "".join(["".join(s)for s in tweet_list])
    text = re.sub(r'http\S+', '', string)
    return text


def tokenize(concated_string):
    #takes in concated string and returns tuple withe word count
    after_concat = nltk.word_tokenize(concated_string)
    counted = Counter(after_concat)
    counted_tuple = counted.most_common()
    return counted_tuple

def create_df(hashtag):
    #will return text. loc, #of retweets, #of followes in DF
    tweets= api.search(hashtag + " -filter:retweets")
    df_list = [[tweet.text, tweet.user.location, tweet.retweet_count,
                tweet.user.followers_count, tweet.favorite_count, tweet.user.name]for tweet in tweets]
    df_tweets = pd.DataFrame(df_list, columns=['text', 'location', 'retweet',
                                               'followers count','favorite_count',
                                               'name'])
    return df_tweets
    
"""
fig, ax = plt.subplots(figsize=(10,10))
kfas_df_tuple.sort_values(by='text').plot.barh(x='text', y='num' ,ax=ax)
plt.show()
"""

def remove_url(text):
    """remove url in text with nothing"""
    
    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())


search_term = "صفاء الهاشم -filter:retweets"
def choose_number_tweets(search_term):
    tweets = tw.Cursor(api.search,
                   q=search_term,
                   lang="ar",
                   since='2019-04-01').items(50)
    return tweets.text

all_tweets = [tweet.text for tweet in tweets]

all_tweets[:5]

#try to retreive that hastags that are in the bulk of the tweets



def pull_tweet(tweeters):
    new_dict = {}
    for tweet in tweeters:
        new_dict[tweet.id] = tweet.text
    return new_dict

def count_dict(listname):
    new_dict = {}
    for i in listname:
        if i in new_dict:
            new_dict[i] += 1
        else:
            new_dict[i] = 1
    return new_dict
    

def prop(add_dict, total):
    c_ratings_pro = {}
    
    for key in add_dict:
        percentage = add_dict[key] / total
        c_ratings_pro[key] = percentage
    return c_ratings_pro

        
    
