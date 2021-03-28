#script to send emails using gmail account

import os
import time
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

receipient = str(input("What is the receipient e-mail address? "))
num_e = int(input("How many Emails to send? "))

# defining Email body
msg = EmailMessage()
msg['Subject'] = 'Grab dinner this weekend?'
msg['From'] = EMAIL_ADDRESS
msg['To'] = receipient
msg.set_content('How about dinner at 6pm this Saturday?')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    for i in range (1,num_e+1):
        time.sleep(0.1)
        print("Email",i, " sent")
        smtp.send_message(msg)

