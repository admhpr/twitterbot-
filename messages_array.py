from twython import Twython

from auth import (


    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
    
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

import random

messages = [
    "Hello",
    "Hi there",
    "What's up?",
    "How's it going?",
    "Have you been here before?",
    "Get a hair cut!",
]

message = "Hello world - here's a picture!"
with open('/home/pi/Downloads/img1.jpg', 'rb') as photo:
    twitter.update_status_with_media(status=message, media=photo)
