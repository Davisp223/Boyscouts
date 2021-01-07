import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = "troop996automessager@gmail.com"
EMAIL_PASSWORD = "Troop996admin"

contacts = ['Email_ADDRESS', 'davisp713@gmail.com',]

msg = EmailMessage()
msg['Subject'] = 'Troop996 Automessage -- Do Not Reply'
msg['From'] = EMAIL_ADDRESS 
msg['To'] = file = open("mycontacts.txt", "r")


msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">Troop 996 - Auto generated emails </h1>
    </body>
</html>
""", subtype='html')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

print(msg)