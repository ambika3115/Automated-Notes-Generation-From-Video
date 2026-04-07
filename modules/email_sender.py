from config import EMAIL_SENDER, EMAIL_PASSWORD
import smtplib
from email.message import EmailMessage

'''def send_email(receiver, subject, body, attachment_path):

    if not receiver or "@" not in receiver:
        return "Invalid email address"

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = EMAIL_SENDER
    msg["To"] = receiver
    msg.set_content(body)

    with open(attachment_path, "rb") as f:
        msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename="notes.pdf")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
        smtp.send_message(msg)

    return "Email sent successfully!" '''

def send_email(receiver, subject, body, attachment_path):
    try:
        # existing code...

        print(f"✅ Sent to {receiver}")
        return True

    except Exception as e:
        print(f"❌ Failed for {receiver}: {str(e)}")
        return False