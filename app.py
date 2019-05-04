from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
import configparser

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
def send_email():
    first_name =  request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    comments = request.form.get('comments')
    text = "Sender: {} {} \n Email: {} \n Message: {} \n".format(first_name, last_name, email, comments)
    if None not in [first_name, last_name, email, comments]:
        with app.app_context():
            msg = Message(subject="KV Beats Website Message",
                        sender=app.config.get("MAIL_USERNAME"),
                        recipients=["<Kochuveettilbeats@gmail.com>"], # replace with your email for testing
                        body=text)
            mail.send(msg)
    return redirect("www.kvbeats.com")

if __name__ == '__main__':
    app.run(debug=True)