# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 15:13:22 2019

@author: GIGABYTE
"""

"""first install conda tweepy



"""


tweets = tweepy.Cursor(api.search, q='#بنك_الخليج', lang='ar').items(140)
data = [s.text.encode('utf8') for s in tweets]
type(data)
data[0]
data[5]
data[2]
data
tweets = tweepy.Cursor(api.search, q='بنك_الخليج', lang='ar').items(140)
data = [s.text.encode('utf8') for s in tweets]
import pandas as pf
import pandas as pd
import numpy as np
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.DataFrame(data=[s.text.encode('utf8') for s in tweets])
data = [s.text.encode('utf8') for s in tweets]
tweets = tweepy.Cursor(api.search, q='بنك_الخليج', lang='ar').items(140)
df = pd.DataFrame(data = [s.text.encode('utf8') for s in tweets], columns=['Tweets'])
df
df = pd.DataFrame(data = [s.text for s in tweets], columns=['Tweets'])
df
tweets = tweepy.Cursor(api.search, q='بنك_الخليج', lang='ar').items(140)
dfnoencode = pd.DataFrame(data = [s.text for s in tweets], columns=['Tweets'])
dfnoencode
dfnoencode.head()
dfnoencode.head(1)
print(dir(tweets[0]))
tweets = tweepy.Cursor(api.search, q='بنك_الخليج', lang='ar').items(140)
data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
data
print(dir(tweets[0]))
tweet
tweets
tweets[0]
tweets[5]
tweets.id
data['Likes']  = np.array([tweet.favorite_count for tweet in tweets])
data['RTs']    = np.array([tweet.retweet_count for tweet in tweets])
tweets_test = tweepy.Cursor(api.search, q='بنك_الخليج', lang='ar')
data_test = [tweet.text for tweet in tweets_test]
api.search('Dogs')
public =  api.search('بنك_الخليج')
for tweet in public:
    print(tweet.text)
    
tweet.text
tweet.text[0]
tweet.text[0][0]
tweet.text[10]
tweet.text
data_newe = pd.DataFrame(data=[tweet.text for tweet in public], columns=['Tweets'])
data_newe
dir(public[0])
print(public[0].id)
print(public[0].geo)
print(public[0].retweets_count)
print(public[0].retweet_count)
print(public[5].retweet_count)
print(public[5].entities)
public[5]
public.text[5]
print(public[5].entities)
data_newe['likes'] = np.array([tweet.retweet_count for tweet in public])
data_newe.head(10)
print(data_newe)
data_newe['RT'] = np.array([tweet.retweet_count for tweet in public])
data_newe['likes'] = np.array([tweet.favorite_count for tweet in public])
data_newe.tail()
data_newe.Likes
data_newe['Likes']
data_newe.columns
data_newe.likes
data_newe.RT
from textblob import TextBlob
data_newe[0]
data_newe.head(1)
tweet
tweet.text
example = TextBlob(tweet.text)
example
example.translate
example.translate(to='en')
list_tweets = [tweet.text for tweet in public]
list_tweets[0]
for e in list_tweets:
    example = TextBlob(e)
    trans = example.translate(to='en')
    print(trans)


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


trans_list = []
for e in safa_data[0]:
    example = TextBlob(e)
    trans = example.translate(to='en')
    trans_list.append(trans)


new_search = search_words + " -filter:retweets"
tweets = tweepy.Cursor(api.search, q=new_search).items(2)
for i in tweets:
    print(i)
    
for i in tweets:
    print(i.text)    
    
tweets= tweepy.Cursor(api.search, q=new_search).items(10)
[tweet.text for tweet in tweets ]
search_name('صفاء الهاشم#')
def new_filtered_search(hastag):
    list_tweets = []
    search = api.search(q + " -filter:retweets")
    for tweet in search:
        tweet_iter = tweet.text
        list_tweets.append(tweet_iter)
    return list_tweets


new_filtered_search("صفاء الهاشم")

def new_filtered_search(hastag):
    list_tweets = []
    search = api.search(hashtag + " -filter:retweets")
    for tweet in search:
        tweet_iter = tweet.text
        list_tweets.append(tweet_iter)
    return list_tweets


new_filtered_search("صفاء الهاشم")
def new_filtered_search(hashtag):
    list_tweets = []
    search = api.search(hashtag + " -filter:retweets")
    for tweet in search:
        tweet_iter = tweet.text
        list_tweets.append(tweet_iter)
    return list_tweets


new_filtered_search('صفاء الهاشم')
test_lists = new_filtered_search('صفاء الهاشم')
gulf_bank_lists = new_filtered_search('بنك الخليج')
sadoun = new_filtered_search('سعدون العتيبي')
sadoun2 = new_filtered_search('سعدون العتيبي')
loans = new_filtered_search('اسقاط_القروض_لليوم_272')
loans2 = new_filtered_search('اسقاط_القروض_لليوم_272')
def new_filtered_search(hashtag):
    list_tweets = []
    id_tweet = []
    search = api.search(hashtag + " -filter:retweets")
    for tweet in search:
        tweet_iter = tweet.text
        tweet_id = tweet.id
        list_tweets.append(tweet_iter)
        id_tweet.append(tweet_id)
    return list_tweets


new_filtered_search('اسقاط_القروض_لليوم_272')
test_wid = new_filtered_search('اسقاط_القروض_لليوم_272')
def new_filtered_search(hashtag):
    list_tweets = []
    id_tweet = []
    search = api.search(hashtag + " -filter:retweets")
    for tweet in search:
        tweet_iter = tweet.text
        tweet_id = tweet.id
        list_tweets.append(tweet_iter)
        id_tweet.append(tweet_id)
    return list_tweets, id_tweet


test_wid = new_filtered_search('اسقاط_القروض_لليوم_272')
import nltk
sadoun
for i in sadoun:
    print(i[0])
    
for i in sadoun:
    print(i[2])
    
for i in sadoun:
    print(i)
    
for i  in sadoun:
    print(i[0:2])
    
len(sadoun2)
sadoun[0]
tok = nltk.word_tokenize(sadoun[0])
tok2 = nltk.word_tokenize(sadoun[1])
tok2 = nltk.word_tokenize(sadoun[3])
tok2
from collections import Counter
word_count = Counter(tok2)
word_count.most_common()
two_strings = sadoun[0] + sadoun[1]
Counter(two_strings)
word_count = Counter(two_strings)
word_count.most_common()
two_strings
tok_new = nltk.tokenize(two_strings)
tok_new = nltk.word_tokenize(two_strings)
tok_new
word_count = Counter(tok_new)
word_count.most_common()
two_strings
two_strings = sadoun[0] + sadoun[2]
two_strings
tok_new = nltk.word_tokenize(two_strings)
tok_new
word_count = Counter(tok_new)
word_count.most_common()
corpus = []
range(sadoun)
for i in len(range(sadoun)):
    text = sadoun[i]
    corpus.append(text)
    
for i in len(range(sadoun)):
    text = str(sadoun[i])
    corpus.append(text)
    
for i in len(range(sadoun)):
    print(i)
    
for i in range(len(sadoun)):
    print(i)
    
for i in range(len(sadoun)):
    text = sadoun[i]
    corpus.append(text)
    
string = "".join(["".join(s)for s in sadoun])
test = nltk.word_tokenize(string)
tested = Counter(test)
tested.most_common()
test_tuple = tested.most_common()
def concat_tweets(tweet_list):
    string = "".join(["".join(s)for s in tweet_item])
    return string


concat_tweets(gulf_bank_lists)
string = "".join(["".join(s)for s in gulf_bank_lists])
string
def tokenize(concated_string):
    after_concat = nltk.word_tokenize(concated_string)
    counted = Counter(after_concat)
    counted_tuple = counted.most_common()
    return counted_tuple
tokenize(string)
string = ["".join(s)for s in gulf_bank_lists]
string
string[0:10]

string[0:1]
tokenize(string)
type(string)
string = "".join(["".join(s)for s in gulf_bank_lists])

type(string)
