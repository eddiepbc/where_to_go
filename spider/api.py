import json
import random
from time import sleep
from urllib.parse import quote
import requests


def get(url):
    header = {
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
    }
    # sleep(random.randint(0,5))
    try:
        return requests.get(url, timeout=10, headers=header)
    except:
        return requests.get(url, timeout=10, headers=header)


# 智联招聘取列表的接口
def getList(cityid, kw, start, length):
    kw = quote(kw, 'utf-8')

    url = 'https://fe-api.zhaopin.com/c/i/sou?start=' + str(start) + '&pageSize=' + str(length) + '&cityId=' + str(cityid) + \
           '&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=' + str(kw) + \
           '&kt=3&_v=0.75444261&x-zp-page-request-id=7635cfbfaff04028938973231acd5f62-1571628525277-679520&x-zp-client-id=51f95334-32ed-4165-9886-f7212333d7cf'

    print('getList of cityid:' + str(cityid) + ',kw=' + str(kw) + ',success')
    print(get(url))
    try:
        return json.loads(get(url).text)
    except:
        return {'code': 0}
