from twython import Twython, TwythonError
import time
import random

app_key = "y23k0F11acTDQdp9EV36yR9NO"
app_secret = "FFrbkbn3ebgSxO7BV5RRHD9cP81fptG3bFfBhdGv5HGepCj0rl"
oauth_token = "804448300153774080-m2S40C1nXBr2quzujuk8KvCWTvI6wr1"
oauth_token_secret = "TfUUKIgloCJIpUCupfHXIjahkBEI8A698zXwJuCfD196B"

twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)

list = [
    "Hello, I'm a Tweet.",
    "And I'm another!",
    "Yoohoo! I'm here too!",
    "We're all here together!",
    "Isn't Twitter so much fun =D",
    "(I think you get the idea by this point...)"
    ]

while True:
    try:
        if len(list) > 0:
            toTweet = list[random.randint(0,len(list))-1]
            twitter.update_status(status=toTweet)
            list.remove(toTweet)
            time.sleep(60)
        else:
            twitter.update_status(status="Oh dear... I'm afraid I'm rather empty =(")
            break
    except TwythonError as e:
        print e
