import urllib.request as urllib2
from flask import Flask, render_template, request, redirect
from sendgrid_mail import dispatch_mailman
# email.py renamed to sendgrid_mail.py due to library conflict

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send_email', methods=['POST'])
def send_email():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    comments = request.form.get('comments')
    if None not in [first_name, last_name, email, comments]:
        dispatch_mailman(first_name, last_name, email, comments)
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)  # True only for development
