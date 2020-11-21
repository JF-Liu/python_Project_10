import requests
from urllib import request
from bs4 import BeautifulSoup
# from lxml import stree
# import jieba
# import time
# import random
# import pandas as pd
# from http import cookiejar



url ="https://hhh.com.tw/forum/ists?category=2"

headers = {'user-agent' : " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 " \
            "(KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
            }


req = request.Request(url=url, headers=headers)
res = request.urlopen(req)
r = requests.get(url)
print(r.status_code)
soup = BeautifulSoup(res, 'html.parser')
#print(soup)



page_number = 1
while page_number >= 1:
    # print(page_number)
    req = request.Request(url=url, headers=headers)
    res = request.urlopen(req)
    r = requests.get(url)
    # print(r.status_code)
    soup = BeautifulSoup(res, 'html.parser')

    article_title_html = soup.select('div[class="post"]')
    print(article_title_html)
    print("========")

    #
    # for each_article in article_title_html:
    #     try:
    #         # 休息時間
    #         # sleep_time = random.randint(3, 7)
    #         # print("sleep time: %s sec"%(sleep_time))
    #         # time.sleep(sleep_time)
    #
    #         # 網頁page,title、link(第一層)萃取
    #         title_text = each_article.a.text
    #         print(each_article.a.text)
    #         print("https://www.searchome.net" + each_article.a['href'])
    #
    #         # 網頁page,內文(第二層)
    #         article_url ="https://www.searchome.net" + each_article.a['href'] #requests
    #         # print(page_number)
    #         article_req = request.Request(url=article_url, headers=headers)
    #         article_res = request.urlopen(article_req)
    #         article_r = requests.get(article_url)
    #         # print(article_r.status_code)
    #         article_soup = BeautifulSoup(article_res, 'html.parser')
    #         # print(article_soup)
    #         # 休息時間
    #         # sleep_time = random.randint(3, 10)
    #         # print("sleep time: %s sec"%(sleep_time))
    #         # time.sleep(sleep_time)
    #
    #         #文章內容
    #         #date
    #         article_data_html_2 = article_soup.select('span[class="date"]')
    #         for each_article in article_data_html_2:
    #             print("date:" + (each_article.text))
    #         detal_1 = ((each_article.text).replace(u'\xa0', '').replace('\n', '').replace('\r', ''))
    #
    #         #focus
    #         article_data_html_3 = article_soup.select('span[class="record"]')
    #         for each_article in article_data_html_3:
    #             print(each_article.text)
    #         detal_2 = ((each_article.text).replace(u'\xa0', '').replace('\n', '').replace('人氣', '').replace('\r', ''))
    #
    #         #detal
    #         article_data_html_4 = article_soup.select('div[class="content_data"]')
    #         for each_article in article_data_html_4:
    #             print("內文:" + (each_article.text).strip().replace(u'\xa0', '').replace('\n', ''))
    #         detal_3 = ((each_article.text).strip().replace(u'\xa0', '').replace('\n', ''))
    #
    #         #images link
    #         images_link = []
    #         article_data_html_5 = article_soup.find_all('span', {"class": "editor_img1"})
    #         for each_article in article_data_html_5:
    #             images_link.append(each_article.img["data-src"])
    #             print(each_article.img["data-src"])
    #         detal_4 = str(images_link)
    #
    #         #建立dict
    #         dict = {"title": (title_text),
    #                 "page_link": (article_url),
    #                 "date": (detal_1),
    #                 "人氣": (detal_2),
    #                 "內文": (detal_3),
    #                 "images_link": (detal_4)
    #         }
    #
    #         #寫檔案
    #         with open(r'%s/%s.txt' % (resource_path, title_text), 'w', encoding='utf-8') as w:
    #             # w.write("title:" + title_text + '\n')
    #             # w.write("page_link:" + article_url + '\n')
    #             # w.write("date:" + detal_1 + '\n')
    #             # w.write("人氣:" + detal_2 + '\n')
    #             # w.write("內文:" + detal_3 + '\n')
    #             # w.write("images_link:" + detal_4 + '\n')
    #             w.write(str(dict))
    #             print()
    #
    #     #錯誤排除
    #     except AttributeError as e:
    #         print("========")
    #         print(each_article)
    #         print(e.args)
    #         print("========")
    #     print("========")


    page_number -= 1














# #分解動作
# #import feedparser
# #設定 request header
# user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
# my_headers = {
#     'User-Agent': user_agent,
#     "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#     "accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
#     "accept-encoding": "gzip, deflate, br",
#     "Connection": "keep-alive",
#     "cache-control": "no-cache",
#     "Accept-Charset": "UTF8,utf-8;q=0.7,*;q=0.7"
# }
# rss_url = "https://udn.com/rssfeed/news/2/7225?ch=news"
#
#
#
#
# #設定 cookie
# my_cookie = cookiejar.CookieJar()
#
#
# newsFeed = feedparser.parse(rss_url)
# newsFeed
#
#
# i = 1
# for e in newsFeed['entries']:
#     title = e['title']
#     link_url = e['links'][0]['href']
#     print("%s, %s, %s"%(i, title, link_url))
#     i = i + 1
#
#
#
#
# #爬文
# each_article_text_list = []
# for e in newsFeed['entries']:
#     url = e['links'][0]['href']
#     print(url)
#     r = requests.get(url, headers = my_headers, cookies = my_cookie)
#     if r.status_code == 200:
#         parse_tree = etree.parse(StringIO(r.text), etree.HTMLParser())
#         article_elements = parse_tree.xpath('//article//p')
#         for a_part in article_elements:
#             if type(a_part.text) is str:
#                 each_article_text_list.append(a_part.text.strip())
#         sleep_time = random.randint(3,10)
#         print("sleep time: %s sec"%(sleep_time))
#         time.sleep(sleep_time)
#     all_article_text = ''.join(each_article_text_list)
# all_article_text
#
#
# seg_words_list = jieba.lcut(all_article_text)
# seg_words_list
#
#
# #stop word
# with open(file='jieba_data/stop_words.txt', mode='r', encoding='utf-8') as file:
#     stop_words = file.read().split('\n')
# stop_words
#
#
# #分詞
# seg_stop_words_list = []
# seg_words_list = jieba.lcut(all_article_text)
# for term in seg_words_list:
#     if term not in stop_words:
#         seg_stop_words_list.append(term)
# seg_stop_words_list