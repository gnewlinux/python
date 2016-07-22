import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("gnewlinux@gmail.com", "fElix123321")
 
msg = "YOUR MESSAGE!"
server.sendmail("Ygnewlinux@gmail.com", "gnewlinux@gmail.com", msg)
server.quit()