import smtplib
sender = 'from@fromdomain.com'
recever = ['to@todomain.com']
message = """From: from person <from@fromdomain.com>
To: to person <to@todomain.com>
Subject:SMTP e-mail test
This is a test email message
"""
try:
    #first connect the smtp server to the localmachine
    fisrtemail = smtplib.SMTP('localhost')
    fisrtemail.sendmail(sender,recever,message)
    print("Email sent sucessfully!")
except SMTPException:
    print("Unable to send email")    
