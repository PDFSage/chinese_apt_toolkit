import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

class SpearPhisher:
    def __init__(self, smtp_host, smtp_port, username, password):
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, from_addr, to_addr, subject, body, attachment_path=None):
        msg = MIMEMultipart()
        msg['From'] = from_addr
        msg['To'] = to_addr
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        if attachment_path:
            with open(attachment_path, "rb") as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(attachment_path)}")
                msg.attach(part)

        try:
            server = smtplib.SMTP(self.smtp_host, self.smtp_port)
            server.starttls()
            server.login(self.username, self.password)
            text = msg.as_string()
            server.sendmail(from_addr, to_addr, text)
            server.quit()
            print(f"Email sent to {to_addr}")
        except Exception as e:
            print(f"Failed to send email: {e}")

if __name__ == '__main__':
    # Example usage
    phisher = SpearPhisher("smtp.gmail.com", 587, "your_email@gmail.com", "your_password")
    phisher.send_email(
        "it.support@acme.com",
        "target@example.com",
        "Important Security Update",
        "Please review the attached security update.",
        "malicious.docx"
    )
