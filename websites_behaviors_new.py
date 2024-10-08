### This file saves the information of the search process (combination of the browsers, websites, and queries) in a CSV file ###
### credentials: Shaghayegh Samadzadeh, Jun2024
""""
This script logs the search process across different browsers, websites, and queries into a CSV file for analysis.
Author: Shaghayegh Samadzadeh
Date: June 2024
"""


import pandas as pd

# Define browser, websites, their links, corresponding behaviors, and queries
browsers = ["Chrome", "Edge", "Firefox"]
websites = ["Wikipedia", "Google", "Bing"]
queries = ["Machine Learning", "Deep Learning", "Python", "Quantum Computing", "Italy"]
behaviors = [f"Search for the topic '{query}'" for query in queries]
links = {
    "Wikipedia": "https://www.wikipedia.org/",
    "Google": "https://www.google.com/",
    "Bing": "https://www.bing.com/"
}
repetition_id = 100

websites_behaviors = []

for website in websites:
    for browser in browsers:
        for query, behavior in zip(queries, behaviors):
            websites_behaviors.append({
                "browser": browser,
                "website": website,
                "link": links[website],
                "behavior": behavior,
                "query": query,
                "repetition_id": repetition_id
                
            })

# Define CSV file name
csv_file = "websites_behaviors.csv"

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(websites_behaviors)

# Write DataFrame to CSV file
df.to_csv(csv_file, index=False)

print(f"Data saved to {csv_file}")



