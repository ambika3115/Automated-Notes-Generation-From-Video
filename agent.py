import smtplib
from email.message import EmailMessage
from config import EMAIL_SENDER, EMAIL_PASSWORD
import time

from modules.audio_extractor import extract_audio
from modules.transcriber import transcribe_audio
from modules.note_generator import generate_notes
from modules.file_saver import save_notes_as_pdf
from modules.email_sender import send_email

def run_pipeline(video_file):
    # Receipients mail ID
    email_list = [
        "ankit123@gmail.com",
        "aishwary123@gmail.com",
        "amit123@gmail.com"
    ]

    audio_path = "outputs/audio/audio.wav"
    notes_path = "outputs/notes/notes.pdf"

    extract_audio(video_file, audio_path)
    transcript = transcribe_audio(audio_path)
    notes = generate_notes(transcript)
    notes = notes.replace("•", "-").replace("–", "-")
    save_notes_as_pdf(notes, notes_path)

    # Open ONE SMTP connection
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)

        for email in email_list:
            print("Sending to:", email)

            msg = EmailMessage()
            msg["Subject"] = "📘 AI-Generated Notes from Your Video"
            msg["From"] = EMAIL_SENDER
            msg["To"] = email
            body = """
Dear Student,

I hope you are doing well.

Please find attached the AI-generated notes from the video you provided. These notes have been carefully structured with key concepts, bullet points, and a summary to help you understand the content more effectively.

You can review and use these notes for your study and revision purposes.

If you have any questions or need further assistance, feel free to reach out.

Best regards,  
Ambika yallal
"""

            msg.set_content(body)

            with open(notes_path, "rb") as f:
                msg.add_attachment(
                    f.read(),
                    maintype="application",
                    subtype="pdf",
                    filename="notes.pdf"
                )

            try:
                smtp.send_message(msg)
                print(f"Sent to {email}")
            except Exception as e:
                print(f"Failed for {email}: {e}")

            time.sleep(3)  # delay to avoid blocking

    return notes, notes_path