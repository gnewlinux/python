import smtplib

server =smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()

server.login('gnewlinux@gmail.com', 'pass')

de = 'gnewlinux@gmail.com'
para = ['gnewlinux@gmail.com']
msg = """From: %s
To: %s
Subject: Buteco Open Source

Email de teste do Buteco Open Source.""" % (de, ', '.join(para))

server.sendmail(de, para, msg)
server.close()