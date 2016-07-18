import twitter
api = twitter.Api()

tweets = api.GetPublicTimeline('gnewlinux')
for tweet in tweets:
    print tweet.text


