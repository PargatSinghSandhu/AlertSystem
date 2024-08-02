import base64

import mysql.connector
import os
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content, Attachment, FileName, FileType, Disposition
from sendgrid import FileContent
from src.utils import get_csv_output_path


def send_email(config, attachment_path):

    '''
    :param config: A dictionary containing the configuration settings
    :param attachment_path: CSV output path from the utils module
    '''

    with open(attachment_path, 'rb') as f:
        file_data = f.read()

    sg= sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    from_email =Email(config["email"]["sender"])
    to_email = To(config["email"]["recipients"][0])
    subject=config["email"]["subject"]
    content = Content("text/plain", config["email"]["body"])
    mail = Mail(from_email, to_email, subject, content)

    encoded_file = base64.b64encode(file_data).decode()
    attachment = Attachment()
    attachment.file_content = FileContent(encoded_file)
    attachment.file_name = FileName(os.path.basename(attachment_path))
    attachment.disposition = Disposition('attachment')

    mail.attachment = attachment

    #send the email
    response = sg.client.mail.send.post(request_body = mail.get())



