# Import python class
import json
from twython import Twython

# # To initiate/write json file with credentials in it
# credentials = {}
# credentials['CONSUMER_KEY'] = 'XDEuh0hP1rQ3lcDZCp1RCE7BO'
# credentials['CONSUMER_SECRET'] = 'tZ9QcPCLyygVbVTcLQSkcL5J7Ovey8GeWOAKcmpn3oY00NNUzq'
# credentials['ACCESS_TOKEN'] = '3037907933-ALptgAJwoCZXacQDAz958AeOBsE6B4PDA27pbJu'
# credentials['ACCESS_SECRET'] = 'iXzrkbjDWCyCQIJCks18wjdDX8I6N5fZJwWifaIYxZuWf'
#
# with open('twitter_credentials.json', 'w') as file:
#     json.dump(credentials, file)

# TWYTHON SEARCH EXAMPLE <--
# Load credentials from JSON file
with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)

# Instantiate an object
python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])

# Create query
query = {'q': 'crackhead',
        'result_type': 'popular',
        'count': 10,
        'lang': 'en',
        }

import pandas as pd

# Seacrh tweets
dict_ = {'user': [], 'date': [], 'text': [], 'favorite_count': []}
for status in python_tweets.search(**query)['statuses']:
    dict_['user'].append(status['user']['screen_name'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['text'])
    dict_['favorite_count'].append(status['favorite_count'])

# Structure data into pandas DataFrame
df = pd.DataFrame(dict_)
df.sort_values(by='favorite_count', inplace=True, ascending=False)
df.head(5)
# END TWYTHON SEARCH EXAMPLE -->

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# TWYTHON STREAMING EXAMPLE <--
from twython import TwythonStreamer
import csv

# Filter out unwanted data
def process_tweet(tweet):
    d = {}
    d['hashtags'] = [hashtag['text'] for hashtag in tweet['entities']['hashtags']]
    d['text'] = tweet['text']
    d['user'] = tweet['user']['screen_name']
    d['user_loc'] = tweet['user']['location']
    return d

# Create a class to inherit TwythonStreamer
class MyStreamer(TwythonStreamer):

    # Recieved data
    def on_success(self, data):

        # Only collect tweets in Eng
        if data['lang'] == 'en':
            tweet_data = process_tweet(data)
            self.save_to_csv(tweet_data)

    # Problem with API
    def on_error(self, status_code, data):
        print(status_code, data)
        self.disconnect()

    # Save each tweet to a CSV file
    def save_to_csv(self, tweet):
        with open(r'saved_tweets.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow(list(tweet.values()))
# END STREAMING EXAMPLE -->

import pandas as pd
tweets = pd.read_csv("saved_tweets.csv")
tweets.head()
