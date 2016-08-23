import smtplib
import getpass
from email.mime.text import MIMEText

sender = 'jason.anderson@digecor.com'
receiver = 'jason.anderson@digecor.com'

message = MIMEText('Python email test')
message['Subject'] = 'Python test email'
message['From'] = sender
message['To'] = receiver

password = getpass.getpass()
#try:
mailman = smtplib.SMTP("smtp.office365.com",587)
mailman.starttls()
mailman.ehlo()
mailman.login(sender, password)

mailman.sendmail(sender,[receiver],message.as_string())
print "Sent mail"
mailman.quit()

#except:
#   print "Problem sending mail"