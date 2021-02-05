import requests
from bs4 import BeautifulSoup

# this code works!
url = "https://www.tmcfinancing.com/covid-19-grants/"
r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

print(r.status_code)

soup = BeautifulSoup(r.text, "html.parser")
soup.find_all('href')
print(soup.prettify())


# testing next url






# if 403 error: pretend i'm firefox's open-source renderer
# r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

# find single (find) vs all
# soup.find_all(x)