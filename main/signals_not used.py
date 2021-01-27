#   import imghdr
#   import os
#   import smtplib
#   from email.message import EmailMessage
#   from django.db.models import signals
#   from django.dispatch import receiver
#   from .models import Post


#@receiver(signals.post_save, sender=Post)
#def send_mail(sender, instance, created, **kwargs):
#     to test if the signal is working
#    print('signal send')
#     replace it with your code once it works
#    EMAIL_ADDRESS = "troop996automessager@gmail.com"
#    EMAIL_PASSWORD = "Troop996admin"
#
#
 #   msg = EmailMessage()
 #   msg['Subject'] = 'Troop996 Automessage -- Do Not Reply'
#   msg['From'] = EMAIL_ADDRESS 
#    msg['To'] = file = open("main/contacts.txt", "r")

#msg.add_alternative("""
#<!DOCTYPE html>
#<html>
#    <body>
#        <h1 style="color:SlateGray;">New Update has been posted to the website visit the website at www.troop996.org</h1>
#    </body>
#</html>
#""", subtype='html')


#    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#        smtp.send_message(msg)

#    print(msg)
