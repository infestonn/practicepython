import requests
from bs4 import BeautifulSoup
import re



base_url = 'http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "lxml")


for i in soup.find_all("p", {"data-reactid": re.compile("[2-3][0-9][0-9]")}):
    if i.string:
        print(i.string)
