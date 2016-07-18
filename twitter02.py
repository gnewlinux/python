# -*- encoding: utf-8 -*-
import twitter
api = twitter.Api(username='gnewlinux', password='felix123321')
status = api.PostUpdate('''Yohohoho! Mensagem com Python''')
