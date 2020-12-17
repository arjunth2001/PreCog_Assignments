import sys
import tweepy
import json

consumer_key = "DqjW4VdIPFv4fC7YWVGpJiqtG"
consumer_secret = "ojrpev2HJu2E2Du5YlSQjUu8W8frYgX6n3FCtJvqyr7GBrLSOX"
access_key = "929492088915337216-yP5PizbCfNMGVSJtt3OgIFlh3iJiB34"
access_secret = "06ZhcJo02h2dZclkugH04fdelLEppg151A3mq4x3FuJ2T"
count=0

def get_top_keyword_in_HYD(api):
    hyd_trend= api.trends_place(2295414)
    return str(hyd_trend[0]["trends"][0]['name'])

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
keyword = get_top_keyword_in_HYD(api)
print(keyword)

class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        global count
        try: 
                with open("tweets.json",'a') as f:
                    f.write(json.dumps(status._json)+"\n")
                    count+=1
                    print(count)
        except Exception as e:
            print(e)

        if(count==10000):
            return False



    def on_error(self, status_code):
        print('Encountered error with status code:', status_code)
        return True

    def on_timeout(self):
        print( 'Timeout...')
        time.sleep(15*60)
        return True


sapi = tweepy.streaming.Stream(auth, CustomStreamListener())    
sapi.filter(track=[keyword])