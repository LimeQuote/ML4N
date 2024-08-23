"""
Title: Automated Web Search Simulation using Selenium

Description:
This script automates the process of simulating user search behavior across different web browsers 
and websites using Selenium WebDriver. The script reads metadata from a CSV file, which contains 
information such as the browser type, target website, and search query. It then performs the 
search on the specified website, handling dynamic content such as cookies and pop-up dialogs.

Key Features:
- Automates search tasks on popular websites like Google, Bing, and Wikipedia.
- Supports multiple browsers including Google Chrome, Microsoft Edge, and Mozilla Firefox.
- Uses WebDriverWait and expected_conditions to handle dynamic web elements and avoid common 
  issues like StaleElementReferenceException.
- Repeats searches multiple times to generate a large volume of traffic data for analysis.

Author: Shaghayegh Samadzadeh
Date: July 2024
"""

import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Assuming you already have the dataframe:

def simulate_search_with_selenium(row):
    browser = row['browser']
    website = row['website']
    link = row['link']
    behavior = row['behavior']
    query = row['query']

    print(f"{behavior} in the website {website} on the browser '{browser}'")

    # Set up Selenium WebDriver for the specified browser
    if browser == "Chrome":
        driver = webdriver.Chrome()
    elif browser == "Edge":
        driver = webdriver.Edge()
    elif browser == "Firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser type")
    
    try:
        # Open the website
        driver.get(link)
        time.sleep(1)  # Wait for the page to load
        # Define search_box variable to store reference to the search input element
        # Check which website we are currently handling
        # Use WebDriverWait to wait for the search input element to be present
        search_box = None
        if website == "Wikipedia":
            search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "searchInput")))
        elif website == "Bing":
            try:
                # Accept cookies if the button is present
                accept_cookies_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'bnp_btn_accept')))
                accept_cookies_button.click()
            except: 
                pass
            search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q")))
        elif website == "Google":
            try:
                driver.find_element(By.ID, "L2AGLb").click()
            except:
                pass
            search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q")))

        
        if search_box: # If search_box is found, proceed
            search_box.clear()# Clear the search box
            search_box.send_keys(query)# Type the query into the search box
            search_box.send_keys(Keys.RETURN)# Press Enter to perform the search
            time.sleep(2) # Wait for some time to allow the page to load (can be adjusted)

        else:
            print("Search box not found or not interactable.")# Print a message if search_box is not found or not interactable
    except Exception as e:
        print(f"Exception occured: {e}")
    finally:
        driver.quit() # Close the WebDriver session

repetition_id = 100
# Read the CSV file containing browsers, websites, links, and behaviors using pandas
csv_file = "websites_behaviors.csv"
df = pd.read_csv(csv_file)
for index, row in df.iterrows():
    if row['browser'] == "Edge" and row['website'] == "Bing" and row['query'] == "Python" :
        for i in range(repetition_id):
            print(f"repetition {i+1}")
            simulate_search_with_selenium(row)

