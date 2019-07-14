# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

api_key = "***REMOVED***"
emails = [***REMOVED***]


def dispatch_mailman(first_name, last_name, email, comments):
    message = Mail(
        from_email='***REMOVED***',
        to_emails=emails
        subject='Sending with Twilio SendGrid is Fun',
        html_content="""Sender: <strong>{} {}</strong> <br/>
            Email: <strong>{}</strong> <br/>
            Message: <strong>{}</strong> <br/> """
                .format(first_name, last_name, email, comments))
    try:
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)