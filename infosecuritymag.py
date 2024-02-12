import requests
from bs4 import BeautifulSoup

def extract_p_content(url):
    # Fetch the content of the webpage
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve the web page")
        return []

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all li elements with class 'webpage-item'
    li_elements = soup.find_all('li', class_='webpage-item')

    # Extract the p elements content
    p_contents = []
    for li in li_elements:
        p = li.find('p', class_='webpage-summary')
        if p:
            p_contents.append(p.get_text(strip=True))

    return p_contents

# Replace with the URL of the webpage you're interested in
url = 'https://www.infosecurity-magazine.com/news/'
p_texts = extract_p_content(url)
line_number = 1
for text in p_texts:
    print(str(line_number) + ". " + text)
    line_number += 1
