# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

api_key = "***REMOVED***"


def dispatch_mailman(first_name, last_name, email, comments):
    message = Mail(
        from_email='***REMOVED***',
        to_emails='***REMOVED***',
        subject='Sending with Twilio SendGrid is Fun',
        html_content="""Sender: <strong>{} {}</strong> \n
            Email: <strong>{}</strong> \n Message: <strong>{}</strong> \n"""
                .format(first_name, last_name, email, comments))
    try:
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)
