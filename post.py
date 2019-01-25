#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
import tweepy

# Consumer keys and access tokens, used for OAuth
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN_KEY = ''
ACCESS_TOKEN_SECRET = ''

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

filenames = []
for element in sys.argv[3:]:
  filenames.append(element)

media_ids = []
for filename in filenames:
  res = api.media_upload(filename)
  media_ids.append(res.media_id)

  # Sample method, used to update a status
api.update_status(' Satelite image: ' + sys.argv[1] + '. max elevation: ' + sys.argv[2] + ' Degrees. #NOAA #weather #noaasatellite #climate #wxtoimg #raspberrypi ', media_ids=media_ids)
