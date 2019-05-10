from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
import configparser, requests

app = Flask(__name__)
config = configparser.ConfigParser()
config.read('config.ini')
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,  # 465 for SSL, 587 for TLS
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": config['email']['username'],
    "MAIL_PASSWORD": config['email']['password']
}
app.config.update(mail_settings)
mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
# def send_email():
    # first_name =  request.form.get('first_name')
    # last_name = request.form.get('last_name')
    # email = request.form.get('email')
    # comments = request.form.get('comments')
    # text = "Sender: {} {} \n Email: {} \n Message: {} \n".format(first_name, last_name, email, comments)
    # if None not in [first_name, last_name, email, comments]:
    #     with app.app_context():
    #         msg = Message(subject="KV Beats Website Message",
    #                     sender=app.config.get("MAIL_USERNAME"),
    #                     recipients=["<***REMOVED***>"], # replace with your email for testing
    #                     body=text)
    #         mail.send(msg)
    # return redirect("/")
def send_email():
    requests.post(
        "https://api.mailgun.net/v3/sandboxa2de269106534839a8c7be8d4137316d.mailgun.org/messages",
        auth=("api", "ab3950059524177b51c95f68b5ce1c78-7bce17e5-ccd1a7d5"),
        data={"from": "Mailgun Sandbox <postmaster@sandboxa2de269106534839a8c7be8d4137316d.mailgun.org>",
              "to": "Tom Biju <***REMOVED***>",
              "subject": "New Inquiry",
              "text": "Congratulations Tom Biju, you just sent an email with Mailgun!  You are truly awesome!"})
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)