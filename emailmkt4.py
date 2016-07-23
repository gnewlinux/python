#! /usr/bin/python

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# open and read list emails
arquivo = open('lista.txt', 'r')
emails = arquivo.read().splitlines()

# me == my email address
# you == recipient's email address
me = "gnewlinux@gmail.com"
you = emails

# Create message container 	- the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Link"
msg['From'] = me
msg['To'] = ", ".join(you)

# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
html = """\
<html>
  <head></head>
  <body>
    <p>HEY!<br>
       Como vai vocẽ?<br>
       EMAIL COM PYTHON <a href="http://www.python.org">link</a> :).
       <br>
       <img src='http://static.giantbomb.com/uploads/original/0/3683/1120634-penguin_chick.jpg'></img>
    </p>
  </body>
</html>
"""

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)

# Send the message via local SMTP server.
s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
s.ehlo()
s.login('gnewlinux@gmail.com', 'pass')
# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
s.sendmail(me, you, msg.as_string())
s.quit()