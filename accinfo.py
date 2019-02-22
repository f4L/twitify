import tweepy

# auth info (secret)
consumer_key="XDEuh0hP1rQ3lcDZCp1RCE7BO"
consumer_secret="tZ9QcPCLyygVbVTcLQSkcL5J7Ovey8GeWOAKcmpn3oY00NNUzq"
access_token="3037907933-ALptgAJwoCZXacQDAz958AeOBsE6B4PDA27pbJu"
access_token_secret="iXzrkbjDWCyCQIJCks18wjdDX8I6N5fZJwWifaIYxZuWf"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Getting a user's account/follower information
user =  api.get_user('ejpdro')

print(user.screen_name)
print(user.followers_count)
for friend in user.friends():
    print(friend.screen_name)

# basic commands

# 20 most recent mentions + retweets
print(api.mentions_timeline())

# 20 most recent tweets that have been retweeted by others
print(api.retweets_of_me())

# Getting user acc activity
user = api.get_user('ejpdro')
print(api.get_user('ejpdro'))
