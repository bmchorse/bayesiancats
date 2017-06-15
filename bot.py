# A twitter bot to write mashups of cats and stats.
# Framework influenced strongly by https://github.com/molly/twitterbot_framework

import tweepy
from secrets import *

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)  
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)  
api = tweepy.API(auth)  