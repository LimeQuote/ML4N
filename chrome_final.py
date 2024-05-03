import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options
import pandas as pd

# Set Chrome options to disable pop-ups and notifications
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")

# Initialize Chrome WebDriver with specified options
driver = webdriver.Chrome(options=chrome_options)

# Read the CSV file containing websites, links, and behaviors using pandas
csv_file = "websites_behaviors.csv"
df = pd.read_csv(csv_file)

# Iterate over the rows of the DataFrame
for index, row in df.iterrows():
    website = row["Website"]
    link = row["Link"]
    behavior = row["Behavior"]
    query = row["Query"]
    
    print(f"Behavior: {behavior} on {website}")
    
    # Open the link in Chrome
    driver.get(link)

    print(f"Searching for {query} on {website}")
    search_box = None
    retries = 3  # Number of retries
    for _ in range(retries):
        try:
            if website == "Wikipedia":
                search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "searchInput")))
            elif website in ["Google", "Bing"]:
                
                # Accept cookies if prompted (specific to Bing)
                if website == "Bing":
                    try:
                        accept_button = driver.find_element(By.ID, "bnp_btn_accept")
                        accept_button.click()
                    except NoSuchElementException:
                        pass  # If the accept button is not found, continue

                # Accept cookies if prompted
                elif website == "Google":
                    try:
                        accept_button = driver.find_element(By.ID, "L2AGLb")
                        accept_button.click()
                    except NoSuchElementException:
                        pass  # If the accept button is not found, continue

                search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q")))
            
            search_box.clear()
            search_box.send_keys(query)
            search_box.send_keys(Keys.RETURN)
            break  # Exit the retry loop if successful
        except (StaleElementReferenceException, TimeoutException):
            print("Element not found or stale. Retrying...")
            continue  # Retry if element not found or stale
    
    # Add some delay between searches
    time.sleep(3)  # Adjust delay as needed
    
    # Go back to the main page before searching for the next query
    driver.back()

# Close the WebDriver after all searches are simulated
driver.quit()
