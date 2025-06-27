import smtplib
from email.message import EmailMessage

def send_gmail_email( app_password, recipients, body, attachment_path):
    sender_email = "diyasingh1015@gmail.com"
    msg = EmailMessage()
    msg['Subject'] = "Meeting Summary PDF"
    msg['From'] = sender_email
    msg['To'] = ", ".join(recipients)
    msg.set_content(body)

    with open(attachment_path, "rb") as f:
        file_data = f.read()
        from os.path import basename
        msg.add_attachment(file_data, maintype="application", subtype="pdf", filename=basename(attachment_path))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)

    print("Email sent successfully.")