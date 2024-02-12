import requests
from bs4 import BeautifulSoup

def get_list_items(url, div_class):
    # Fetch the content of the webpage
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve the web page")
        return []

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the div with the given class
    div = soup.find('div', class_=div_class)
    if not div:
        print(f"No div found with class '{div_class}'")
        return []

    # Find the ul within the div
    ul = div.find('ul')
    if not ul:
        print(f"No ul found within div with class '{div_class}'")
        return []

    # Extract text from all li items within the ul
    list_items = []
    for li in ul.find_all('li'):
        text = ' '.join(li.stripped_strings)
        # Remove space before commas and periods
        text = text.replace(' ,', ',').replace(' .', '.').replace(" '", "'")
        list_items.append(text)

    return list_items

# Example usage
url = 'https://en.wikipedia.org/wiki/Portal:Current_events'  # Replace with your URL
div_class = 'p-current-events-headlines'
items = get_list_items(url, div_class)
line_number = 1
for item in items:
    print(str(line_number) + ". " + item)
    line_number += 1
