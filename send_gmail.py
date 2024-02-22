import os.path
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/gmail.send']


def login():
    """Log in to the Google API and save the session for future use."""
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds


def create_message(sender, to, subject, message_html):
    """Create a message for an email."""
    message = MIMEMultipart('alternative')
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    part = MIMEText(message_html, 'html')
    message.attach(part)
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw_message}


def send_email(service, user_id, message):
    """Send an email message."""
    try:
        message = (service.users().messages().send(userId=user_id, body=message).execute())
        print(f'Message Id: {message["id"]}')
    except HttpError as error:
        print(f'An error occurred: {error}')


def send_gmail(emails, subject, file_path):
    creds = login()
    service = build('gmail', 'v1', credentials=creds)
    sender = 'stavros8003@gmail.com'  # Make sure this is the email associated with your Google account

    try:
        # Read the HTML content from the file
        with open(file_path, 'r', encoding='utf-8') as file:
            message_html = file.read()

        for to in emails:
            message = create_message(sender, to, subject, message_html)
            send_email(service, 'me', message)

        return "Email sent successfully."

    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except HttpError as error:
        print(f"An error occurred: {error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

