# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Edge WebDriver with specified options
driver = webdriver.Edge()

# Read the CSV file containing websites, links, and behaviors using pandas
csv_file = "websites_behaviors.csv"
df = pd.read_csv(csv_file)

# Iterate over the rows of the DataFrame
for index, row in df.iterrows():
    website = row["website"]  # Extract website name from DataFrame row
    link = row["link"]        # Extract link from DataFrame row
    behavior = row["behavior"]  # Extract behavior from DataFrame row
    query = row["query"]        # Extract query from DataFrame row

    # Open the link in Edge, Navigate to the link provided by df
    driver.get(link)

    # Print information about the current search being performed
    print(f"{index + 1}) Searching for {query} on {website}")

    # Define search_box variable to store reference to the search input element
    search_box = None

    # Check which website we are currently handling
    if website == "Wikipedia":
        # Use WebDriverWait to wait for the search input element to be present
        search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "searchInput")))
    elif website == "Bing":
        # Use WebDriverWait to wait for the search input element to be present
        search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "sb_form_q")))
    elif website == "Google":
        # If it's Google, handle special cases
        if query == "Machine Learning":  # Special case for the first query
            # Click the "Accept All" button if it appears
            driver.find_element(By.ID, "L2AGLb").click()
        # Use WebDriverWait to wait for the search input element to be present
        search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q")))

    # If search_box is found, proceed
    if search_box:
        # Clear the search box
        search_box.clear()
        # Type the query into the search box
        search_box.send_keys(query)
        # Press Enter to perform the search
        search_box.send_keys(Keys.RETURN)
        # Wait for some time to allow the page to load (can be adjusted)
        time.sleep(3)
    else:
        # Print a message if search_box is not found or not interactable
        print("Search box not found or not interactable.")
