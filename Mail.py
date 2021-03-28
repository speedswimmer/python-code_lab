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
#with smtplib.SMTP('localhost', 1025) as smtp:
#    smtp.ehlo()
#    smtp.starttls()
#    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    #subject = 'Grab dinner this weekend?'
    #body = 'How about dinner at 6pm this Saturday?'
    #salut = 'CU, Name'

    #msg = f'Subject: {subject}\n\n{body}\n\n{salut}'

    for i in range (1,num_e+1):
        time.sleep(0.1)
        print("Email",i, " sent")
        #smtp.sendmail(EMAIL_ADDRESS, receipient, msg)
        smtp.send_message(msg)

