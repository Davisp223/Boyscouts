from django.dispatch import receiver
from django.db.models import signals
from .models import Post
import os
import smtplib
import imghdr
from email.message import EmailMessage




@receiver(signals.post_save, sender=Post)
def send_mail(sender, instance, created, **kwargs):

    context = {
        'posts': Post.objects.all()
        }

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

    msg.add_alternative("""\
    <!DOCTYPE html>
    <html>
     <body>
           <h1 style="color:SlateGray;"> {{ content }}</h1>
        </body>
    </html>
    """, subtype='html')




    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

    print(msg)