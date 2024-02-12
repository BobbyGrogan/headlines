import requests
from bs4 import BeautifulSoup

url = 'https://www.techtarget.com/searchsecurity/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
headlines = soup.find('body').find_all('h4')

inc = 0
for x in headlines:
    print(x.text.strip())
    inc += 1
    if inc > 4:
        exit()
