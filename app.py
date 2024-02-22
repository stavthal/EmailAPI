from flask import Flask
from mail import send_mail
from send_gmail import send_gmail

app = Flask(__name__)

# An array of emails (strings seperated by comma) to send out your emails.
emails = ['<EMAIL>', '<EMAIL>']

# Filepaths for html templates
welcome_email_path = 'static/OKTO RO HTML (With Cards and Deep Links)/Welcome email (only registration) - RO.html'
welcome_email_direct_verification_level_1_path = 'static/OKTO RO HTML (With Cards and Deep Links)/Welcome email direct verification level 1 - RO.html'
reminder_email_for_verification_path = 'static/OKTO RO HTML (With Cards and Deep Links)/Reminder email for verification - RO.html'
confirmation_level_2_path= 'static/OKTO RO HTML (With Cards and Deep Links)/Confirmation of verification (level2) - RO.html'
confirmation_level_1_path = 'static/OKTO RO HTML (With Cards and Deep Links)/Confirmation of verification (level1) - RO.html'


# Defined example routes for sending out the mails
@app.route('/send-welcome-email')
def index():
    return send_gmail(emails, 'Test Welcome Email', welcome_email_path )
@app.route('/send-welcome-email-direct-verification')
def direct_verification():
    return send_gmail(emails, 'Test Welcome Email (Direct Verification Level 1)',
                     welcome_email_direct_verification_level_1_path)

@app.route('/send-reminder-email')
def reminder_email():
    return send_gmail(emails, 'Test Reminder Email', reminder_email_for_verification_path)

@app.route('/send-confirmation-email-level-1')
def confirmation_level_1():
    return send_gmail(emails, 'Test Confirmation Level 1', confirmation_level_1_path)

@app.route('/send-confirmation-email-level-2')
def confirmation_level_2():
    return send_gmail(emails, 'Test Confirmation Level 2', confirmation_level_2_path)


# You can always toggle the debug to off
if __name__ == '__main__':
    app.run(debug=True)

