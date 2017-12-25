# -*- coding:utf-8 -*-
"""
计算空气质量指数
从网上爬取数据
V5.0
20171225
"""


import requests


def get_html_text(url):
    r = requests.get(url, timeout = 30)
    return r.text


def main():
    city_pinyin = input("请输入城市拼音:")
    url = "http://pm25.in/" + city_pinyin
    url_text = get_html_text(url)
    aqi_div = """ <div class="span12 data">
        <div class="span1">
          <div class="value">
            """
    index = url_text.find(aqi_div)
    begin_index = index + len(aqi_div)
    end_index = begin_index + 2
    aqi_value = url_text[begin_index:end_index]
    print("空气质量为:{}".format(aqi_value))


if __name__ == "__main__":
    main()