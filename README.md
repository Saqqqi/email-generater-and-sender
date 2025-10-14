# Email Generator and Sender

An automated email generation and sending application built with Flask that allows users to send personalized emails to multiple recipients using Excel data files.

## Table of Contents
- [Technologies Used](#technologies-used)
- [How It Works](#how-it-works)
- [Project Complexity and Uniqueness](#project-complexity-and-uniqueness)
- [Code Interaction](#code-interaction)
- [Setup and Installation](#setup-and-installation)
- [Usage Instructions](#usage-instructions)
- [Deployment](#deployment)
- [Logging](#logging)
- [License](#license)

## Technologies Used

### Core Technologies
- **Python 3.x**: Primary programming language
- **Flask**: Lightweight web framework for handling HTTP requests and rendering templates
- **pandas**: Data manipulation library for processing Excel files
- **smtplib**: Built-in Python library for sending emails via SMTP
- **HTML/CSS**: Frontend templating and styling

### Dependencies
- `Flask`: Web framework for routing and template rendering
- `pandas`: Data processing for Excel file handling
- `openpyxl`: Engine for reading Excel files (.xlsx format)

These technologies were chosen for their reliability, ease of use, and suitability for the task:
- Flask provides a simple yet powerful foundation for web applications
- Pandas offers robust data handling capabilities for Excel files
- SMTP ensures reliable email delivery
- HTML/CSS provides a clean, customizable user interface

## How It Works

1. **User Interface**: The application presents a web form where users can:
   - Input an HTML email template with placeholders
   - Upload an Excel file containing recipient data

2. **Data Processing**: 
   - The application reads the uploaded Excel file using pandas
   - Validates that required columns ('Email' and 'Business Name') exist
   - Processes each row to extract recipient information

3. **Email Generation**:
   - Replaces placeholders in the email template with actual data
   - Constructs MIME-compliant HTML emails with proper headers

4. **Email Sending**:
   - Connects to an SMTP server using SSL encryption
   - Authenticates with predefined credentials
   - Sends personalized emails to each recipient with a 5-second delay between emails

5. **Logging**:
   - Records the status of each email (success/failure) with timestamps
   - Creates timestamped log files for tracking email delivery

## Project Complexity and Uniqueness

### Key Features
- **Batch Email Processing**: Handles multiple recipients from Excel data
- **Template Customization**: Supports HTML email templates with dynamic placeholders
- **Rate Limiting**: Implements delays between emails to prevent server throttling
- **Comprehensive Logging**: Tracks email delivery status for auditing
- **Graceful Error Handling**: Manages SMTP connection issues and data validation
- **Cross-platform Compatibility**: Runs on Windows via batch script

### Unique Aspects
- **Dynamic Placeholder Replacement**: Automatically replaces `{business_name}` in templates
- **Real-time Status Updates**: Provides immediate feedback on email delivery
- **Signal Handling**: Properly handles application termination to preserve logs
- **Production-ready Structure**: Includes deployment configuration for Vercel

## Code Interaction

### Main Components
1. **[app.py](file:///c:/Users/Saqlain/Downloads/email-generater-and-sender-master/email-generater-and-sender-master/app.py)**: Core application logic
   - Flask routes for handling web requests
   - Email sending functionality via SMTP
   - Excel file processing with pandas
   - Logging mechanisms

2. **[templates/index.html](file:///c:/Users/Saqlain/Downloads/email-generater-and-sender-master/email-generater-and-sender-master/templates/index.html)**: User interface
   - HTML form for uploading files and entering templates
   - CSS styling for a professional appearance

3. **[requirements.txt](file:///c:/Users/Saqlain/Downloads/email-generater-and-sender-master/email-generater-and-sender-master/requirements.txt)**: Dependency management
   - Lists all required Python packages

4. **[server.bat](file:///c:/Users/Saqlain/Downloads/email-generater-and-sender-master/email-generater-and-sender-master/server.bat)**: Startup script
   - Automates application launch on Windows systems

5. **Log Files**: Email delivery tracking
   - Real-time recording of email statuses
   - Timestamped filenames for historical tracking

### Data Flow
```
User Input → Flask App → Excel Processing → Email Generation → SMTP Server → Recipients
     ↑                                            ↓
     ←←←←←←←←←←←←←←←←←← Logging ←←←←←←←←←←←←←←←←←←←
```

## Setup and Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone or Download the Repository**
   ```bash
   git clone <repository-url>
   cd email-generater-and-sender-master
   ```

2. **Create a Virtual Environment (Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure SMTP Settings**
   In [app.py](file:///c:/Users/Saqlain/Downloads/email-generater-and-sender-master/email-generater-and-sender-master/app.py), update the following variables with your SMTP credentials:
   ```python
   smtp_server = 'your-smtp-server.com'
   smtp_port = 465  # or 587 for TLS
   sender_email = 'your-email@example.com'
   sender_password = 'your-app-password'
   ```

### Excel File Format
Prepare your Excel file with these required column headers:
- `Email`: Recipient email addresses
- `Business Name`: Names to be used in the email template

Example:
| Email                 | Business Name     |
|-----------------------|-------------------|
| john@example.com      | John's Bakery     |
| sarah@example.com     | Sarah's Cafe      |

## Usage Instructions

### Starting the Application

#### Method 1: Using the Batch Script (Windows)
1. Double-click [server.bat](file:///c:/Users/Saqlain/Downloads/email-generater-and-sender-master/email-generater-and-sender-master/server.bat) to start the application
2. The default browser will automatically open to `http://127.0.0.1:5000`

#### Method 2: Manual Start
```bash
python app.py
```
Then navigate to `http://127.0.0.1:5000` in your browser

### Sending Emails

1. **Access the Web Interface**
   Open your browser and go to `http://127.0.0.1:5000`

2. **Create an Email Template**
   Write your HTML email template in the text area. Use `{business_name}` as a placeholder for personalization.
   
   Example template:
   ```html
   <p>Hello {business_name},</p>
   <p>I hope this email finds you well. I'm reaching out to discuss...</p>
   ```

3. **Upload Excel File**
   Click "Choose File" and select your properly formatted Excel file

4. **Send Emails**
   Click the "Send Emails" button to begin the batch sending process

5. **View Results**
   - Success page will confirm when emails are sent
   - Check log files for detailed delivery status

### Graceful Shutdown
Press `Ctrl+C` in the terminal to properly shut down the application. This ensures all logs are saved.

## Deployment

### Vercel Deployment
The project includes a [vercel.json](file:///c:/Users/Saqlain/Downloads/email-generater-and-sender-master/email-generater-and-sender-master/vercel.json) configuration file for easy deployment to Vercel:
- Uses the official Python runtime
- Routes all requests to the main application file

### Environment Variables
For production deployments, it's recommended to use environment variables for sensitive data:
- SMTP_SERVER
- SMTP_PORT
- SENDER_EMAIL
- SENDER_PASSWORD

## Logging

The application creates two types of log files:

1. **Generic Log**: [email_log.txt](file:///c:/Users/Saqlain/Downloads/email-generater-and-sender-master/email-generater-and-sender-master/email_log.txt) - Continuously updated with latest entries
2. **Timestamped Logs**: `email_log_YYYYMMDD_HHMMSS.txt` - Created for each application session

Each log entry includes:
- Timestamp of the email attempt
- Recipient email address
- Delivery status (Success/Failure with error details)

Example log entry:
```
2024-11-19 08:55:31.164264 - user@example.com - Successfully sent
```

## License

This project is proprietary software developed for business email automation purposes. All rights reserved.
