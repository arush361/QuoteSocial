"""
	author : abhishek goswami
	abhishekg785@gmail.com

	main.py : the actual flow of the programme that handles all the modules and packages 
	at one place
"""

import os
import csv
from random import randint

from textToImage import TextToImage 	# TextToImage module to convert the quote text into a png file

from twitter import twitter 	# twitter package to handle the twitter related functions


class QuoteIT(object):

	def __init__(self):
		pass

	def get_random_quote_from_csv(self):
		"""Simply returns a random quote from the csv file 
		generated earlier using quoteScrapper.py 

		@return
			{ 
				"text" : "Life is short! Stop living someone else's life", 
				"author" : "Steve Jobs" 
			}
		"""

		quotes = []
		rownum = 0;
		file_name = "top_100_quotes.csv"
		with open(file_name, 'rb') as f:	# start reading the csv file
			reader = csv.reader(f)
			for row in reader:
				if rownum == 0:
					header = row 	# separates the header part of the csv file
				else:
					text = row[0]	
					author = row[1]
					quote = { 'text' : text, 'author' : author }
					quotes.append(quote)
				rownum += 1
			quotes_count = len(quotes)
			random_count = randint(0, quotes_count - 1)		# generates a random no here 
			random_quote = quotes[random_count]
			return random_quote



if __name__ == '__main__':
	image_name = 'quote.png'	# default name of the quote png image to be generated
	obj = QuoteIT()
	quote = obj.get_random_quote_from_csv()

	# converts the quote text into a image 
	image_conv = TextToImage(quote['text'], image_name)
	image_conv.create_image()	# this creates the png image of the quote called inside the textToImage module

	IMAGE_PATH = os.path.join(os.path.dirname(__name__), 'quote.png') 	# creates a path to the image in the root dir

	#post the image to twitter
	twitter_obj = twitter.Twitter()
	twitter_obj.post_image(IMAGE_PATH)