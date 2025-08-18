import smtplib        # Module to send emails via SMTP
import traceback      # Module to print detailed error stack trace


gmail_user = 'you@gmail.com'      # Your Gmail address
gmail_password = 'P@ssword!'      # Your Gmail password (⚠ Not secure to hardcode!)

sent_from = gmail_user            # Sender email address
to = ['me@gmail.com', 'bill@gmail.com']  # List of recipient email addresses
subject = 'This is my first Python Message'  # Email subject
body = 'Hi, What is going on'     # Email body

try:
    # Create a secure SSL connection to Gmail's SMTP server on port 465
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()  # Identify ourselves to the server

    # Log in to the Gmail account
    server.login(gmail_user, gmail_password)

    # Send the email
    server.sendmail(sent_from, to, body)

    # Close the SMTP connection
    server.close()

    print('Email sent!')  # Success message

except:
    traceback.print_exc()  # Print full error details if something goes wrong
