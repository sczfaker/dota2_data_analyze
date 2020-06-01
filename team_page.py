#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests

url = 'http://dotamax.com/match/tour_famous_team_list/'
headers = {'Host': 'dotamax.com', 'Connection': 'keep-alive', 'Cache-Control': 'max-age=0', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.88 Safari/537.36 Vivaldi/2.4.1488.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'Referer': 'http://dotamax.com/bets/index/', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'}
cookies = {'_ga': 'GA1.2.917068991.1593764201', '_gid': 'GA1.2.981710910.1593764201', 'Hm_lvt_575895fe09d48554a608faa5ef059555': '1593764202', 'csrftoken': 'PP0Xh0PvPbiSWlk7tzkeVaJf7Cc9gUPe', 'pkey': 'MTU5Mzc2ODE0My42MnNjel8wMDBfMnNjbHBlY2x3dGxzbnVrYWg__', '_gat': '1', 'Hm_lpvt_575895fe09d48554a608faa5ef059555': '1593768539'}
data = {}

html = requests.get(url, headers=headers, verify=False, cookies=cookies)
print(len(html.text))
print(html.text)
