# A twitter bot to write mashups of cats and stats.
# Framework influenced strongly by https://github.com/molly/twitterbot_framework

import tweepy
from secrets import *
from pycorpora import animals, technology, science
import random

auth = tweepy.OAuthHandler(C_KEY, C_SECRET) 
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)  
api = tweepy.API(auth)  

explevels = ['is an expert in', 'is mediocre at', 'studies', 'regularly makes use of', 'is a power-user of',
'has an inordinate fondness for', 'flicks a tail at', 'has several degrees in', 'relaxes by thinking about',
'can lecture at length on', 'has an avocation doing', 'could write a book on',
'teaches at the university about', 'purrs when thinking of', 'misuses']

def catction():
    return "{0} the {1} {2} {3}.".format(
        re.sub("\d+ ","", random.choice(science.minor_planets["minor_planets"])),
        random.choice(animals.cats["cats"]),
        random.choice(explevels),
        random.choice(technology.computer_sciences['computer_sciences']))

mytweet = catction()
print(mytweet)

api.update_status(mytweet)