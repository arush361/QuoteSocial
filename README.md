# QuoteSocial

## It simply does : 


Scrapes the quotes from the website https://www.brainyquote.com and creates a csv file of the quote and the respective author.

Randomly selects a quote and create a png image for the quote.

Post the Quote image to the Twitter, Instagram, Facebook


## Language
	
I have used python for the implementation.
	
	Python v2.7

## Setup


#### cd into the main directory 
    cd QuoteSocial/

#### Create a virtual environment
    virtualenv env

then   
        
    source env/bin/activate
    
#### Install the requirements :
    pip install -r requirements.txt

#### Generate csv file of quotes
    python quoteScrapper.py

this will create  a csv file of quotes to be used later.

#### Set the config file for the social platforms
##### For Twitter :

    cd twitter/
 
Create a config.py file inside this directory

    touch config.py  
or simply create a config.py file ( for windows )

Go to  https://dev.twitter.com/build and create a twitter app which will give the app credentials to set in the config.py file.

set the content in the config.py file as :

    CONSUMER_KEY = < your consumer key here >
    CONSUMER_SECRET = < your consumer secret here >
    ACCESS_TOKEN_KEY = < access token key here >
    ACCESS_TOKEN_SECRET = < access token secret here > 


### Run the API to post the quote to the social platforms.
    python main.py

this will handle everything and will simply post the quote png image to the social platforms.

