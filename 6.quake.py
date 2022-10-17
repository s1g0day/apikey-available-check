#/usr/bin/python3
# https://quake.360.cn/quake/#/help?id=5e6845ade1322779dd299e14&title=Quake%E7%AE%80%E4%BB%8B

import time
import urllib3
import sys
import requests
import json
from tabulate import tabulate

print('\n' + '*'*30 + "程序运行" + '*'*30 + '\n')
table = [["API_key", "user_fullname", "month_remaining_credit", "constant_credit", "free_query_api_count", "role_fullname"]]

quake_apiurl = 'https://quake.360.cn/api/v3/user/info'

for key in open("key.txt"):
    API_key=key.strip()
    header = {
        'X-QuakeToken': API_key
    }
    res = requests.get(quake_apiurl,headers=header)
    if res.status_code == 200:
        results = json.loads(res.text)
        lenrole = len(results["data"]["role"])
        # print(results["data"])
        results_data = API_key + ',' + str(results["data"]["user"]["fullname"]) + ',' + str(results["data"]["month_remaining_credit"]) + ',' + str(results["data"]["constant_credit"]) + ',' + str(results["data"]["free_query_api_count"]) + ',' + str(results["data"]["role"][lenrole-1]["fullname"])
        print(results_data.split(","))
        table.append(results_data.split(","))
    else:
        print(API_key + ', Error!')
    time.sleep(2)

print('\n' + '*'*30 + "程序结果" + '*'*30 + '\n')
test = '''
user_fullname: quake用户名,
month_remaining_credit: 月度剩余积分, 
constant_credit: 长效积分, 
free_query_api_count: api月度剩余免费查询次数
role_fullname: 用户级别
'''
print(test + '\n' + '*'*30 + "程序结果" + '*'*30 + '\n')
print(tabulate(table, headers='firstrow'))

