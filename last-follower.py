import tweepy
from time import time, sleep

consumer_key = "your consumer key" 
consumer_secret = "your consumer secret"
access_token = "your api access token"
access_secret = "your api access secret"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

print(auth.get_authorization_url())
verifier = input('Verifier:')
token = auth.get_access_token(verifier = verifier)
mycreds = {
    'consumer_key': consumer_key,
    'consumer_secret': consumer_secret,
    'access_token': token[0],
    'access_token_secret': token[1]
}

t_auth = tweepy.OAuthHandler(
    consumer_key = mycreds['consumer_key'],
    consumer_secret = mycreds['consumer_secret'])
t_auth.set_access_token(
    mycreds['access_token'],
    mycreds['access_token_secret'])

the_api = tweepy.API(t_auth)

last_follower = the_api.followers()[0].screen_name

while True:
    sleep(60*2)

    me_obj = the_api.me()
    new_status = "Full Stack developer @Inspire_Forth · Maintaining @bgpartemis · Blogging @DigitaLifeBlog · Cybersecurity and web dev. Last follower: @" + last_follower
    last_follower = the_api.followers()[0].screen_name
    the_api.update_profile(description=new_status)
