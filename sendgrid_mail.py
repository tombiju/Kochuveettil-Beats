# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os

api_key = os.environ['SENDGRID_API_KEY']
emails = os.environ['RECIPIENT_EMAILS'].split(",")


def dispatch_mailman(first_name, last_name, email, message_body):
    message = Mail(
        from_email=os.environ['SENDER_EMAIL'],
        to_emails=emails,
        subject='KV Beats Website Message!',
        html_content="""Sender: <strong>{} {}</strong> <br/>
            Email: <strong>{}</strong> <br/>
            Message: <strong>{}</strong> <br/> """
                .format(first_name, last_name, email, message_body))
    try:
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)
