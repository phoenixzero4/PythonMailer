import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

def get_info(file):
    with open(file, 'r') as f:
        recipients = f.readlines()
    return recipients

def main():
    server = smtplib.SMTP('smtp.shaw.ca', 25)
    server.ehlo()

    # retrieve password and email address from file
    with open('password.txt', 'r') as f:
        password = f.readline().strip()
        account = f.readline().strip()

    server.login(account, password)

    msg = MIMEMultipart()
    recipients = get_info('info.txt')
    subject = recipients[0]
    subject = subject[8:]

    for r in range(1, len(recipients),2): 
        msg['From'] = account
        to = recipients[r].strip()
        msg['To']  = to[3:]
        filename = recipients[r+1].strip()
        filename = filename[3:]
        msg['Subject'] = subject

        with open('email_body.txt', 'r') as email:
            message = email.read()

        msg.attach(MIMEText(message, 'plain'))
        if filename != 'None':
            attachment = open(filename, 'rb')
            p = MIMEBase('application', 'octet-stream')
            p.set_payload(attachment.read())
            encoders.encode_base64(p)
            p.add_header('Content-Disposition', f'attachment; filename={filename}')
            msg.attach(p)
        text = msg.as_string()
        server.sendmail(account, to, text)    
    

main()
