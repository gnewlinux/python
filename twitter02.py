# -*- encoding: utf-8 -*-
import twitter
api = twitter.Api(username='gnewlinux', password='pass')
status = api.PostUpdate('''Yohohoho! Mensagem com Python''')
