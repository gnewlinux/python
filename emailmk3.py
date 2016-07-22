import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("gnewlinux@gmail.com", "pass")
 
msg = "YOUR MESSAGE!"
server.sendmail("Ygnewlinux@gmail.com", "gnewlinux@gmail.com", msg)
server.quit()