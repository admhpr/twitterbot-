
from twython import Twython, TwythonError
 
from auth import (


    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
    
)
 
naughty_words = ["NFL", "angry", "sad", "kardashian", "likeforlike","instalike"]
good_words = ["#servantleader", "#positivequote", "#positivity", "#PositiveVibes", "#happiness","#motivation","#SpreadLove"] 
filter = " OR ".join(good_words)
blacklist = " -".join(naughty_words)
keywords = filter + blacklist
 
twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)
 
search_results = twitter.search(q=keywords, count=10)
try:
    for tweet in search_results["statuses"]:
        try:
            twitter.retweet(id = tweet["id_str"])
        except TwythonError as e:
            print e
except TwythonError as e:
    print e


