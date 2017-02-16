
//no working

//see this for reference http://stackoverflow.com/questions/27094275/how-to-post-image-to-twitter-with-twython
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

    def RandomImageTwitt(folder):
        #Takes the folder where your images are as the input
        images = glob.glob(folder + "*")
        image_open = open(images[random.randint(0,len(images))-1])
        #new code starts here 
        image_ids = twitter.upload_media(media=image_open)
        twitter.update_status('hello this is a status',image_ids['media_id'])


RandomImageTwitt("/home/XXX/.reddit-twitter-image/XXX/")
