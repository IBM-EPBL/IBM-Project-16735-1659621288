import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='mmalishwaran2002@gmail.com',
    to_emails='hariharantamilselvan009@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>Tell your skill and Get a job</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('API key'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)