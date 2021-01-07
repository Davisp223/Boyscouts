import imghdr
import os
import smtplib
from email.message import EmailMessage

from django.db.models import signals
from django.dispatch import receiver

from .models import Post


@receiver(signals.post_save, sender=Post)
def send_mail(sender, instance, created, **kwargs):
    breakpoint()  #from Python3.7
    model = Post
    context_object_name = 'posts'
    # to test if the signal is working
    print('signal send')
    # replace it with your code once it works
    EMAIL_ADDRESS = "troop996automessager@gmail.com"
    EMAIL_PASSWORD = "Troop996admin"

    contacts = ['Email_ADDRESS', 'davisp713@gmail.com',]

    msg = EmailMessage()
    msg['Subject'] = 'Troop996 Automessage -- Do Not Reply'
    msg['From'] = EMAIL_ADDRESS 
    msg['To'] = file = open("main/contacts.txt", "r")
    msg.set_content = f"Lets see if this works {content}"




    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

    print(msg)
