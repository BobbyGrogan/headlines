import requests
from bs4 import BeautifulSoup

url = 'https://www.wsj.com/news/latest-headlines'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup)
headlines = soup.find('body').find_all("span") # class_='WSJTheme--headlineText--He1ANr9C')

#inc = 0
for x in headlines:
    print(x.text.strip())
#    inc += 1
#    if inc > 10:
#        exit()
