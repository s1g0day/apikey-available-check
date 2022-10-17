#/usr/bin/python3

import time
from tabulate import tabulate
import zoomeye.sdk as zoomeye

print('\n' + '*'*30 + "程序运行" + '*'*30 + '\n')
table = [["api_key", "interval", "role", "expired_at", "remain_free_quota", "remain_pay_quota", "remain_total_quota"]]
for key in open("key.txt"):
    zm = zoomeye.ZoomEye()
    zm.api_key = key.strip()
    try:
        # resources_info 获取当前用户的信息
        results = zm.resources_info()
        results_data = zm.api_key + ',' + str(results['resources']['interval']) + ',' + str(results['user_info']['role']) + ',' + str(results['user_info']['expired_at']) + ',' + str(results['quota_info']['remain_free_quota']) + ',' + str(results['quota_info']['remain_pay_quota']) + ',' + str(results['quota_info']['remain_total_quota'])
        print(results_data.split(","))
        table.append(results_data.split(","))
    except ValueError as e:
        print(zm.api_key + ', Error: {}'.format(e))
    time.sleep(2)
print('\n' + '*'*30 + "程序结果" + '*'*30 + '\n')
print("interval: 额度更新周期", "\nrole: 服务级别", "\nexpired_at: 服务期限", "\nremain_free_quota: 剩余免费额度", "\nremain_pay_quota: 剩余充值额度", "\nremain_total_quota: 剩余总额度")
print('\n' + '*'*30 + "程序结果" + '*'*30 + '\n')
print(tabulate(table, headers='firstrow'))