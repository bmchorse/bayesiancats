# A twitter bot to write mashups of cats and stats.
# Framework influenced strongly by https://github.com/molly/twitterbot_framework

import tweepy
import time
from secrets import *
from pycorpora import animals, technology, science
import random

auth = tweepy.OAuthHandler(C_KEY, C_SECRET) 
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)  
api = tweepy.API(auth)  

cats = animals.cats['cats']

# Remove some of the less recognizable cat breeds
dropcats = ['Aegean', 'Asian', 'Australian Mist', 'Bambino', 
'Bombay', 'Burmilla', 'California Spangled', 'Chantilly-Tiffany', 
'Chartreux', 'Chausie', 'Cheetoh', 'Cymric', 'Cyprus', 'Donskoy',
'Dragon Li', 'Foldex', 'Havana Brown', 'Highlander', 'Khao Manee',
'Korat', 'Korn Ja', 'LaPerm', 'Minskin', 'Munchkin', 'Ojos Azules', 
'Oregon Rex', 'PerFold', 'Persian (Modern)', 'Persian (Traditional)',
'Peterbald', 'Raas', 'Ragamuffin', 'Sam Sawet', 'Serengeti', 
'Serrade Petit', 'Singapura', 'Sokoke', 'Suphalak', 'Thai', 'Thai Lilac',
'Toyger', 'Ukrainian Levkoy']

# Add in some additional fun
addcats = ['tiger', 'lion', 'ocelot', 'cheetah', 'leopard', 
'panther', 'jaguar', 'snow leopard', 'cave lion', 'serval', 'caracal', 
'lynx', 'bobcat', 'kitten', 'fishing cat', 'sand cat', 'ThunderCat']

trimmedcats = [c for c in cats if c not in dropcats]
fullcats = trimmedcats + addcats

explevels = ['is an expert in', 'is mediocre at', 'studies', 'regularly makes use of', 'is a power-user of',
'has an inordinate fondness for', 'flicks a tail at', 'has several degrees in', 'relaxes by thinking about',
'can lecture at length on', 'could write a book on',
'teaches at the university about', 'purrs when thinking of', 'misuses']

topics = technology.computer_sciences['computer_sciences']

# Thin the technology list a little
droptopics = ['AIM', 'Algol', 'Amazon', 'AppStream', 'ASPnet', 'Aviato',
'Backbone', 'Bootstrap', 'Bower', 'Browserify', 'Bundler', 'Capistrano',
'ClearDB', 'CloudFormation', 'CloudFront', 'CloudSearch', 'CloudTrail',
'CloudWatch', 'COBOL', 'Cognito', 'CrunchBang', 'Cucumber', 'Dart', 'Diaspora', 
'Discourse', 'EBS', 'EC2', 'EJS', 'ElasticBeanstalk', 'ElasticSearch', 'ERB',
'Express', 'Fedora', 'Foundation', 'Ghost', 'Glacier', 'Grunt', 'HacketyHack',
'ICQ', 'ImageMagick', 'IRB', 'IronCache', 'Jasmine', 'Jekyll', 'KeenIO', 
'Kickstarter', 'Knockout', 'LeapMotion', 'Lyft', 'Middleman', 'Mocha', 'NewRelic',
'Nginx', 'NLTK', 'Nokogiri', 'NPM', 'Objective-C', 'OCR', 'Octopress', 'Pandora',
'Passenger', 'PGP', 'PIP', 'Polymer', 'Processing', 'PubNub', 'Redis',
'Refinery', 'Route53', 'Rspec', 'Sendgrid', 'SES', 'Silverlight', 'Sinatra',
'SNS', 'Solr', 'SpoonRocket', 'SWF', 'TCP', 'Uber', 'Ubuweb', 'Unicorn',
'Webaudio', 'Webrick', 'Websockets', 'XTags', 'Yahoo', 'Yelp', 'Zepto']

trimmedtopics = [t for t in topics if t not in droptopics]

# Add some statistics
statsterms = ['Bayesian analyis', 'stochastic gradient descent', 'linear regression', 
'least-squares regression', 'uninformative priors', 'Monte Carlo methods', 'Markov Chain Monte Carlo',
'rejection sampling', 'Theano', 'scikit-learn', 'simulated annealing', 'Metropolis-Hastings', 
'hierarchical modeling', 'Gibbs sampling', 'model comparison', 'expectation maximization',
'Bayesian stats', 'Bayesian inference', 'Gaussian mixture models']

fulltopics = trimmedtopics + statsterms

def catction():
    return "{0} the {1} {2} {3}.".format(
        re.sub("\d+ ","", random.choice(science.minor_planets["minor_planets"])),
        random.choice(fullcats),
        random.choice(explevels),
        random.choice(fulltopics))

while True:
    mytweet = catction()
    api.update_status(mytweet)
    time.sleep(1800)
