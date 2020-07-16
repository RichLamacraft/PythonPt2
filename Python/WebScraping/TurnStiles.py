# taken from this guide: https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460

import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# set the address of the site we want to scrape

url = 'http://web.mta.info/developers/turnstile.html'
response = requests.get(url) # 200 is good, 404 is not!

soup = BeautifulSoup(response.text, "html.parser")
soup.findAll('a')

one_a_tag = soup.findAll('a')[37]
link = one_a_tag['href']

download_url = 'http://web.mta.info/developers/' + link
urllib.request.urlretrieve(download_url, './'+link[link.find('/turnstile_')+1:])
