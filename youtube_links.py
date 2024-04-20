import os
import csv
import googleapiclient.discovery
from dotenv import load_dotenv

# Load environment variables containing YouTube API key
load_dotenv()
YOUTUBE_API_KEY = os.getenv("API_Key")

# Function to fetch video links using YouTube Data API
def fetch_youtube_video_links(api_key, query, max_results=100):
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

    video_links = []
    next_page_token = None
    total_results_fetched = 0

    while total_results_fetched < max_results:
        request = youtube.search().list(
            part="snippet",
            q=query,
            maxResults=min(50, max_results - total_results_fetched),  # Limit to remaining results
            type="video",
            pageToken=next_page_token  # Use next page token for pagination
        )
        response = request.execute()

        for item in response["items"]:
            video_id = item["id"]["videoId"]
            video_link = f"https://www.youtube.com/watch?v={video_id}"
            video_links.append(video_link)
            total_results_fetched += 1

        next_page_token = response.get("nextPageToken")
        if not next_page_token:
            break  # No more pages to fetch

    return video_links

# Query for YouTube videos (e.g., "machine learning tutorials")
query = "machine learning"

# Fetch 100 YouTube video links for the given query
video_links = fetch_youtube_video_links("API_Key", query)

# Write video links to a CSV file

csv_file = "youtube_video_links.csv"
with open(csv_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Video Links"])
    writer.writerows([[link] for link in video_links])

print(f"Video links saved to {csv_file}")
