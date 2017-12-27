# -*- coding:utf-8 -*-
"""
计算空气质量指数
从网上爬取数据
使用Beautifulsoup解析网页
获取所有城市列表
输出到文件
使用panda分析数据
V9.0
20171227
"""


import csv
import pandas as pd


def main():
    aqi_data = pd.read_csv('china_city_aqi.csv')
    print(aqi_data.info())
    print(aqi_data.head())
    print(aqi_data['AQI'].max())
    print(aqi_data['AQI'].min())
    print(aqi_data['AQI'].mean())

    # top10
    sorted = aqi_data.sort_values(by = ['AQI'], ascending=False)
    print(sorted.head(10))

    # 保存为csv文件
    sorted.head(10).to_csv('top10_aqi.csv', index = False)

if __name__ == "__main__":
    main()