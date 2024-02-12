import requests
from bs4 import BeautifulSoup

url = 'https://worldview.stratfor.com/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
headlines = soup.find('body').find_all('li', class_='headline')
line_number = 1
for x in headlines:
    print(str(line_number) + ". " + x.text.strip())
    line_number += 1
