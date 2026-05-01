from email_reader import fetch_emails

def save_emails():
    emails = fetch_emails()

    with open("data/emails.txt", "w", encoding="utf-8") as f:
        for email in emails:
            f.write(email + "\n\n---\n\n")



if __name__ == "__main__":
    save_emails()