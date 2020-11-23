import re
import tensorflow as tf
from tensorflow import keras
import numpy as np
import functools
import os
import io

from twitter_scraper import get_tweets
from requests_html import HTML, HTMLSession
from langdetect import detect


def clean_tweet(tweet): 
        return ''.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|(\[\])", " ", tweet))


def review_encode(s):
    encoded = [1]
    for word in s:
        if word.lower() in word_index:
            encoded.append(word_index[word.lower()])
        else:
            encoded.append(2)
    return encoded





word_index = tf.keras.datasets.imdb.get_word_index()


word_index = {k:(v+3) for k,v in word_index.items()}
word_index["<PAD>"] = 0
word_index["<START>"] = 1
word_index["<UNK>"] = 2
word_index["<UNUSED>"] = 3
#reverse_word_index = dict([(value,key) for (key,value) in word_index.items()])




session = HTMLSession()


def get_trends():
    trends = []

    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8",
        "X-Twitter-Active-User": "yes",
        "X-Requested-With": "XMLHttpRequest",
        "Accept-Language": "en-US",
    }

    html = session.get("https://twitter.com/i/trends", headers=headers)
    html = html.json()["module_html"]

    html = HTML(html=html, url="bunk", default_encoding="utf-8")

    for trend_item in html.find("li"):
        trend_text = trend_item.attrs["data-trend-name"]

        trends.append(trend_text)

    return trends


var = get_trends()
print(var)
filetag = io.open('test_tag.txt', "w", encoding="utf-8")
for i in var:
    tag = i 
    filetag.write(tag)
filetag.close()


file1 = io.open('test1.txt', "w", encoding="utf-8")
for tweet in get_tweets(var[0], pages=1): 
    text = tweet['text']
    text = clean_tweet(text)
    if detect(tweet['text']) == 'en':
        print('english',end='\n')
        file1.write(text)
        #print(tweet)
    else :
        print("other",end='\n')
    
file1.close()


#FILE OPENS

os.system('cmd /c "test_tag.txt"')
os.system('cmd /c "test1.txt"')



#SCANNING FILE



model = keras.models.load_model("model_final.h5")
mean = 0
total = 0
for tweet in get_tweets(var[0], pages=1):
    text = tweet['text']
    mline = clean_tweet(text)
    nline = mline.replace("," , "").replace("." , "").replace(")" , "").replace("(" , "").replace(";" , "").replace(":" , "").replace("\"" , " ").strip().split(" ")
    encode = review_encode(nline)
    encode = keras.preprocessing.sequence.pad_sequences([encode],value=word_index["<PAD>"],padding="post",maxlen=250)
   
    predict = model.predict(encode)
    #print(line)
    #print(mline)
    #print(encode)
    print(predict[0])
    mean = ( mean + predict[0])
    total = total + 1

mean_final = mean / total 

if mean_final * 100 >= 50 :
    print("POSITIVE")
    print(mean_final)
else :
    print("Negative")
    print(mean_final)