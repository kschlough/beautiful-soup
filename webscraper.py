### notes

# if 403 error: pretend i'm firefox's open-source renderer
# r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

# find single (find) vs all
# soup.find_all(x)




import requests
from bs4 import BeautifulSoup

### this code works!
url = "https://www.tmcfinancing.com/covid-19-grants/"
r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

print(r.status_code)

soup = BeautifulSoup(r.text, "html.parser")
### commented out for now while doing other tests
# soup.find_all('a')[2].attrs['href']
# print(soup.prettify())

### test: extract links from website into data structure
### maybe store in dictionary not array?
links = {}

### using get_text() method
for link in soup.find_all('a'):  
    links[link.get_text()] = link

print(links)

### 








