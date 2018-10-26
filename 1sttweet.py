import tweepy

from tokens import *

auth = tweepy.OAuthHandler(api_key,apisecret_key)
auth.set_access_token(access_token,asecret_token)
auth.secure = True
api = tweepy.API(auth)
tweet1 = input(" enter the tweet you what to ...")
api.update_status(status = tweet1)
