import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_mail():
    sendgrid_api_key = os.getenv('SENDGRID_API_KEY')
    if sendgrid_api_key is None:
        print("SENDGRID_API_KEY environment variable is not set.")
    else:
        message = Mail(
            from_email='stavros8003@gmail.com',
            to_emails='stavros8003@gmail.com',
            subject='Sending with Twilio SendGrid is Fun',
            html_content='<strong>and easy to do anywhere, even with Python</strong>')
        try:
            sg = SendGridAPIClient(sendgrid_api_key)
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(str(e))
