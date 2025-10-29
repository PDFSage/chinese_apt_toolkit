import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_phishing_email(from_email, to_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, "password")
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Error: {e}")

def main():
    from_email = input("Enter from email: ")
    to_email = input("Enter to email: ")
    subject = input("Enter subject: ")
    body = input("Enter body: ")
    send_phishing_email(from_email, to_email, subject, body)

if __name__ == "__main__":
    main()
