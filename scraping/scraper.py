# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Alberto Mecca - a.mecca@unito.it
# Eleonora Racca - e.racca@unito.it
# 
# Script to download UniTo sensor data from AirCare site
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#!/usr/bin/env python3
import os
from argparse import ArgumentParser
from bs4 import BeautifulSoup
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import ElementClickInterceptedException
import time
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

# TODO: ricordarsi che poi bisogna cambiare pagina sistemati i primi 100 sensori

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~ Global variables
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Link of the page
TARGET_URL = 'https://unito-fits.harpaitalia.it/login'
# Vector of last days for the periods to download
DATES = []
# Number of days to download (0 for 1 day, 9 is the maximum number of days with data each 5 minutes)
DAY_NUMBER = 9



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~ Main function
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main(args):
    # Logs
    logging.info('args: %s', args)
    
    # ---- Elapsed time ----
    time_start = time.time()
    
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(" Webscraping to download UniTo AirCare sensors data")
    print(" ")
    
    # ---- Useful dates ----
    print("-------------------------------------------------------------------")
    print(" Creating the array with ending dates for the download period")
    print(" ")
    
    # --- Default dates for the period to be downloaded
    # Today and first day to be downloaded
    date_today = datetime.today().date()
    date_first = date_today - relativedelta(months = 1)
    
    print(f" First day to be downloaded: {date_first}")
    print(f" Last day to be downloaded:  {date_today}")
    
    # --- Changing the default dates, if necessary
    change_date = 'n'
    change_date = input(" Do you wish to change beginning and ending dates? (y/n): ").strip().lower()
    				
    while change_date not in ["y", "n"]:
    		print(" Invalid answer! Insert 'y' to change the dates or 'n' to mantain the default ones.")
    		next_page = input(" Do you wish to change beginning and ending dates? (y/n): ").strip().lower()
    
    if(change_date == 'n'):
    		# Set current date to today
    		date_corrente = date_today
    else:
    		# Changing date for the first date to download
    		date_first_custom = input("Insert new date for first day to be downloaded: (YYYY-MM-DD): ").strip()
    		try:
    				date_first = datetime.strptime(date_first_custom, "%Y-%m-%d").date()
    		except ValueError:
    				print("Format not valid, keeping original date.")
    				
    		# Changing date for the last date to download
    		date_last_custom = input("Insert new date for last day to be downloaded: (YYYY-MM-DD): ").strip()
    		try:
    				date_today = datetime.strptime(date_last_custom, "%Y-%m-%d").date()
    		except ValueError:
    				print("Format not valid, keeping original date.")
    				
    		# Set current date to today
    		date_corrente = date_today
    
    # Loop to get the ending dates of the periods to download
    while date_corrente >= date_first:
    		DATES.append(date_corrente)
    		date_corrente -= timedelta(days = DAY_NUMBER + 1)
    		
    #for data in DATES:
    #		print(data.strftime("%d/%m/%Y"))
    
    print("")
    print(f" Please, keep in mind that the first day to be downloaded may vary \nbetween the date chosen and {DAY_NUMBER} days before.")
    print(" The final day to be saved is the chosen one as errors may occour \nif the date is in the future.")
    print(" This is because the script saves a costant number of days starting \nfrom the end date. Sorry for the inconvenience.")
    
    # ---- Site scraping ----
    print(" ")
    print("-------------------------------------------------------------------")
    print(" Scraping")
    print(" ")
    
    # Scrape function
    scrape()
    
    # ---- Elapsed time ----
    time_end = time.time()
    time_duration = time_end - time_start
    
    # Printing
    time_start_dt = datetime.fromtimestamp(time_start)
    time_end_dt = datetime.fromtimestamp(time_end)
    
    time_begin_readable = time_start_dt.strftime("%Y-%m-%d %H:%M:%S")
    time_end_readable = time_end_dt.strftime("%Y-%m-%d %H:%M:%S")
    time_duration_readable = str(timedelta(seconds = time_duration))
    
    print(" ")
    print("-------------------------------------------------------------------")
    print(f" Begin time:   {time_begin_readable}")
    print(f" End time:     {time_end_readable}")
    print(f" Elapsed time: {time_duration_readable}")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    return 0
    
    

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~ Website scraper
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def scrape():
    # Open Firefox
    with webdriver.Firefox() as driver:
    		# ---- Going to the correct webpage ----
    		# Go to url page
    		driver.get(TARGET_URL)
    		
    		# Manual login (to avoid further troubles) and proceed to correct page where it is possible to download the data
    		print(" - Please, log in to the website and go to the Inventory page with the \n   left sidebar.")
    		print(" - Remember to change the default download folder of the browser through \n   the browser setting to save the files in the scraping subfolder.")
    		print(" - To optimise the download for the greatest number of sensors, remember \n   to set the page to 50 sensors and minimise the zoom in the page.")
    		print(" - Remember to put the sensors in alphabetical order by sensor name to \n   download correctly all the sensors. The platform orders them\n   by last measure received and therefore the order is randomised each time you change the page.")
    		input(" Press any key when the browser has loaded the Inventory page and\n you are ready to start the web-scraping...")
    		
    		# ---- Downloading data ----
    		# --- Loop on all the pages including sensors
    		next_page = "y"
    		
    		while next_page == "y":
    				# --- Table with sensors
    				tables = driver.find_elements(By.CLASS_NAME, 'dataTable')
    				logging.info("Number tables %d", len(tables))
    		
    				# Rows with the sensors information
    				rows = tables[0].find_elements(By.XPATH, "//body//tbody//tr")
    		
    				# --- For each sensor, download the desired period data
    				for row_sensor in rows:
    						# - Function to download the data in the entire period
    						select_sensor(driver, row_sensor)
    				
    				# --- Go to the next page with sensor data
    				print(" Please, go to the next page to continue the download before answering the following question.")
    				print(" If this is the last page, answer 'n'.")
    				next_page = input(" Shall I proceed with the dowload? (y/n): ").strip().lower()
    				
    				while next_page not in ["y", "n"]:
    						print(" Invalid answer! Insert 'y' to continue or 'n' to finish.")
    						next_page = input(" Shall I proceed with the dowload? (y/n): ").strip().lower()
    
    print(" ")
    print(" The download ended. Thank you very much for your patience!")
    

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~ Function to loop on the dates
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def select_sensor(driver, row):
    # -- Get sensor name
    row_cols = row.find_elements(By.TAG_NAME, "td")
    name_sensor = row_cols[3].text.replace("/", "-")
    print(" Downloading data for sensor: " + name_sensor)
    
    # -- Select the sensor
    check = row.find_element(By.CLASS_NAME, 'm-checkbox')
    check.click()
    time.sleep(1)
    
    # - Loop to download the data for the entire period
    for day in DATES:
        # For each sub-period, download the data:
        download_data(driver, day, name_sensor)

    # -- At the end of the period, the sensor must be deselected
    checked_button = False
    while(not checked_button):
        try:
	          check.click() # report is the second (-> 1) button
	          checked_button = True
        except ElementClickInterceptedException:
	          logging.debug("ElementClickInterceptedException")
	          time.sleep(1)
    time.sleep(1)
    
    

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~ Function to download the data in a specific period
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def download_data(driver, day_end, name_sensor):
    # -- Period of the data to download
    # Final day in the period
    endtime_site = day_end.strftime("%m/%d/%Y")
    endtime_file = day_end.strftime("%Y-%m-%d")
    
    # First day in the period
    day_start = day_end - timedelta(days = DAY_NUMBER)
    begintime_site = day_start.strftime("%m/%d/%Y")
    begintime_file = day_start.strftime("%Y-%m-%d")
    
    #logging.debug("start = %s (%s) - end = %s (%s)", start, start_str, end, end_str)

    # -- Report pop up
    # - Select report button (report is useful to download the data)
    time.sleep(1)
    wrapper = driver.find_element(By.CLASS_NAME, 'dataTables_filter')
    buttons = wrapper.find_elements(By.CLASS_NAME, 'quick-action-button')
    clicked_button = False
    while(not clicked_button):
        try:
	          buttons[1].click() # report is the second (-> 1) button
	          clicked_button = True
        except ElementClickInterceptedException:
	          logging.debug("ElementClickInterceptedException")
	          time.sleep(1)

    time.sleep(1)
    
    report = driver.find_element(By.CLASS_NAME, 'reportModal')
        
    # - Filling the pop-up to download the data correctly
    # Select xls type of file
    xls = report.find_element(By.XPATH, "//input[@id='xls']/parent::label")
    xls.click()
    
    # Name of the file
    title = report.find_element(By.ID, 'title')
    title.click()
    title.send_keys(name_sensor + "_" + begintime_file  + "_" + endtime_file)
    
    # Filling the period form
    dropdown = report.find_element(By.CLASS_NAME, 'dropdown')
    dropdown.click()    
    time.sleep(1)
    
    inner = dropdown.find_element(By.CLASS_NAME, 'inner')
    dropdown_menu = inner.find_element(By.CLASS_NAME, 'dropdown-menu')        
    options = dropdown_menu.find_elements(By.CLASS_NAME, 'dropdown-item')
    options[4].click() # Custom period is the fifth (-> 4) option
    
    pers_period = report.find_element(By.ID, 'pers_period')
    period_from = pers_period.find_element(By.ID, 'period_custom1') # first day
    period_from.click()
    period_from.send_keys(begintime_site)
    
    period_to = pers_period.find_element(By.ID, 'period_custom2') # last day
    period_to.click()
    period_to.send_keys(endtime_site)
    
    # -- Download
    download = report.find_element(By.ID, 'downloadButton')
    download.click()
    
    time.sleep(3)
    
    return
    
    

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~ Parser for arguments
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def parse_args():
    parser = ArgumentParser(description = "Script to download data from AirCare platform.")
    parser.add_argument('--log', dest='loglevel', metavar='LEVEL', default='WARNING', help='Level for the python logging module. Can be either a mnemonic string like DEBUG, INFO or WARNING or an integer (lower means more verbose).')

    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    loglevel = args.loglevel.upper() if not args.loglevel.isdigit() else int(args.loglevel)
    logging.basicConfig(format='%(levelname)s:%(module)s:%(funcName)s: %(message)s', level=loglevel)

    exit(main(args))
