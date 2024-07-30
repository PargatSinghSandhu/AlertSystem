import mysql.connector
import os
import sendgrid
import sendgrid.helpers.mail import Mail, Email, To, Content


def send_email():

    current_dir = os.pathname.dirname(file)
    attachment_path= os.path.join(current_dir, '..','Reports','reports.csv')
    attachment_path = os.path.abspath(attachment_path)


    sg= sendgrid.SendGridAPIClient(api_key=os.environ.get('SEND_API_KEY'))
    from_email = Email("sandhu.pargat@gmail.com")
    to_email=To("harpreet")
    subject = "Sending with SendGrid is fun"
    content = Content("text/plain","reports")
    mail = Mail(from_email, to_email, subject, content)

    mail_json = mail.get();

    response = sg.client.mail.send.post(request_body = mail_json)
    print(response.status_code)
    print(response.headers)




