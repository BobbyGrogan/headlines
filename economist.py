import requests
from bs4 import BeautifulSoup
import re

# URL of the webpage to scrape
url = 'https://www.economist.com/'

# Fetch the webpage content
response = requests.get(url)
html_content = response.text

# Parse HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Prepare a regular expression pattern to match data-analytics values
pattern = re.compile(r'top_stories:headline_\d+')

# Find all <a> elements with a matching data-analytics attribute
links = soup.find_all('a', attrs={'data-analytics': pattern})

# Extract and print the text of each link
line_number = 1
for link in links:
    print(str(line_number) + ". " + link.get_text())
    line_number += 1
