#/usr/bin/python3
import time
import shodan
from tabulate import tabulate


print('\n' + '*'*30 + "程序运行" + '*'*30 + '\n')
table = [["API_KEY", "scan_credits", "query_credits", "usage_limits_ips", "monitored_ips"]]
for key in open("key.txt"):
    api = shodan.Shodan(key.strip())
    try:
        results = api.info()    # GET https://api.shodan.io/api-info?key=xxx
        results_data = key.strip() + "," + str(results["scan_credits"]) + "," + str(results["query_credits"]) + "," + str(results["usage_limits"]["monitored_ips"]) + "," + str(results["monitored_ips"])
        print(results_data.split(","))
        table.append(results_data.split(","))
    except shodan.APIError as e:
        print(key.strip() + ',Error: {}'.format(e))
    time.sleep(1)

print('\n' + '*'*30 + "程序结果" + '*'*30 + '\n')
print("scan_credits: 剩余扫描积分", "\nquery_credits: 剩余查询积分",  "\nusage_limits_ips: 可监控IP数", "\nmonitored_ips: 已监控IP数")
print('\n' + '*'*30 + "程序结果" + '*'*30 + '\n')
print(tabulate(table, headers='firstrow'))