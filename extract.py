"""
Created on Sun Oct 04 23:10:41 2015
@author: ujjwal.karn
"""

#first, install pip by following instructions here: http://stackoverflow.com/questions/4750806/how-to-install-pip-on-windows 
#then to install tweepy, go to command prompt and type: pip install tweepy
#once tweepy is installed, run the codes below:

import tweepy    #this will give an error if tweepy is not installed properly
from tweepy import OAuthHandler
 
#provide your access details below 
access_token = '142851656-wuNbUSpI3lIPIpTzfuwUBr7obqpPqcPMZrh41ON6'
access_token_secret = '6CV5VBUuIfFpeelEUJHFASOdwxA4DGVIML5TrwcgxeFeV'

consumer_key = 'cMJWIvkDceU3S3TCCjr2PA'
consumer_secret = 'nnYYK8gjIZGDefntmVnstVnv8x2ebp5mmdSgwNHg8SA'

 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
api = tweepy.API(auth)    
    
from tweepy import Stream
from tweepy.streaming import StreamListener
 
class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:  #change location here
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())

#change the keyword here
twitter_stream.filter(track=['#bolsonaro'])

#references:
#http://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/
#http://adilmoujahid.com/posts/2014/07/twitter-analytics/
#https://github.com/tweepy/tweepy

