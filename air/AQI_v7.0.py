# -*- coding:utf-8 -*-
"""
计算空气质量指数
从网上爬取数据
使用Beautifulsoup解析网页
获取所有城市列表
V7.0
20171226
"""


import requests
from bs4 import BeautifulSoup
import time


def get_city_aqi(city_pinyin):
    url = "http://pm25.in/" + city_pinyin
    r = requests.get(url, timeout = 30)
    soup = BeautifulSoup(r.text, 'lxml')
    div_list = soup.find_all('div', {'class':'span1'})

    city_aqi = []
    for i in range(8):
        div_content = div_list[i]
        caption = div_content.find('div', {'class':'caption'}).text.strip()
        value = div_content.find('div', {'class':'value'}).text.strip()
        city_aqi.append((caption, value))
    return city_aqi


def get_all_cities():
    url = "http://pm25.in/"
    city_list = []
    r = requests.get(url, timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')

    city_div = soup.find_all("div", {"class":"bottom"})[1]
    city_link_list = city_div.find_all('a')
    for city_link in  city_link_list:
        city_name = city_link.text
        city_pinyin = city_link['href'][1:]
        city_list.append((city_name, city_pinyin))
    print(city_list)
    return city_list


def main():
    city_list = get_all_cities()
    for city in city_list:
        city_name = city[0]
        city_pinyin = city[1]
        city_aqi = get_city_aqi(city_pinyin)
        print("{}的空气质量为:{}".format(city_name, city_aqi))
        time.sleep(5)


if __name__ == "__main__":
    main()