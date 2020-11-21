import requests
import cookiejar
from urllib import request
from bs4 import BeautifulSoup

url ="https://www.100.com.tw/article"

headers = {'user-agent' : " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 " \
            "(KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
            }


req = request.Request(url=url, headers=headers)
res = request.urlopen(req)
r = requests.get(url)
print(r)
soup = BeautifulSoup(res, 'html.parser')
print(soup)