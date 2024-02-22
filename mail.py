import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_mail(to_emails, subject, html_file_path):
    sendgrid_api_key = os.getenv('SENDGRID_API_KEY')
    # Ensure to_emails is a list of strings
    if isinstance(to_emails, str):
        to_emails = [to_emails]  # Convert a single email address to a list

    # Read HTML content from the file
    try:
        with open(html_file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
    except Exception as e:
        print(f"Failed to read HTML file: {e}")
        return f"Failed to send email: {e}"

    if sendgrid_api_key is None:
        print("SENDGRID_API_KEY environment variable is not set.")
    else:
        message = Mail(
            from_email='stavros8003@gmail.com',
            to_emails=to_emails,
            subject=subject,
            html_content=html_content)
        try:
            sg = SendGridAPIClient(sendgrid_api_key)
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
            return "Email sent successfully"
        except Exception as e:
            print(str(e))
            return "An error occurred while sending email"
