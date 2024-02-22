Hello and welcome the my Project.

This is a project that I made to help me in my daily tasks, which include editing email templates and sending them out.
So I believe that this can help others trying to test mails like I do.

The API features two services that can be used to send mails:
* SendGrid
* Gmail API

_You can set up both, or just one of them. If you are a beginner, I would strongly suggest going with SendGrid first_.

#### **What you will need for the project to run:**
* Python
* a Google Cloud Project (Optional)
* SendGrid API key (Optional)
* pip
* Flask

The Cloud Project will need a different configuration for each one and there should also be three files present.

* credentials.json 
* client_secret.json
* token.json


These two files will also be needed if you want both services to work, containing the environmental variables

* sendgrid.env
* gmail.env


In the static folder, I have placed the templates that I want to use, and in the app.py I am setting the variables the file paths, in order to send them by triggering each route responsible for the specific mail.


If you run into any problems, you should probably check the Google Cloud docs, for Python specifically in order to troubleshoot any issues that are presented.

I will update this in the future if extra instructions are needed.

# Setup:

### SendGrid:
You should follow the instructions from their website as they are very straightforward, and I don't believe that I need to analyze them further.

### Gmail:
After you setup your Google Cloud Project and you have followed the instructions on the official documentation you can follow these steps. What you should have done after following the official documentation is:

1. Have setup the google environment variable.
2. Having setup a service account and downloaded the JSON.
3. Having setup a Oauth 2 Client ID.
4. Have authenticated with Google Cloud.
5. Created token.json through the authentication process.


You will need to run setup_gmail.py once you have the token.json, credentials.json and client_secret.json in order to check that everything works.

```Python
    python setup_gmail.py
```

You should expect an output of your google mail's labels.


#### Please keep in mind that there will probably be required extra effort to make it run with Gmail


### Helpful links:
For SendGrid:
* https://app.sendgrid.com/

For Gmail API:
* https://developers.google.com/gmail/api/quickstart/python
* https://developers.google.com/gmail/api/guides
* https://developers.google.com/gmail/api/reference/rest