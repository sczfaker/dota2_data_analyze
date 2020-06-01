#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests

url = 'https://api.opendota.com/api/players/5390881/matches?limit=70&game_mode=1'
headers = {'Host': 'api.opendota.com', 'Connection': 'keep-alive', 'Cache-Control': 'max-age=0', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.88 Safari/537.36 Vivaldi/2.4.1488.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9'}
cookies = {'_ga': 'GA1.2.654318434.1592888382', '__cfduid': 'd6eccdc8731914f51dde26e1717f02e611593764220', '_gid': 'GA1.2.61074614.1593764226'}
data = {}

html = requests.get(url, headers=headers, verify=False, cookies=cookies)
print(len(html.text))
print(html.text)
