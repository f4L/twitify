import tweepy
from tweepy import API
from tweepy import Cursor

# auth = tweepy.AuthHandler(, )
# auth.set_access_token(, )

# auth info (secret)
consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# If authentication was successful, this will print account name
# print(api.me().name)

# End of authorization
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

# Get the user object for twitter...
user = api.get_user('')

print(user.screen_name)
print(user.followers_count)
for friend in user.friends():
    print(friend.screen_name)
