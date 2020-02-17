#!/usr/bin/python3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import filecmp
import os


def send_appointment_email(sender,password,receiver,subject,emailText):
    
    try:
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = receiver
        msg ['Subject'] = subject
        body = emailText

        msg.attach(MIMEText(body,'plain'))
        
       
       
        text=msg.as_string()

        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login(sender,password)
        mail.sendmail(sender,receiver,text)
        mail.close()
    except Exception as err:
        print(err)
    
def send_info_email(email,name,body):
    try:
        adminEmail  = 'rushhourapp9@gmail.com'
        adminPass   = "!e123456789"
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = adminEmail
        msg ['Subject'] = 'Information Request'
        body = body

        msg.attach(MIMEText(body,'plain'))
        
       
       
        text=msg.as_string()

        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login(adminEmail,adminPass)
        mail.sendmail(email,adminEmail,text)
        mail.close()
    except Exception as err:
        print(err)


 
