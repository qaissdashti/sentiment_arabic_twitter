# Creating an Arabic Sentiment Analyser

Twitter is where the Arab world goes to vent, under hidden anonymous names off course. It’s a place with millions of data points that can show how people feel in this part of the region. I thought i may try to tackle the problem and see if I can use twitter API and use the mod tweepy and TextBlob translate the Arabic words into English and then capture the sentiment from there. it worked, kinda. Disclaimer, the code i wrote is the first code that i ever wrote completely alone, so its kinda confusing and has no explanations. But it does work, and the code captures the tweets from a hashtag provided by the user then translates it to English and then from English to a sentiment polarity number. 




<b>Table of Contents:</b>
<b>Libraries Used:</b>
<b>Files Description</b>
<b> My Questions </b>
<b>My findings</b>
<b>Acknowledgments and thanks</b>






<b>Libraries Used:</b>

The project was done on Jupyter Notebook and Python 3.0, below are the libraries used:
1. Tweepy
2. TextBlob
3. NLTK

<b> Summary </b>
To create a Arabic sentiment analyser, using tweepy to connect and then using TextBlob to translate the text data coming into the API. The function created takes in from the user a name or hastag and then the API return the results. The results are returned in json format. Not all attributes of the data are taken. The attributes that reflect the sentiment are retrieved like retweet count, favourite count. Also note that TextBlob can easily translate many Arabic to English words. But when the Arabic words are localized, TextBlob cant know what the word means in English. TextBlob also has sentiment polarity for each word in English. Hence when the word is translated from Arabic to English, then we can use the sentiment polarity to assign a number from 1 to 0. One being positive, and 0.5 neutral, and 0 as negative.   

<b>My findings</b>
After creating some functions and trying out different data attributes from the tweepy. We can translate most of the Arabic worlds into English and then use TextBlob to see the sentiment polarity. We can also see these tweets came from which location geographically. An even better approach is to collect all these polarity numbers and then create a table showing each country in the Arab world and most frequent tweets or can even find the most trending hashtag, capture the tweets that are associated with it, then get the polarity, compile them in a graph. 

<b>Acknowledgments and thanks</b>
Thanks to Tweeter API team, and not thinking i am some rouge Arabic government going after its citizens.
Also thanks to the great mods of Tweepy, NLTK and TextBlob. 

