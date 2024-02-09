import smtplib
import os

SENDEREMAIL = os.environ.get('senderemail')
MYEMAIL = os.environ.get('email')
PASSWORD = os.environ.get('password')

def email(host):
    with smtplib.SMTP("eu-smtp-outbound-1.mimecast.com", 25) as connection:
        connection.starttls()
        connection.login(user=SENDEREMAIL, password=PASSWORD)
        connection.sendmail(from_addr=SENDEREMAIL,
                            to_addrs=MYEMAIL,
                            msg=f"subject:{ host } is down\n\n{ host } is offline and has failed for 3 seperate checks")