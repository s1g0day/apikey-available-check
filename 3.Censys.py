#/usr/bin/python3
# https://search.censys.io/api

import time
import sys
import requests
import json
from tabulate import tabulate

print('\n' + '*'*30 + "程序运行" + '*'*30 + '\n')
table = [["UID/SECRET", "used", "allowance", "resets_at"]]

API_URL = "https://search.censys.io/api/v1/account"

for key in open("key.txt"):
    UID, SECRET = key.strip().split("|")
    res = requests.get(API_URL, auth= (UID, SECRET))
    if res.status_code == 200:
        results = json.loads(res.text)
        results_data = UID + ':' + SECRET + ',' + str(results['quota']['used']) + ',' + str(results['quota']['allowance']) + ',' + str(results['quota']['resets_at'])
        print(results_data.split(","))
        table.append(results_data.split(","))
    else:
        print(UID + ', Error!')
    time.sleep(2)

print('\n' + '*'*30 + "程序结果" + '*'*30 + '\n')
print("used: 使用次数", "\nallowance: 剩余额度", "\nresets_at: 重置时间")
print('\n' + '*'*30 + "程序结果" + '*'*30 + '\n')
print(tabulate(table, headers='firstrow'))

