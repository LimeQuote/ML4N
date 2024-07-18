#This program checks if geckodriver is running using the Selenium library.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Path to your GeckoDriver executable
geckodriver_path = r'C:\Users\Shaghayegh\geckodriver.exe'
#I added the path to the environmental variables of the system

# Initialize Firefox WebDriver
driver = webdriver.Firefox()

# Open Google homepage
driver.get("https://www.google.com/")

# Accept cookies if prompted
try:
    accept_button = driver.find_element(By.ID, "L2AGLb")
    accept_button.click()
except Exception as e:
    print("No cookie acceptance button found, or already accepted.", e)

# List of queries to simulate browsing
queries = ["Machine Learning", "Politecnico di Torino", "Data Science", "Artificial Intelligence", "Python programming"]

# Loop through each query and simulate browsing
for query in queries:
    # Find the search box and submit the query
    search_box = driver.find_element(By.NAME, "q")
    search_box.clear()  # Clear any previous content in the search box
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    
    # Wait for the results to load (you may need to adjust the time depending on your internet speed)
    time.sleep(5)
    
    # Navigate back to the Google homepage for the next query
    driver.get("https://www.google.com/")
    
# Close the browser window after all queries are simulated
driver.quit()

