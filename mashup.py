import doctest
import re
import os
import bs4
from urllib.parse import urlencode
import requests
import time
from selenium import webdriver

'''
リンク先のURLから評価のトップの情報を得る
'''
def recomended_shop(details_a):
    content_list = []
    for link in details.find_all('a'):
        content = str(link.get('href'))
        content_list = content.split('=')

        recommended_shop = []
        try  :
            best_scor = content_list[-2]+content_list[-1]
            if best_scor =="D&sort_mode1":
                return content
        except :
            pass

#-------------------------------------------
#---------------------------
'''
Address search
'''
def address_search(url_best):
#    print(url_best)
    resp = requests.get(url_best)
    details = bs4.BeautifulSoup(resp.text)
    content_list = []
    for link in details.find_all('a'):
        content = str(link.get('href'))
#        print(content)

    test_url = details.find_all('a', attrs={"class": "ist-rst__rst-name-target cpy-rst-name js-ranking-num", "href": "/link"})
    print(test_url)
'''
    for link_u in  details.find_all('a'):
        best_url = link_u.find('href', class="ist-rst__rst-name-target cpy-rst-name js-ranking-num")
        print(best_url)
        return best_url
'''
#---------------------------
'''
食べログ　で関内の店の
URLへ

'''
station_name = input("Please Enter station name where you search restrants: ")
driver = webdriver.Chrome()
driver.get('https://s.tabelog.com/')
time.sleep(1)
search_box = driver.find_element_by_name("sa")
'''
サンプル　”関内駅”
'''
#search_box.send_keys('関内駅')
search_box.send_keys(station_name)
search_box.submit()
time.sleep(1)# １秒間待つ

'''
移動した先のURLを取得する。
'''
cur_url = driver.current_url
'''
移動した先のページ情報を取得
'''
resp = requests.get(cur_url)
details = bs4.BeautifulSoup(resp.text)

best_shop = recomended_shop(details)
#print(best_shop)
driver.get(best_shop)

address_search(best_shop)

time.sleep(3)

'''
search best scor shop's URL
'''
#driver.get(recommended_shop[0])
time.sleep(5)
driver.quit()
