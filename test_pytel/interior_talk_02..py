import requests
import cookiejar
from urllib import request
from bs4 import BeautifulSoup





# url ="https://www.100.com.tw/article"
#
# headers = {'user-agent' : " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 " \
#             "(KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
#             }
#
#
# req = request.Request(url=url, headers=headers)
# res = request.urlopen(req)
# r = requests.get(url)
# print(r.status_code)
# soup = BeautifulSoup(res, 'html.parser')
# print(soup)



url ="https://www.100.com.tw/article"
headers = {'User-Agent': " Mozilla/5.0 (Windows NT 10.0; Win64; x64)" \
             " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"
}


#設定 cookie
#CookieJar = "_ga=GA1.3.1662238672.1597508753; _gid=GA1.3.1812574736.1598843566; _gat=1"
#my_cookie = cookiejar.CookieJar(request)

req = request.Request(url=url, headers=headers)
res = request.urlopen(req)
r = requests.get(url)
print(r)
soup = BeautifulSoup(res, 'html.parser')
print(soup)

# 'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,"
# "image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
# "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
# "accept-encoding": "gzip, deflate, br",
# "Connection": "keep-alive",
# "cache-control": "max-age=0",
# "Accept-Charset": "UTF8,utf-8;q=0.7,*;q=0.7",
# "If-None-Match": "10f53-B8YHDa/OaIIByx3qZPS3eeMfvRY"