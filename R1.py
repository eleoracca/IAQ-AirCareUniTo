#!/usr/bin/env python3
import os
from argparse import ArgumentParser
from bs4 import BeautifulSoup
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.select import Select
import time
import datetime

HTML_CACHE = 'index_R1.html'
TARGET_URL = 'https://unito-fits.harpaitalia.it/login'
R1_CLIENT_NAME = u'CERN Restaurant N°1'
INDENT_CHR='    '

def main(args):
    logging.info('args: %s', args)

    scrape(TARGET_URL)
    return 0


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--log', dest='loglevel', metavar='LEVEL', default='WARNING', help='Level for the python logging module. Can be either a mnemonic string like DEBUG, INFO or WARNING or an integer (lower means more verbose).')

    return parser.parse_args()


def scrape(url, **kwargs):
    opts = Options()
    # opts.page_load_strategy = 'eager'
    # opts.add_argument('--headless')

    with webdriver.Firefox(
        options=opts
    ) as driver:
        driver.get(url)
        # Accesso alla pagina di login
        # Il terminale aspetta che schiacci invio prima di fare cose
        input('Press any key when the browser has loaded the page:')
        
        # Log in manuale alla pagina e spostamento sulla pagina corretta
        
        # --- Scaricamento dati
        # -- Tabella con i dati
        tables = driver.find_elements(By.CLASS_NAME, 'dataTable')
        logging.info("Number tables %d", len(tables))
        
        rows = tables[0].find_elements(By.XPATH, "//body//tbody//tr")
        
        #for row_data in rows:
        #        col = row_data.find_elements(By.TAG_NAME, "td")
        #        for i in range(len(col)):
        #            print(col[i].text)
                    
        # - Selezionamento del sensore
        check = rows[0].find_element(By.CLASS_NAME, 'm-checkbox')
        check.click()
        
        time.sleep(1)
        
        # -- Selezionamento del pulsante per il report
        wrapper = driver.find_element(By.CLASS_NAME, 'dataTables_filter')
        button = wrapper.find_elements(By.CLASS_NAME, 'quick-action-button')
        button[1].click()
        
        time.sleep(1)
        report = driver.find_element(By.CLASS_NAME, 'reportModal')
        
        # - Riempimeto dati per il pop-up del report
        xls = report.find_element(By.XPATH, "//input[@id='xls']/parent::label")
        xls.click()
        
        # - Riempimento titolo
        title = report.find_element(By.ID, 'title')
        title.click()
        title.send_keys('Sensor')
        
        # - Scelta del periodo (MM/DD/YYYY)
        dropdown = report.find_element(By.CLASS_NAME, 'dropdown')
        dropdown.click()
        
        time.sleep(1)
        
        inner = dropdown.find_element(By.CLASS_NAME, 'inner')
        dropdown_menu = inner.find_element(By.CLASS_NAME, 'dropdown-menu')        
        options = dropdown_menu.find_elements(By.CLASS_NAME, 'dropdown-item')
        options[4].click()
        
        pers_period = report.find_element(By.ID, 'pers_period')
        period_from = pers_period.find_element(By.ID, 'period_custom1')
        period_from.click()
        period_from.send_keys('01/22/2025')
        
        period_to = pers_period.find_element(By.ID, 'period_custom2')
        period_to.click()
        period_to.send_keys('01/23/2025')
        
        # -- Download
        download = report.find_element(By.ID, 'downloadButton')
        download.click()
        
        
        input("Attendo - Download")
        
        return


if __name__ == '__main__':
    args = parse_args()
    loglevel = args.loglevel.upper() if not args.loglevel.isdigit() else int(args.loglevel)
    logging.basicConfig(format='%(levelname)s:%(module)s:%(funcName)s: %(message)s', level=loglevel)

    exit(main(args))
