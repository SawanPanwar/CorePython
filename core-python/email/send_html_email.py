import smtplib, ssl                              # smtplib for sending emails, ssl for secure connection
from email.mime.text import MIMEText             # MIMEText for creating text/HTML parts
from email.mime.multipart import MIMEMultipart   # MIMEMultipart for combining multiple parts into one email

# Sender and receiver email addresses and password
sender = "xyz@gmail.com"                         # Sender Gmail address
receiver = "abc@gmail.com"                       # Receiver email address
password = "PA$$12345"                           # Sender Gmail password or App Password (⚠ avoid hardcoding in real apps)

# Create a multipart/alternative message container (plain text + HTML)
msg = MIMEMultipart("alternative")
msg["Subject"] = "multipart test"                # Email subject
msg["From"] = sender                             # Sender shown in email
msg["To"] = receiver                             # Receiver shown in email

# Create both plain text and HTML parts of the email
plain = MIMEText("Hi,\nHow are you?\nwww.realpython.com", "plain")  # Plain text version
html = MIMEText(
    "<p>Hi,<br>How are you?<br>"
    "<a href='https://www.raystec.com/'>Real Python</a></p>",
    "html"
)  # HTML version

# Attach both versions to the email
msg.attach(plain)
msg.attach(html)

# Connect securely to Gmail SMTP server using SSL on port 465
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender, password)               # Log in to Gmail SMTP server
    server.sendmail(sender, receiver, msg.as_string())  # Send the email
