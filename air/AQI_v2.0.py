# -*- coding:utf-8 -*-
"""
计算空气质量指数
JSON文件操作
V2.0
20171223
"""
import json


def process_json_file(filepath):
    f = open(filepath, mode="r", encoding='utf-8')
    city_list = json.load(f)
    return city_list


def main():
    filepath = input("请输入json文件路径：")
    city_list = process_json_file(filepath)
    city_list.sort(key = lambda city: city['aqi'])
    top5_list = city_list[:5]
    f = open('top5_aqi.json', mode='w', encoding='utf-8')
    json.dump(top5_list, f, ensure_ascii=False)

if __name__ == "__main__":
    main()