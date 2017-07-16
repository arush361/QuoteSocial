"""
	author : abhishek goswami
	abhishekg785@gmail.com

	twitter.py 
	for tweeting image to the twitter 


	Twitter api v1.1 uses Oauth now, so we will need to Oauth 
	So i am using Tweepy for handling oauth and handling things with the Twitter API
"""

import config

from tweepy import OAuthHandler 	# tweepy for OAuth
from tweepy import API

import os	# will be using to get the path of the quote image

ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__name__) , os.path.pardir))


class Twitter(object):

	def __init__(self):
		try:
			consumer_key = config.CONSUMER_KEY
			consumer_secret = config.CONSUMER_SECRET
			access_token_key = config.ACCESS_TOKEN_KEY
			access_token_secret = config.ACCESS_TOKEN_SECRET
			self.auth = OAuthHandler(consumer_key, consumer_secret)
			self.auth.set_access_token(access_token_key, access_token_secret)
			self.api = API(self.auth, wait_on_rate_limit = True)
			print "Authenticated with Twitter :)"
		except Exception as err:
			print 'Error occurred with twitter auth!'
			print err


	def post_image(self, IMAGE_PATH):
		try:
			self.api.update_with_media(IMAGE_PATH, 'Here is a quote !')
		except Exception as err:
			print 'Error occurred with twitter image upload! Try again'
			print err


# for demo

# if __name__ == '__main__':
#   IMAGE_PATH = os.path.join(ROOT_PATH, 'quote.png')
# 	obj = Twitter()
# 	obj.post_image(IMAGE_PATH)