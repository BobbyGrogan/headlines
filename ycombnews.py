import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = 'https://news.ycombinator.com/'

# Fetch the webpage content
response = requests.get(url)
html_content = response.text

# Parse HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all <span> elements with the "titleline" class
headlines = soup.find_all('span', class_='titleline')

# Extract and print headlines
line_number = 1
for headline in headlines:
    print(str(line_number) + ". " + headline.get_text().strip())
    line_number += 1
