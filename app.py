import urllib.request as urllib2
from flask import Flask, render_template, request, redirect
from sendgrid_mail import dispatch_mailman
# email.py renamed to sendgrid_mail.py due to library conflict

app = Flask(__name__)


@app.before_request
def redirect_to_primary_domain():
    # Get the current host (domain)
    host = request.host
    
    # List of domains to redirect to kvbeats.com
    redirect_domains = ['kochuveettilbeats.com', 'www.kochuveettilbeats.com',
                        'kochuveetilbeats.com', 'www.kochuveetilbeats.com']
    
    # If the host is in the redirect list, perform the 301 redirect
    if host in redirect_domains:
        return redirect(f"https://kvbeats.com{request.path}", code=301)


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
