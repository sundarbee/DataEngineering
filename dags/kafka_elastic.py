import os
from dotenv import load_dotenv
from pathlib import Path
import tweepy as tw
import json
import kafka
 
env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)
 
consumer_key = os.getenv("TWITTER_API_KEY")
consumer_secret = os.getenv("TWITTER_API_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_TOKEN_SECRET")
 
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)
 
def dict_to_binary(the_dict):
 str = json.dumps(the_dict)
 binary = " ".join(format(ord(letter), "b") for letter in str)
 return binary
 
class MyStreamListener(tw.StreamListener):
 def on_status(self, data):
    tweet_dict = {
    "text": data.text,
    "user_name": data.user.name,
    "screen_name": data.user.screen_name,
    "id_string": data.user.id_str,
    "location": data.user.location,
    }
    print(data.text)
    producer.send("trump", json.dumps(tweet_dict).encode("utf-8"))
    return True
    
    def on_error(self, status_code):
        if status_code == 420:
            return False
 
producer = kafka.KafkaProducer(bootstrap_servers=['localhost:9092'],
              api_version=(0,11,5),
              value_serializer=lambda x: dumps(x).encode('utf-8'))
myStreamListener = MyStreamListener()
myStream = tw.Stream(auth=api.auth, listener=myStreamListener)
myStream.filter(track=["trump"], is_async=True)