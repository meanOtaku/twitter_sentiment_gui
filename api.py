import tweepy
import json
 
consumerKey = "WL9qLoAs3iITSoA0Ywk0P3HlS" 
consumerSecret = "rzZMPzjsLqFu92IVOJjjIJBeEEgNE9XyrC1ynp9jN2RsiV3fDa" 
accessToken = "1120882257118420992-moWBx8bFzxYKU83Z6Ozkwpub9Y2Km9" 
accessTokenSecret = "TY4qwgQ8MDNpfqDYGh4fTwNYOaSf31HbWtDp9Datp2iLP" 
 
auth = tweepy.OAuthHandler(consumerKey, consumerSecret) 
auth.set_access_token(accessToken, accessTokenSecret) 
api = tweepy.API(auth) 
places = api.geo_search(query="india", granularity="country")
place_id = places[0].id
 
india_trends = api.trends_place(2282863)

#print(json.dumps(india_trends, indent=4))
india_trends_set = set([trend['name'] 
                        for trend in india_trends[0]['trends']])

india_trends_list = list(india_trends_set)                       
#print(india_trends_list[0])
q = india_trends_list[0]
date_since = "2020-12-7"
tweets = tweepy.Cursor(api.search,
              q=q,
              lang="en",
              since=date_since).items(5)
for tweet in tweets:
    print(type(tweet))