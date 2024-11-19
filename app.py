
from flask import Flask, request, render_template, redirect, url_for
import pandas as pd
import smtplib
from email.mime.text import MIMEText
import os
import time
from datetime import datetime
import signal
import sys

app = Flask(__name__)

# Global variable to store log file name
log_file_name = f'email_log_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt'

# Function to send email
def send_email(to_email, business_name, email_template):
    smtp_server = 'globaldigitsolutions.com'
    smtp_port = 465
    sender_email = 'smtptest@globaldigitsolutions.com'  # Replace with your email
    sender_password = 'X;A8m.,kzOon'  # Replace with your email password

    subject = "Freelance Recruitment Application"
    body = email_template.replace("{business_name}", business_name)

    msg = MIMEText(body, 'html')
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = to_email

    try:
        server = smtplib.SMTP_SSL(smtp_server, smtp_port) 
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())
        server.quit()
        print(f"Email sent to {to_email}")
        log_email_status(to_email, "Successfully sent")
        return True
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")
        log_email_status(to_email, f"Failed to send: {e}")
        return False

def log_email_status(email, status):
    with open(log_file_name, 'a') as log_file:
        log_file.write(f"{datetime.now()} - {email} - {status}\n")

def signal_handler(sig, frame):
    print("Exiting the program. Log file created:", log_file_name)
    sys.exit(0)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the uploaded file and email template
        file = request.files['file']
        email_template = request.form['template']
        
        if file:
            # Read the data from the uploaded Excel file
            try:
                df = pd.read_excel(file)
                df.columns = df.columns.str.strip()  # Remove leading/trailing spaces
                
                # Print the column names for debugging
                print("Columns in the uploaded file:", df.columns.tolist())
                
                # Check if required columns exist
                if 'Email' not in df.columns or 'Business Name' not in df.columns:
                    return "Error: Required columns 'Email' and 'Business Name' are missing from the uploaded file."
                
                for index, row in df.iterrows():
                    email = row['Email']
                    business_name = row['Business Name']
                    send_email(email, business_name, email_template)
                    time.sleep(5)  # Pause for 5 seconds between emails
                return redirect(url_for('success'))
            except Exception as e:
                return f"Error reading the Excel file: {e}"
    return render_template('index.html')

@app.route('/success')
def success():
    return "Emails sent successfully!"

if __name__ == '__main__':
    # Register the signal handler for graceful exit
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    # Create uploads directory if it doesn't exist
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    
    app.run(debug=True)