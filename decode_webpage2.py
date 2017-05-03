import requests
from bs4 import BeautifulSoup
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


base_url = 'http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "lxml")
filename = raw_input("Enter output file name: ")
with open(filename, 'w') as open_file:
    for i in soup.find_all("p", {"data-reactid": re.compile("[2-3][0-9][0-9]")}):
        if i.string:
            open_file.write(str(i.string)+'\n')
