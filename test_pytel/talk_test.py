import requests
import random
import time
from urllib import request
from bs4 import BeautifulSoup



headers = {'user-agent' : " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 " \
            "(KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
            }

url = "https://www.searchome.net/article.aspx?id=25054"  # requests

req = request.Request(url=url, headers=headers)
res = request.urlopen(req)
r = requests.get(url)
#print(r.status_code)
soup = BeautifulSoup(res, 'html.parser')
#print(soup)

# article_data_html_1 = soup.select('div[class="articel_info"]')
# article_data_html_2 = soup.select('span[class="date"]')
# article_data_html_3 = soup.select('span[class="record"]')
# article_data_html_4 = soup.select('div[class="content_data"]')
# article_data_html_5 = soup.select('div[class="content_data"]')
# article_data_html_5 = soup.find_all('span', {"class": "editor_img1"})
# article_data_html_6 = soup.select('div[class="home_data"]')
#article_data_html_5 = soup.select('div[class="container"]')

#article_data_html_5 = soup.select('span[class="editor_img1"]')
images_link = []
article_data_html_6 = soup.find_all('span', {"class": "editor_img1"})
for each_article in article_data_html_6:
    try:
        images_link.append(each_article.img["data-src"])
        print(each_article.img["data-src"])
    except:
        pass
    detal_5 = str(images_link)




# for each_article in article_data_html_1:
#     each_article.span['date']
# print(article_data_html_1)
# for each_article in article_data_html_2:
#     print("date" + (each_article.text))
#
# for each_article in article_data_html_3:
#     print(each_article.text)
#
# for each_article in article_data_html_4:
#     print("內文"+(each_article.text))


# for each_article in article_data_html_6:
#     print(each_article)
#     print(each_article.text)
    # print(each_article.img["data-src"])

#

