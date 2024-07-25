import os

def relative_path():

        current_dir = os.path.dirname(__file__)

        config = load_config(os.path.join(current_dir,'..','config.json'))

        attachment_path = os.path.join(current_dir, '..', 'cron', 'reports','movies.csv')
        attachment_path= os.path.abspath(attachment_path)


