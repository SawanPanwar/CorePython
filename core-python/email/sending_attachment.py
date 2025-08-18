import smtplib                                  # For sending email using SMTP protocol
from email.mime.multipart import MIMEMultipart  # For creating multipart email (text + attachment)
from email.mime.text import MIMEText            # For adding plain text/HTML body
from email.mime.base import MIMEBase            # For adding attachments (binary data)
from email import encoders                      # For encoding attachment in base64

# Sender and receiver email addresses
fromaddr = "jacksonbuddy17@gmail.com"
toaddr = "jacksonbuddy17@gmail.com"

# Create MIMEMultipart object to hold all parts of the email
msg = MIMEMultipart()

# Set sender's email address
msg['From'] = fromaddr

# Set receiver's email address
msg['To'] = toaddr

# Set email subject
msg['Subject'] = "This is the Document Attachted"

# Body of the email
body = "Below is the Attachment"

# Attach the body to the email as plain text
msg.attach(MIMEText(body, 'plain'))

# File name to appear in the attachment
filename = "File_name_with_extension"

# Open the file to be sent in binary read mode
attachment = open("Document.txt", "rb")

# Create MIMEBase object for binary attachment
p = MIMEBase('application', 'octet-stream')

# Load the file content into payload
p.set_payload((attachment).read())

# Encode the payload in base64 so it can be sent as email data
encoders.encode_base64(p)

# Add header to indicate attachment and filename
p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# Attach the file object to the email message
msg.attach(p)

# Create SMTP session (connecting to Gmail's SMTP server on port 587)
s = smtplib.SMTP('smtp.gmail.com', 587)

# Start TLS encryption for secure communication
s.starttls()

# Login to the email account
s.login(fromaddr, "sender_password")

# Convert the MIMEMultipart message into a string format for sending
text = msg.as_string()

# Send the email from sender to receiver
s.sendmail(fromaddr, toaddr, text)

# Terminate the SMTP session
s.quit()