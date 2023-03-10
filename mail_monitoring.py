import imaplib
import email

mail = imaplib.IMAP4_SSL('mail.server.com')
mail.login('username', 'password')
mail.select('inbox')

result, data = mail.search(None, 'UNSEEN')
for num in data[0].split():
    result, data = mail.fetch(num, '(RFC822)')
    email_body = data[0][1]
    mail_subject = email.message_from_bytes(email_body).get('Subject')
    mail_from = email.message_from_bytes(email_body).get('From')
    print(f"Subject: {mail_subject}")
    print(f"From: {mail_from}")

mail.close()
mail.logout()

