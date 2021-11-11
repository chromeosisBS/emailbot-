import smtplib, ssl
from getpass import getpass

port = 587  # For starttls
smtp_server = "smtp.gmail.com" # choose smtp server default is google
# get sender creds
sender_email = "example@gmail.com"
password = getpass("type your password and press enter:")
# get reciever emil
receiver_email= input("Enter  receiver email: ")
#compose message here
message = imput("enter message and press enter:")

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)