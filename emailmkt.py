import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()

server.login('gnewlinux@gmail.com', 'pass')

de = 'gnewlinux@gmail.com'
para = ['gnewlinux@gmail.com']
msg = """From: %s
To: %s
Subject: EMAIL POR PYTHON

<HTML>
<HEAD>
<TITLE>EMAIL MKT</TITLE>
</HEAD>
<BODY>

Email de teste de envio via python! YAAAAAAAAA. <a href='www.google.com.br'>clique aqui</a>


</BODY>
</HTML>
""" % (de, ', '.join(para))


server.sendmail(de, para, msg)
server.close()