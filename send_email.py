import smtplib
import getpass
from email.mime.text import MIMEText

def send_mail():
    sender_address = 'supriyachaudhari140@gmail.com'
    print('Password : ')
    password = getpass.getpass()
    subject = 'AI - Mafia Machine Learning'
    msg = '''
        Machine Learning
        Machine learning is a sub-category of artificial intelligence and effectively automates the process of analytical model building and allows machines to adapt to new scenarios independently.
        
        Thank You!
        Supriya Chaudhari
    '''
    #server initialization
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender_address,password)
    recipients = 'supriyachaudhari140@gmail.com'

    #draft my message body
    msg = MIMEText(msg)
    msg['Subject'] = subject
    msg['From'] = sender_address
    #msg['To'] = ", ".join(recipients)
    msg['To'] = 'supriyachaudhari140@gmail.com'
    #msg.set_param('importance','high value')


    server.sendmail(sender_address, recipients, msg.as_string())
    print("Mail Sent...!")

send_mail()