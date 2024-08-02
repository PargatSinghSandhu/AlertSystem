import os

def get_csv_output_path(relative_path):
    '''

    :param relative_path: The relative path for the csv.
    :return: The absolute path for the csv file.
    '''

    current_dir = os.path.dirname(__file__)
    full_path = os.path.join(current_dir, '..', relative_path)
    return os.path.abspath(full_path) #return the absolute path