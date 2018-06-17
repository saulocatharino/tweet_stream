
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import oauth2 as oauth
import urllib2 as urllib
import json

access_token_key = '142851656-wuNbUSpI3lIPIpTzfuwUBr7obqpPqcPMZrh41ON6'
access_token_secret = '6CV5VBUuIfFpeelEUJHFASOdwxA4DGVIML5TrwcgxeFeV'

consumer_key = 'cMJWIvkDceU3S3TCCjr2PA'
consumer_secret = 'nnYYK8gjIZGDefntmVnstVnv8x2ebp5mmdSgwNHg8SA'

_debug = 0

oauth_token = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"

http_handler = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url,
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

def fetchsamples():
  url = "https://api.twitter.com/1.1/search/tweets.json?q=eleições+2018"
  parameters = []
  response = twitterreq(url, "GET", parameters)
  return json.load(response)

myResults = fetchsamples()
print("----------------------------------------------------------------")
print (myResults)
#print (type(myResults))
