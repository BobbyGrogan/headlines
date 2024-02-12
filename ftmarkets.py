import requests
from bs4 import BeautifulSoup

def extract_span_content(url):
    # Fetch the content of the webpage
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve the web page")
        return []

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all ul elements with class 'mod-ui-news__list'
    ul_elements = soup.find_all('ul', class_='mod-ui-news__list')
    if not ul_elements:
        return []

    # Extract the span elements content from all ul elements
    span_contents = []
    for ul in ul_elements:
        li_elements = ul.find_all('li')
        for li in li_elements:
            spans = li.find_all('span')
            for span in spans:
                span_contents.append(span.get_text(strip=True))

    return span_contents

# Replace with the URL of the webpage you're interested in
url = 'https://markets.ft.com/data'
span_texts = extract_span_content(url)
line_number = 1
for text in span_texts:
    print(str(line_number) + ". " + text)
    line_number += 1
