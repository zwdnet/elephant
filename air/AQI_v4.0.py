# -*- coding:utf-8 -*-
"""
计算空气质量指数
CSV文件操作
V4.0
20171224
"""
import json
import csv
import os

def process_json_file(filepath):
    # f = open(filepath, mode="r", encoding='utf-8')
    # city_list = json.load(f)
    # return city_list
    with open(filepath, mode="r", encoding='utf-8') as f:
        city_list = json.load(f)
    print(city_list)


def process_csv_file(filepath):
    with open(filepath, mode="r", encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(', '.join(row))

def main():
    filepath = input("请输入文件名称：")
    filename, file_ext = os.path.splitext(filepath)

    if file_ext == '.json':
        process_json_file(filepath)
    elif file_ext == '.csv':
        process_csv_file(filepath)
    else:
        print("不支持的文件格式!")

    # city_list = process_json_file(filepath)
    # city_list.sort(key = lambda city: city['aqi'])
    #
    # lines = []
    # lines.append(list(city_list[0].keys()))
    # for city in city_list:
    #     lines.append(list(city.values()))

    # f = open('aqi.csv', 'w', encoding='utf-8', newline='')
    # writer = csv.writer(f)
    # for line in lines:
    #     writer.writerow(line)
    # f.close()


if __name__ == "__main__":
    main()