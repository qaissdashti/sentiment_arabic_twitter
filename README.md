# Creating an Arabic Sentiment Analyser

Twitter is where the arab wolrd goes to vent, under hidden annaomous names offcourse. Its a place with millions of data points that can show how people feel in this part of the region. I thought i may try to tackle the problem and see if i can use twiiter API and use the mod tweepy and transulate the arabic wolrds into english and then capture the sentimnent from there. it worked, kinda. Discolaimere, the code i wrote is the first code that i ever wrote complety, so its kinda confusing and has no exaplinations. But it does work, and the code captures the tweets from a hastag provided by the user then transulates it to english and then from english to the sentimnet. 




<b>Table of Contents:</b>
<b>Libraries Used:</b>
<b>Files Description</b>
<b> My Questions </b>
<b>My findings</b>
<b>Acknowledgments and thanks</b>






<b>Libraries Used:</b>

The project was done on Jupyter Notebook and Python 3.0, below are the libraries used:
1. Tweepy
2.TextBlob

<b> Summary </b>
To create a arabic sentimnet analyser, using tweepy to connect and then using TextBlob to transulate the text data comming into the API. The function created take in from the user a name or hastag and then the API return the results. The results are returned in json format. Not all attriubtes of the data are taken. The attributes that reflect the sentimte are retrivied like retweet count, favorite count. Also note that TextBlob can easly transulate many arabic to english words. But when the arabic words are locilized, TextBlob cant know what the word means in english. TextBlob also has the sentimnet polirity for each word in english. Hence when the word is trasnuled from Arbic to English, then we can use the sentimenat polarity to assign a number from 1 to 0.  

<b>My findings</b>
After creating some functions and trying out different data attributes from the tweepy. We can transuklate most of the arabic worlds into english and then use TextBlob to see the sentiment polairty. We can also see these tweets came from whcih location geapgraphicly. An even better approuch is to collect all these polities and then create a table showing each counrty in the Arab wolrd and most frequest tweets or can even find the most trending hashtag, capture the tweets that are associated with it, then get the poliatry, compile them in a graph. 

<b>Acknowledgments and thanks</b>
Thanks to Tweeter API team, and not thinking i am some rouge arabic govermnet going after its citizens. 
