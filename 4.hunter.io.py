#/usr/bin/python3
# https://hunter.io/api-documentation/v2

import time
import urllib3
import sys
import requests
import json
from tabulate import tabulate

print('\n' + '*'*30 + "程序运行" + '*'*30 + '\n')
table = [["API_key", "plan_name", "plan_level", "reset_date", "calls_used", "calls_available", "searches_used", "searches_available", "verifications_used", "verifications_available"]]

hunter_format = "https://api.hunter.io/v2/account?api_key={key}"

for key in open("key.txt"):
    API_key=key.strip()
    url = hunter_format.format(key=API_key)
    res = requests.get(url)
    if res.status_code == 200:
        results = json.loads(res.text)
        results_data = API_key + ',' + str(results['data']['plan_name']) + ',' + str(results['data']['plan_level'])+ ',' + str(results['data']['reset_date']) + ',' + str(results['data']['calls']['used']) + ',' + str(results['data']['calls']['available']) + ',' + str(results['data']['requests']['searches']["used"]) + ',' + str(results['data']['requests']['searches']['available']) + ',' + str(results['data']['requests']['verifications']["used"]) + ',' + str(results['data']['requests']['verifications']['available'])
        print(results_data.split(","))
        table.append(results_data.split(","))
    else:
        print(API_key + ', Error!')
    time.sleep(2)

print('\n' + '*'*30 + "程序结果" + '*'*30 + '\n')
print("plan_name: 会员计划", "\nplan_level: 会员级别", "\nreset_date: 重置时间", "\ncalls_used: 使用总次数", "\ncalls_available: 总额度", "\nsearches_used: 搜索使用次数", "\nsearches_available: 搜索总额度", "\nverifications_used: 验证使用次数", "\nverifications_available: 验证总额度")
print('\n' + '*'*30 + "程序结果" + '*'*30 + '\n')
print(tabulate(table, headers='firstrow'))

