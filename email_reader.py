import imaplib
import email
from config import EMAIL_USER, EMAIL_PASSWORD

def fetch_emails():
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(EMAIL_USER, EMAIL_PASSWORD)
    mail.select("inbox")

    _, messages = mail.search(None, "ALL")
    email_ids = messages[0].split()

    emails = []

    for e_id in email_ids[-20:]:  # last 20 emails
        _, msg_data = mail.fetch(e_id, "(RFC822)")

        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])

                subject = msg["subject"]
                body = ""

                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == "text/plain":
                            body = part.get_payload(decode=True).decode(errors="ignore")
                else:
                    body = msg.get_payload(decode=True).decode(errors="ignore")

                emails.append(f"Subject: {subject}\n{body}")

    mail.logout()
    return emails