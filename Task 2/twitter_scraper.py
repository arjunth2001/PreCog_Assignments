import tweepy
import json
import time

total_tweets=0
min_tweets_required=10000
num_tweets_in_one_go=100
oldest=1339207339711234052


consumer_key = "DqjW4VdIPFv4fC7YWVGpJiqtG"
consumer_secret = "ojrpev2HJu2E2Du5YlSQjUu8W8frYgX6n3FCtJvqyr7GBrLSOX"
access_key = "929492088915337216-yP5PizbCfNMGVSJtt3OgIFlh3iJiB34"
access_secret = "06ZhcJo02h2dZclkugH04fdelLEppg151A3mq4x3FuJ2T"

filename="tweets.json"


def get_top_tweets_for_hashtag_from_HYD(hashtag, api):
    global num_tweets_in_one_go
    global filename
    global total_tweets
    global oldest
    try:
        tweets = tweepy.Cursor(api.search, q=hashtag,geocode="17.3841,78.4564,60km",max_id=oldest).items(num_tweets_in_one_go)
    except Exception as e:
        print(e)
        time.sleep(5)
    with open(filename, 'a') as f:
        for tweet in tweets:
            total_tweets+=1
            if oldest==None:
                oldest=tweet.id-1
            elif oldest > tweet.id:
                oldest=tweet.id-1
            f.write(json.dumps(tweet._json)+"\n")


    
    
                


def get_top_keyword_in_HYD(api):
    hyd_trend= api.trends_place(2295414)
    return str(hyd_trend[0]["trends"][0]['name'])



    
if __name__ == '__main__':
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
    hashtag=get_top_keyword_in_HYD(api)
    #print(hashtag)
    while(total_tweets <= min_tweets_required):
        get_top_tweets_for_hashtag_from_HYD("#KomaramBheemNTR",api)
        print("Progess:" , total_tweets, min_tweets_required)
        

        
        





