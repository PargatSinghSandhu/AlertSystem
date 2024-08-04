
import os
import requests

from src.utils import get_csv_output_path


def send_email(config, attachment_path):

    '''
    :param config: A dictionary containing the configuration settings
    :param attachment_path: CSV output path from the utils module
    '''

    api_key = os.environ.get('MAILGUN_API_KEY')
    domain = os.environ.get("MAILGUN_DOMAIN")

    url = f"https://api.mailgun.net/v3/{domain}/messages"

    with open(attachment_path, 'rb') as f:
        response = requests.post(
            url,
            auth=("api", api_key),
            files={"attachment": f},
            data={
                "from": config["email"]["sender"],
                "to": config["email"]["recipients"],
                "subject": config["email"]["subject"],
                "text": config["email"]["body"]
            }
        )

    if response.status_code == 200:
        print("Email sent successfully!")
    else:
        print(f"Failed to send email: {response.status_code} - {response.text}")



