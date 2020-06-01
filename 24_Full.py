#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import sys,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

url = 'https://api.tuotu.live/api/front/schedule/match/5491169641?game_category=dota2'
headers = {'Host': 'api.tuotu.live', 'Connection': 'keep-alive', 'Accept': 'application/json, text/plain, */*', 'Origin': 'https://www.tuotugame.com', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.88 Safari/537.36 Vivaldi/2.4.1488.36', 'Referer': 'https://www.tuotugame.com/dota2/5ef8a98f4302e82c262a1ac2', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9'}
cookies = {}
data = {}

html = requests.get(url, headers=headers, verify=False, cookies=cookies)
print(len(html.text))
print(html.text)
