import twitter

api = twitter.Api()

status_list = api.GetPublicTimeline()
for status in status_list:
	print status.gnewlinux
