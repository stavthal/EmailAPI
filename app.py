from flask import Flask
from mail import send_mail

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return send_mail()


if __name__ == '__main__':
    app.run()
