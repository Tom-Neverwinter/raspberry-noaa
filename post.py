#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
import tweepy

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN_KEY = ''
ACCESS_TOKEN_SECRET = ''

# authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
# argentinaFlag = u'\U0001F1E6' + u'\U0001F1F7'

filenames = []
for element in sys.argv[3:]:
  filenames.append(element)

media_ids = []
for filename in filenames:
  res = api.media_upload(filename)
  media_ids.append(res.media_id)

#update this for status
api.update_status(status=argentinaFlag + ' Imagen satelital: ' + sys.argv[1] + '. Elevacion maxima: ' + sys.argv[2] + ' grados. #NOAA #weather #argentinaimagenes #noaasatellite #clima #wxtoimg #raspberrypi #argentina #argentinasat', media_ids=media_ids)
#English V1
# api.update_status(status=argentinaFlag + ' satellite Image: ' + sys.argv[1] + '. Max Elevation: ' + sys.argv[2] + ' Degrees. #NOAA #weather #noaasatellite #climate #wxtoimg #raspberrypi', media_ids=media_ids)
