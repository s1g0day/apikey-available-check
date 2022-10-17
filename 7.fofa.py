#/usr/bin/python3
# https://fofa.info/api/introd

import time
import sys
import requests
import json
from tabulate import tabulate

print('\n' + '*'*30 + "程序运行" + '*'*30 + '\n')
table = [["email/key", "api_url", "isvip", "vip_level"]]

urllist = ["https://fofa.info","https://g.fofa.info"]

def get_url_result(email, key, urllistint):
    get_url = urllist[urllistint] + "/api/v1/info/my?email={your_email}&key={your_key}"
    url = get_url.format(your_email=email, your_key=key)
    res = requests.get(url)
    results = json.loads(res.text)
    return results

def successkey(email, key, urllistint, results):
    results_data = email + ':' + key + ',' + urllist[urllistint] + ',' + str(results['isvip']) + ',' + str(results['vip_level'])
    print(results_data.split(","))
    table.append(results_data.split(","))

for key in open("key.txt"):
    email, key = key.strip().split(":")
    urllistint = 0
    results = get_url_result(email, key, urllistint)
    
    if results["error"] == False:
        successkey(email, key, urllistint, results)
    elif results["error"] == True:
        urllistint = 1
        results = get_url_result(email, key, urllistint)
        if results["error"] == False:
            successkey(email, key, urllistint, results)
        else:
            print(email + ', Error!')
    time.sleep(2)

print('\n' + '*'*30 + "程序结果" + '*'*30 + '\n')
test = '''
api_url: api地址
isvip: 是否是vip,
vip_level: 用户级别
'''
print(test + '\n' + '*'*30 + "程序结果" + '*'*30 + '\n')
print(tabulate(table, headers='firstrow'))


