import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
from urllib.parse import urljoin

# List of URLs to scrape
urls = [
    'https://sgp.fas.org/crs/natsec/index.html',
    'https://sgp.fas.org/crs/natsec/primer.html',
    'https://sgp.fas.org/crs/mideast/index.html',
    'https://sgp.fas.org/crs/row/index.html',
    'https://sgp.fas.org/crs/secrecy/index.html',
    'https://sgp.fas.org/crs/intel/index.html',
    'https://sgp.fas.org/crs/homesec/index.html',
    'https://sgp.fas.org/crs/nuke/index.html',
    'https://sgp.fas.org/crs/weapons/index.html',
    'https://sgp.fas.org/crs/terror/index.html',
    'https://sgp.fas.org/crs/misc/index.html'
]

# Function to parse a date string and return a datetime object
def parse_date(date_str):
    try:
        # Check for 'updated' word and extract date
        match = re.search(r'(updated )?(\w+ \d+, \d{4})', date_str)
        if match:
            return datetime.strptime(match.group(2), '%B %d, %Y')
    except ValueError:
        return None

# Function to fetch and parse articles from a URL
def fetch_articles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = []
    for li in soup.find_all('li'):
        link = li.find('a')
        if link and link.get('href'):
            title = link.get_text()
            href = urljoin(url, link['href'])  # Combine base URL with link extension
            date_str = li.get_text().split(', ', 1)[1] if ', ' in li.get_text() else ''
            date = parse_date(date_str)
            if date:
                articles.append({"date": date, "title": title, "url": href})
    return articles

# Fetch articles from all URLs
all_articles = []
for url in urls:
    all_articles.extend(fetch_articles(url))

# Sort articles by date and get the 10 most recent
all_articles.sort(key=lambda x: x["date"], reverse=True)
most_recent_articles = all_articles[:10]

# Print the 10 most recent articles
line_number = 1
for article in most_recent_articles:
    print(str(line_number) + ".")
    print(f"Title: {article['title']}")
    print(f"Date: {article['date'].strftime('%B %d, %Y')}")
    print(f"URL: {article['url']}")
    line_number += 1
    print()
