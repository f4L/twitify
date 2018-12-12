from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = 'amxElnK6NlYAyyrH8sgDx3qbL'
csecret = 'lIi2tdBuuCwIs3lCeSXPo1ERQGIzujnBElr6usvltX9vL79O4D'
atoken = '3037907933-HadjMd1MhLaPOiyWuob84ijrRK5iXjYURDEBUJi'
asecret = 'sUlXnvnYfvKPtkvK8halPxDm0b6kZmV6DnIhxONzjWbss'

class listener(StreamListener):

    def on_data(self, data):
        print(data)
        return true

    def on_error(self, status):
         print(status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])





