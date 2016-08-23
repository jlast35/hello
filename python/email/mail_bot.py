import smtplib
from email.mime.text import MIMEText

smtp_host = 'smtp.gmail.com'
smtp_port = 587
username = 'digecor.mailbot@gmail.com'
password = 'tl7itotw$'

sender = username
receiver = 'jason.anderson@digecor.com'

message = MIMEText('digEcor mailbot test email')
message['Subject'] = 'digEcor mailbot test email'
message['From'] = sender
message['To'] = receiver

#try:
mailman = smtplib.SMTP(smtp_host,smtp_port)
print "Connected to SMTP host"
mailman.ehlo()
mailman.starttls()
mailman.login(username, password)
print "Login successful"
mailman.sendmail(sender,[receiver],message.as_string())
print "Sent mail"
mailman.quit()

#except:
#   print "Problem sending mail"