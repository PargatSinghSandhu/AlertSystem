from src.fetch_data import fetch_data
from src.send_email import send_email
from src.utils import get_csv_output_path
import os
import json

#loading config file
def load_config(config_file): # loading the config file
    with open (config_file, 'r') as file:
        config = json.load(file)
    return config #this will return the config file as a dictionary


def main():
    #laod the configuration file
    current_dir = os.path.dirname(__file__)
    config_path = os.path.join(current_dir, 'config.json')
    config = load_config(config_path)

    #Fetch the data and write to CSV file
    start_ID = config["queries"]["start_ID"]
    end_ID = config["queries"]["end_ID"]
    fetch_data(config, start_ID, end_ID)

    #Send email with the attached CSV
    csv_output_path = get_csv_output_path(config["output"]["csv_output_path"])
    send_email(config, csv_output_path)


if __name__ == "__main__": #the program will only run when the script is executed directly , and not when it
    #is imported as a module into another script
    main()

    #if I run main directly so the __name__ will be main
    #and if I import main let's say file name is pop, into anotherscript, then
    #__name__ will bepop