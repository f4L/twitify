import tweepy
from tweepy import API
from tweepy import Cursor

# auth = tweepy.AuthHandler(XDEuh0hP1rQ3lcDZCp1RCE7BO, tZ9QcPCLyygVbVTcLQSkcL5J7Ovey8GeWOAKcmpn3oY00NNUzq)
# auth.set_access_token(3037907933-ALptgAJwoCZXacQDAz958AeOBsE6B4PDA27pbJu, iXzrkbjDWCyCQIJCks18wjdDX8I6N5fZJwWifaIYxZuWf)

# auth info (secret)
consumer_key="XDEuh0hP1rQ3lcDZCp1RCE7BO"
consumer_secret="tZ9QcPCLyygVbVTcLQSkcL5J7Ovey8GeWOAKcmpn3oY00NNUzq"
access_token="3037907933-ALptgAJwoCZXacQDAz958AeOBsE6B4PDA27pbJu"
access_token_secret="iXzrkbjDWCyCQIJCks18wjdDX8I6N5fZJwWifaIYxZuWf"

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
user = api.get_user('ejpdro')

print(user.screen_name)
print(user.followers_count)
for friend in user.friends():
    print(friend.screen_name)
