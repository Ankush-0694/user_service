from flask_mail import  Message
from Constants.constants import *

def send_email(msgData):
    from app import mail 

    mail.send(msgData)
    # print(msgData)
    return 'Mail sent'