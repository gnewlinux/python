import tweepy

consumer_key = "dVCK89Pg0geCv1Dz4w7eesCTa"
consumer_secret = "KYLbAVSBJSO9PbxG9UhEeVv2pwcgjpR2DtNHI4JK5tM2PPqChR"
access_token = "864462438112145412-I0hZJHc25Ni5zcbPGTTszqe63OqVZ47"
access_token_secret = "D3hm4PgfKLOoLt34RTPKdb0utDnBOHNYAJCuVazrcMLwo"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.get_user('diegosarzi')._json

def seguidores(usuarios_no_twitter):
    consulta_api = api.get_user(usuarios_no_twitter)._json
    seguidores = consulta_api['followers_count']
    return seguidores
  
def seguindo(usuarios):
   consulta_api = api.get_user(usuarios)._json
   seguindo = consulta_api['friends_count']
   return seguindo       

nome = input('Digite o user twitter: ')
seguidores = seguidores(nome)
seguindo = seguindo(nome)

print(f'Quantos seguem: {seguidores}, seguindo: {seguindo}')
