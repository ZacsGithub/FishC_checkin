import requests
import json
import os

Cookie = os.environ.get('cookies')

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41",
    "Host": "fishc.com.cn",
    "Connection": "keep-alive",
    'Referer' : 'https://fishc.com.cn/plugin.php?id=k_misign:sign',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'Cookie' : Cookie
    }


F = requests.get('https://fishc.com.cn/plugin.php?id=k_misign:sign', headers=headers)

print(F.status_code)
