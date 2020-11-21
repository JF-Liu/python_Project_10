import requests
import random
import time
import json
import sys
import os
from urllib import request
from bs4 import BeautifulSoup

# data mkdir
resource_path = r'D:/pytel_data/interior_talk_0923_ta'
# resource_path = r'./interior_talk_03_ta'
if not os.path.exists(resource_path):
    os.mkdir(resource_path)

# headers
headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                        " (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
           }

# test
# url = "https://www.searchome.net/solution.aspx?page=%s"%(page_number)
# url ="https://www.searchome.net/solution.aspx?"
# url ="https://www.searchome.net/solution.aspx?page=1"
# def(test):
#     req = request.Request(url=url, headers=headers)
#     res = request.urlopen(req)
#     r = requests.get(url)
#     print(r.status_code)
#     soup = BeautifulSoup(res, 'html.parser')
#     print(soup)
#     def searchome_txet(title, n_page=0, url = url):


# 網頁page(第一層)

page_number = 2164
while page_number >= 0:
    # website
    url = "https://www.searchome.net/solution.aspx?page=%s"%(page_number)
    # print(page_number)
    req = request.Request(url=url, headers=headers)
    res = request.urlopen(req)
    r = requests.get(url)
    # print(r.status_code)
    soup = BeautifulSoup(res, 'html.parser')

    article_title_html = soup.select('div[class="rdata"]')
    # print(article_title_html)
    print("========")


    for each_article in article_title_html:
        try:
            # 休息時間
            # sleep_time = random.randint(3, 7)
            # print("sleep time: %s sec"%(sleep_time))
            # time.sleep(sleep_time)

            # 網頁page,title、link(第一層)萃取
            title_text = each_article.a.text
            print(each_article.a.text)
            print("https://www.searchome.net" + each_article.a['href'])

            page_id = "sea"+(each_article.a['href'].replace("/article.aspx?id=", ''))
            print(page_id)

            # 網頁page,內文(第二層)
            article_url = "https://www.searchome.net" + each_article.a['href'] # requests
            # print(page_number)
            article_req = request.Request(url=article_url, headers=headers)
            article_res = request.urlopen(article_req)
            article_r = requests.get(article_url)
            # print(article_r.status_code)
            article_soup = BeautifulSoup(article_res, 'html.parser')
            # print(article_soup)
            # 休息時間
            # sleep_time = random.randint(3, 10)
            # print("sleep time: %s sec"%(sleep_time))
            # time.sleep(sleep_time)


            # 文章內容
            # date
            article_data_html_2 = article_soup.select('span[class="date"]')
            for each_article in article_data_html_2:
                print("date:" + (each_article.text))
            detal_1 = ((each_article.text).replace(u'\xa0', '').replace('\n', '').replace('\r', ''))

            # focus
            article_data_html_3 = article_soup.select('span[class="record"]')
            for each_article in article_data_html_3:
                print(each_article.text)
            detal_2 = ((each_article.text).replace(u'\xa0', '').replace('\n', '').replace('人氣', '').replace('\r', ''))

            # home_data
            article_data_html_4 = article_soup.select('div[class="home_data"]')
            for each_article in article_data_html_4:
                print("home_data:" + (each_article.text).replace(u'\xa0', '').replace('\n', '').replace('\t', '')
                       .replace('\r', '').replace('\n\n', '').replace('Home Data', ''))
            detal_3 = ((each_article.text).replace(u'\xa0', '').replace('\n', '').replace('\t', '')
                       .replace('\r', '').replace('\n\n', '').replace('Home Data', ''))

            # detal
            article_data_html_5 = article_soup.select('div[class="content_data"]')
            for each_article in article_data_html_5:
                print("內文:" + (each_article.text).strip().replace(u'\xa0', '').replace('\n', ''))
            detal_4 = ((each_article.text).strip().replace(u'\xa0', '').replace('\n', ''))

            # images link
            images_link = []
            article_data_html_6 = article_soup.find_all('span', {"class": "editor_img1"})
            for each_article in article_data_html_6:
                try:
                    images_link.append(each_article.img["data-src"])
                    print(each_article.img["data-src"])
                except:
                    pass
            detal_5 = str(images_link)

            # 建立dict
            dict = {"_id": (page_id),
                    "title": (title_text),
                    "page_link": (article_url),
                    "date": (detal_1),
                    "人氣": (detal_2),
                    "home_data": (detal_3),
                    "內文": (detal_4),
                    "images_link": (detal_5)
            }

            # 寫檔案
            # try:
            # with open(r'%s/%s.txt' % (resource_path, title_text), 'w', encoding='utf-8') as w:
            with open(r'%s/%s.json' % (resource_path, page_id), 'w', encoding='utf-8-sig') as f:
                json.dump(dict, f, ensure_ascii=False)
            f.close()
            # 1 <-- ok
            print("1")
                    # w.write("title:" + title_text + '\n')
                    # w.write("page_link:" + article_url + '\n')
                    # w.write("date:" + detal_1 + '\n')
                    # w.write("人氣:" + detal_2 + '\n')
                    # w.write("內文:" + detal_3 + '\n')
                    # w.write("images_link:" + detal_4 + '\n')
                    # w.write(str(dict))
            # pattern = r'[\\/:*?"<>|\r\n]+'
            # except:
            #     with open(re.sub(r's', '-',% (resource_path, title_text)), 'w', encoding='utf-8') as f:
            #         json.dump(dict, f, ensure_ascii=False)
            #     print("2")
        # 錯誤排除
        except AttributeError as e:
            print("========")
            print(each_article)
            print(e.args)
            print("========")
        print("========")

    page_number -= 1

    time.sleep(random.uniform(1, 5))
    print(time.sleep)
sys.exit()
