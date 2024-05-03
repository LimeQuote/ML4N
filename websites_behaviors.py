import csv

# Define websites, their links, corresponding behaviors, and queries
websites_behaviors = [
    {"website": "Wikipedia", "link": "https://www.wikipedia.org/", "behavior": "Search for the topic 'Machine Learning'", "query": "Machine Learning"},
    {"website": "Wikipedia", "link": "https://www.wikipedia.org/", "behavior": "Search for the topic 'Deep Learning'", "query": "Deep Learning"},
    {"website": "Wikipedia", "link": "https://www.wikipedia.org/", "behavior": "Search for the topic 'Python'", "query": "Python"},
    {"website": "Wikipedia", "link": "https://www.wikipedia.org/", "behavior": "Search for the topic 'Quantom Computing'", "query": "Quantom Computing"},
    {"website": "Wikipedia", "link": "https://www.wikipedia.org/", "behavior": "Search for the topic 'Italy'", "query": "Italy"},
    {"website": "Google", "link": "https://www.google.com/", "behavior": "Search for the topic 'Machine Learning'", "query": "Machine Learning"},
    {"website": "Google", "link": "https://www.google.com/", "behavior": "Search for the topic 'Deep Learning'", "query": "Deep Learning"},
    {"website": "Google", "link": "https://www.google.com/", "behavior": "Search for the topic 'Python'", "query": "Python"},
    {"website": "Google", "link": "https://www.google.com/", "behavior": "Search for the topic 'Quantom Computing'", "query": "Quantom Computing"},
    {"website": "Google", "link": "https://www.google.com/", "behavior": "Search for the topic 'Italy'", "query": "Italy"},
    {"website": "Bing", "link": "https://www.bing.com/", "behavior": "Search for the topic 'Machine Learning'", "query": "Machine Learning"},
    {"website": "Bing", "link": "https://www.bing.com/", "behavior": "Search for the topic 'Deep Learning'", "query": "Deep Learning"},
    {"website": "Bing", "link": "https://www.bing.com/", "behavior": "Search for the topic 'Python'", "query": "Python"},
    {"website": "Bing", "link": "https://www.bing.com/", "behavior": "Search for the topic 'Quantom Computing'", "query": "Quantom Computing"},
    {"website": "Bing", "link": "https://www.bing.com/", "behavior": "Search for the topic 'Italy'", "query": "Italy"}
]

# Define CSV file name
csv_file = "websites_behaviors.csv"

# Write data to CSV file
with open(csv_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Website", "Link", "Behavior", "Query"])  # Write header row
    for item in websites_behaviors:
        writer.writerow([item["website"], item["link"], item["behavior"], item["query"]])

print(f"Data saved to {csv_file}")


#Here all behaviors are searching and the queries are all the same for different websites. 
#If you want to change the behavior or the queries you need to change the simulator accordingly.
#In a more advanced implementation we can implement different kind of interactions with websites utelizing selenium webdriver