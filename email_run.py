from main import pirce_track

import pandas as pd
import smtplib

price_t=pirce_track()



def send_email(reciever):
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    

    sender='tanmoysaha7112000@gmail.com'

    sender_pass='tanmoy7112000'
    
    product_name=price_t.get_name()
    price_now=price_t.get_price()
    content_message='Product Name is '+product_name+'\n Price is now :'+price_now
    message=MIMEMultipart()
    message['From']=sender
    message['To']=reciever
    
    message['Subject']='Good news ! Price of your product'+product_name+' came down'

    message.attach(MIMEText(content_message,'plain'))


    session=smtplib.SMTP('smtp.gmail.com',587)

    session.starttls()

    session.login(sender,sender_pass)

    text=message.as_string()

    session.sendmail(sender,reciever,text)

    session.quit()

    print('Email Sent Succesfully')

df=pd.read_csv('price.csv')


if int(price_t.get_price())<int(df.product_price):
    send_email('tanmoysaha52643@gmail.com')
    print('Mail Send Successfully')
    price_t.create_csv()
    
