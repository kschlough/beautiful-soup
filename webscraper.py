import requests
from bs4 import BeautifulSoup

url = "http://www.pyladies.com"
r = requests.get(url)

print(r.status_code)

soup = BeautifulSoup(r.text, "html.parser")
soup.find_all('a')
print(soup.prettify())



# if 403 error: pretend i'm firefox's open-source renderer
# r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

# find single (find) vs all
# soup.find_all(x)