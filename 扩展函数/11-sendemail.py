#!/usr/bin/env python  
# -*- coding: UTF-8 -*-  
  
from email.mime.multipart import MIMEMultipart  
from email.mime.base import MIMEBase  
from email.mime.text import MIMEText  
   
from email.utils import COMMASPACE,formatdate  
from email import encoders  
   
import os  
   
def send_mail(server, fro, to, subject, text, files=[]):   
    assert type(server) == dict   
    assert type(to) == list   
    assert type(files) == list   
   
    msg = MIMEMultipart()   
    msg['From'] = fro   
    msg['Subject'] = subject   
    msg['To'] = COMMASPACE.join(to) #COMMASPACE==', '   
    msg['Date'] = formatdate(localtime=True)   
    msg.attach(MIMEText(text))   
   
    for f in files:   
        part = MIMEBase('application', 'octet-stream') #'octet-stream': binary data   
        part.set_payload(open(f, 'rb').read())   
        encoders.encode_base64(part)   
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))   
        msg.attach(part)   
   
    import smtplib   
    smtp = smtplib.SMTP(server['name'], server['port'])   
    smtp.ehlo()  
    smtp.starttls()  
    smtp.ehlo()   
    smtp.login(server['user'], server['passwd'])   
    smtp.sendmail(fro, to, msg.as_string())   
    smtp.close()  
      
if __name__=='__main__':  
    server = {'name':'mail.niub.la', 'user':'testeam.abcft', 'passwd':'Test@123', 'port':465}  
    fro = 'testeam@abcft.com'  
    to = ['ygu@abcft.com']  
    subject = '脚本运行提醒'  
    text = 'mail content'  
    #files = ['top_category.txt']  
    #send_mail(server, fro, to, subject, text, files=files) 
    send_mail(server, fro, to, subject, text)   