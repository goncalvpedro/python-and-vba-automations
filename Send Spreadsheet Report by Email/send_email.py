from email.message import EmailMessage
import smtplib
import ssl


def send_email(from_email, to_email, subject, body):
    password = open('password.txt', 'r').read().strip()
    message = EmailMessage()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = subject

    message.set_content(body)

    safe = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
        smtp.login(from_email, password)
        smtp.send_message(message, from_email, to_email)
