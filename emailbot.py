import smtplib, ssl
from getpass import getpass
import os


port = 587  # For starttls
smtp_server = "smtp.gmail.com" # choose smtp server default is google
# get sender creds
def login():
    sender_email = "emailbottesting@gmail.com" # put your email here
    password = getpass("type your password and press enter:")

# get reciever email

def get_reciever():
    receiver_email= input("Enter  receiver email: ")

f=open("message.txt", "r")
if f.mode == 'r':

    message = f.read()
context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted

def send(): 
    print (message)
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
        
        