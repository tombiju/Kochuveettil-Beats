from flask_sendgrid import SendGrid
app = Flask(__name__)
app.config['SENDGRID_API_KEY'] = 'your api key'
app.config['SENDGRID_DEFAULT_FROM'] = 'admin@yourdomain.com'
mail = SendGrid(app)

# send single recipient; single email as string
mail.send_email(
    from_email='tombiju95@yahoo.com',
    to_email='test@example.com',
    subject='KV Beats Website Message',
    text='testing ............',
)


