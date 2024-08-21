from src.fetch_data import fetch_data
from src.send_email import send_email
from src.utils import get_csv_output_path
import csv
import mysql.connector
from mysql.connector import connect
from concurrent.futures import ThreadPoolExecutor, as_completed
import os
import json


#loading config file
def load_config(config_file): # loading the config file
    with open (config_file, 'r') as file:
        config = json.load(file)
    return config #this will return the config file as a dictionary

def process_country(config, country, donation_plans, start_date, end_date):
    csv_output_path = fetch_data(config, country, donation_plans, start_date, end_date)
    return csv_output_path

def main():
    #laod the configuration file
    current_dir = os.path.dirname(__file__)
    config_path = os.path.join(current_dir, 'config.json')
    config = load_config(config_path)

    #Fetch the data and write to CSV file
    config['database']['password'] = os.getenv('DB_PASSWORD', config['database']['password'])

    #extracting parameters
    start_date= config['reportConfig']['dateRange']['start_date']
    end_date=config['reportConfig']['dateRange']['end_date'] #here we accesing the json value
    countries=config['reportConfig']['countries']
    donation_plans=config['reportConfig']['donationPlans']

    num_threads = len(countries) if len(countries)> 0 else 1

    with ThreadPoolExecutor(max_workers = num_threads) as executor:
        futures = {
            executor.submit(process_country, config,country, donation_plans, start_date, end_date):country
            for country in countries
        }

        for future in as_completed(futures):
            try:
                csv_output_path = future.result()
                #email sending tasks
                executor.submit(send_email, config, csv_output_path)
            except Exception as e:
                print(f"An error occured: {e}")

if __name__ == "__main__": #the program will only run when the script is executed directly , and not when it
    #is imported as a module into another script
    main()

    #if I run main directly so the __name__ will be main
    #and if I import main let's say file name is pop, into anotherscript, then
    #__name__ will bepop