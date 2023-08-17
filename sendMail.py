#!/usr/bin/env python3

import os

from dotenv import load_dotenv
from getpass import getpass

from smtplib import SMTP
from email.mime.text import MIMEText

def test_conn_open(conn):
    try:
        status = conn.noop()[0]
    except:  # smtplib.SMTPServerDisconnected
        status = -1
    return True if status == 250 else False

"""
Take HTML Content and send the mail
"""
def sendmail(mail, sender, recipient, email):
  
      msg = MIMEText(email.content, 'html')

      msg['Subject'] = email.subject
      msg['From'] = sender
      msg['To'] = recipient

      mail.sendmail(sender, recipient, msg.as_string())

def sendmails (mail, sender, recipients, email): 
      for recipient in recipients : 
        sendmail(mail, sender, recipient, email)
        print("sent to ", recipient)

def getSES ():
      load_dotenv('.env')
      usr = os.environ.get('EMAIL_USER', None)
      pwd = os.environ.get('EMAIL_PASS', None)
      host = os.environ.get('EMAIL_HOST', None)
      port = os.environ.get('EMAIL_PORT', None)
      if port : port = int(port)

      if not usr: usr = input("username: ")
      if not pwd: pwd = getpass("password: ")
      if not host: host = input("smtp host: ")
      if not port: port = int(input("smtp port: "))

      ses = SMTP(host, port)
      ses.starttls()
      ses.login(usr, pwd)
      return ses


