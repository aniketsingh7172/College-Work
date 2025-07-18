import smtplib
conn=smtplib.SMTP('smtp.gmail.com',587)
conn.ehlo()
conn.starttls()

def email_input():
    sender_email=input("Enter sender email: ")
    print(sender_email)
    return sender_email

email_input()