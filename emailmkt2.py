# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
with open(textfile) as fp:
    # Create a text/plain message
    msg = MIMEText(fp.read())

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'The contents of %s' % textfile
msg['From'] = gnewlinux@gmail.com
msg['To'] = gnewlinux@gmail.com

# Send the message via our own SMTP server.
s = smtplib.SMTP('smtp.gmail.com', 587)
s.smtp.starttls()
s.smtp.login('gnewlinux@gmail.com', 'felix123321')
s.send_message(msg)
s.quit()