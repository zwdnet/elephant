# -*- coding:utf-8 -*-
"""
计算空气质量指数
从网上爬取数据
使用Beautifulsoup解析网页
获取所有城市列表
输出到文件
使用panda分析数据
V10.0
20171227
"""


import csv
import pandas as pd
import matplotlib.pyplot as plt


def main():
    aqi_data = pd.read_csv('china_city_aqi.csv')
    print(aqi_data.info())
    print(aqi_data.head())

    # 数据清理
    filter_condition = aqi_data['AQI'] > 0
    clean_aqi_data = aqi_data[filter_condition]

    print(aqi_data['AQI'].max())
    print(aqi_data['AQI'].min())
    print(aqi_data['AQI'].mean())

    print(clean_aqi_data['AQI'].max())
    print(clean_aqi_data['AQI'].min())
    print(clean_aqi_data['AQI'].mean())


    sorted = aqi_data.sort_values(by = ['AQI'], ascending=False)
    print(sorted.head(50))

    top50_cities = clean_aqi_data.sort_values(by=['AQI']).head(50)
    top50_cities.plot(kind='bar', x='city', y='AQI', figsize=(20, 10))
    plt.savefig('top50_aqi.png')
    plt.show()

    # 保存为csv文件
    sorted.head(10).to_csv('top10_aqi.csv', index = False)


    top50_cities = clean_aqi_data.sort_values(by=['AQI'].head(50))
    top50_cities.plot(kind='bar', x = 'city', y = 'AQI', title = 'top50',
                      figsize=(20, 10))

if __name__ == "__main__":
    main()