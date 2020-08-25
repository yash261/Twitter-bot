import tweepy
import time
auth=tweepy.OAuthHandler('enter consumer_key','enter consumer_secret')
auth.set_access_token('enter access_token','enter access_token_secret')
api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
def retweet():
    for tweet in api.search(q='enter text or #hashtag you want to retweet',rpp=10):
        rt=tweet.id
        try:
            api.retweet(rt)
            print("tweeted")
        except:
            print('already tweeted')
        #f'{tweet.user.name}: {tweet.text}'
def message(msg):
    for i in range(250,350):
        print(i)
        api.update_status(msg+str(i))
try:
    api.verify_credentials()
    msg=input("Enter message:")
    print("working")
    message(msg)
    for i in range(40):
        retweet()
        time.sleep(3)
    
except:
    print("some problem")