import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
        search_box = None
        # Check which website we are currently handling
        if website == "Wikipedia":
            # Use WebDriverWait to wait for the search input element to be present
            search_box = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "searchInput")))
        elif website == "Bing":
            # Use WebDriverWait to wait for the search input element to be present
            search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q")))
        elif website == "Google":
            #try:
            driver.find_element(By.ID, "L2AGLb").click()
            search_box = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "q")))
            #except:
                # Use WebDriverWait to wait for the search input element to be present
                #search_box = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "q")))

        # If search_box is found, proceed
        if search_box:
            # Clear the search box
            search_box.clear()
            # Type the query into the search box
            search_box.send_keys(query)
            # Press Enter to perform the search
            search_box.send_keys(Keys.RETURN)
            # Wait for some time to allow the page to load (can be adjusted)
            time.sleep(2)
        else:
            # Print a message if search_box is not found or not interactable
            print("Search box not found or not interactable.")
    finally:
        # Close the WebDriver session
        driver.quit()


# Read the CSV file containing browsers, websites, links, and behaviors using pandas
csv_file = "websites_behaviors.csv"
df = pd.read_csv(csv_file)
for index, row in df.iterrows():
    browser = row["browser"]    # Extract browser name from DataFrame row
    website = row["website"]    # Extract website name from DataFrame row
    link = row["link"]          # Extract link from DataFrame row
    behavior = row["behavior"]  # Extract behavior from DataFrame row
    query = row["query"]        # Extract query from DataFrame row
    repetition_id = row["repetition_id"]

repetition_id = row["repetition_id"]
for i in range(repetition_id):
    print(f"repetition {i+1}")
    simulate_search_with_selenium(df.iloc[0])

