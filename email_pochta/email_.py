# # xqvmseglngdupwrf
# import smtplib
#
# host = 'smtp.gmail.com'
# sender = 'absaitovdev@gmail.com'
# port = 465
# email = 'xoliqulov116@gmail.com'
# password = 'xqvmseglngdupwrf'
#
# msg = "Hello , My name is Botirjon"
# with smtplib.SMTP_SSL(host , port) as server:
#     server.login(sender , password)
#     server.sendmail(sender , email , msg)
#     print("Send message !")
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
mail_content = '''Hello,
This is a test mail.
In this mail we are sending some attachments.
The mail is sent using Python SMTP library.
Thank You
'''
#The mail addresses and password
sender = 'absaitovdev@gmail.com'
password = ''
receiver = 'absaitovdev@gmail.com'
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = 'A test mail sent by Python. It has an attachment.'


message.attach(MIMEText(mail_content, 'plain'))
attach_file = open('email_.py', 'rb')
payload = MIMEBase('application', 'octate-stream')
payload.set_payload((attach_file).read())
encoders.encode_base64(payload)

payload.add_header('Content-Decomposition', 'attachment', filename='email_.py')
message.attach(payload)

session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(sender, password)
text = message.as_string()
session.sendmail(sender, receiver, text)
session.quit()
print('Mail Sent')
