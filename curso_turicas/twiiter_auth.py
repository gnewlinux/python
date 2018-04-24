import tweepy

consumer_key = "dVCK89Pg0geCv1Dz4w7eesCTa"
consumer_secret = "KYLbAVSBJSO9PbxG9UhEeVv2pwcgjpR2DtNHI4JK5tM2PPqChR"
access_token = "864462438112145412-I0hZJHc25Ni5zcbPGTTszqe63OqVZ47"
access_token_secret = "D3hm4PgfKLOoLt34RTPKdb0utDnBOHNYAJCuVazrcMLwo"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

