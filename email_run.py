from main import pirce_track


import smtplib

price_t=pirce_track()

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from requests.sessions import session

sender='tanmoysaha7112000@gmail.com'

sender_pass='tanmoy7112000'
reciever='tanmoysaha52643@gmail.com'

content_message='Product Name is '+price_t.get_name()
message=MIMEMultipart()
message['From']=sender
message['To']=reciever

message['Subject']='Hey we are just testing'

message.attach(MIMEText(content_message,'plain'))


session=smtplib.SMTP('smtp.gmail.com',587)

session.starttls()

session.login(sender,sender_pass)

text=message.as_string()

session.sendmail(sender,reciever,text)

session.quit()

print('Email Sent Succesfully')
