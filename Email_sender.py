import smtplib
from datetime import datetime
import schedule
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

sender_email ='pavitramb098@gmail.com'

password ='Temenos@1998'
receiver_email ='pavitramb321@gmail.com'

subject = 'Automated mail'
print("3")
body = """

Hello,

This is an automated email sent by a Python script.

Best regards,
Your Automated System

"""
message =MIMEMultipart()
message["FROM"] = sender_email
message["TO"] = receiver_email
message['Subject']= subject

message.attach(MIMEText(body, "plain"))
context = ssl.create_default_context()


def send_mail():
    
    try:
        
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            print("13")
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            
        print(f"Email sent to {receiver_email} succussfully")
        
    except Exception as e:
        print(f"failed to send email: {e}")
        
def scheduletime():
    schedule.every().day.at("9:00").do(send_mail)
    while True:
        schedule.run_pending()
        time.sleep(1)
if __name__ == "__main__":
    send_mail()
