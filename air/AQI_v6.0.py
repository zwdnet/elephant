# -*- coding:utf-8 -*-
"""
计算空气质量指数
从网上爬取数据
使用Beautifulsoup解析网页
V6.0
20171225
"""


import requests
from bs4 import BeautifulSoup


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


def main():
    city_pinyin = input("请输入城市拼音:")
    city_aqi = get_city_aqi(city_pinyin)
    print("空气质量为:{}".format(city_aqi))


if __name__ == "__main__":
    main()