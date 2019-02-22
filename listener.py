import textblob as textblob
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
from textblob import TextBlob

# auth info (secret)
consumer_key="XDEuh0hP1rQ3lcDZCp1RCE7BO"
consumer_secret="tZ9QcPCLyygVbVTcLQSkcL5J7Ovey8GeWOAKcmpn3oY00NNUzq"
access_token="3037907933-ALptgAJwoCZXacQDAz958AeOBsE6B4PDA27pbJu"
access_token_secret="iXzrkbjDWCyCQIJCks18wjdDX8I6N5fZJwWifaIYxZuWf"


class StdOutlistener(StreamListener):
    def on_data(self, data):
        all_data = json.loads(data)
        tweet = TextBlob(all_data["text"])

        #Add the 'sentiment' data to all_data
        all_data['sentiment'] = tweet.sentiment

        print(tweet)
        print(tweet.sentiment)

        # Open json text file to save the tweets
        with open('tweets.json', 'a') as tf:
            # Write a new line
            tf.write('\n')

            # Write the json data directly to the file
            json.dump(all_data, tf)
            # Alternatively: tf.write(json.dumps(all_data))

        return True

    def on_error(self, status):
        print(status)


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Twitter IDs: ejpdro = 418032314, notwlsn = 3037907933, owengift = 3251789096, benjweldon = 2323972303
twitterStream = Stream(auth, StdOutlistener())
twitterStream.filter(languages=["en"], follow=["418032314", "3037907933", "3251789096", "2323972303"])
