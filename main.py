from src.fetch_data import fetch_data
from src.send_email import send_email
import os
import json

#loading config file
def load_config(config_file): # loading the config file
    with open (config_file, 'r') as file:
        config = json.load(file)
    return config


def main():

    fetch_data();
    send_email();

if __name__ == "__main__": #the program will only run when the script is executed directly , and not when it
    #is imported as a module into another script
    main()

    #if I run main directly so the __name__ will be main
    #and if I import main let's say file name is pop, into anotherscript, then
    #__name__ will bepop