#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import sys,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
url = 'https://www.vpgame.com/schedule/dota/dotaS00007710'
headers = {'Host': 'www.vpgame.com', 'Connection': 'keep-alive', 'Cache-Control': 'max-age=0', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.88 Safari/537.36 Vivaldi/2.4.1488.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9'}
cookies = {'gr_user_id': '9c2ec6da-19af-4658-ad8c-4df34c82c77c', 'grwng_uid': '48068c2b-a51b-41b6-b552-a65219ef4cb1', 'VPLang': 'zh_CN', 'VPLang.sig': 'YnJ5rF9PQgOnWLVHGcoeKlgoy3E', 'Device-Id': '37c45e33c0febfb70f2cb94c4e9ea2a2', 'Device-Id.sig': 'DZNRiT7JF-n3lnS1ebFn4k1Fcdw', '__cfduid': 'defbbbc043ea77db39c59730378a9857b1596956292', '__auc': 'a651178f173d204a04ae3bcd16f', 'Hm_lvt_20c4cdf230856f4a4479a32ec8b13dd6': '1596956424', 'VPToken': 'Bearer+eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJiNzAzMjQyMC1kYTEwLTExZWEtYWJjMS1jZmU4Y2ZiMmE5YmQiLCJpYXQiOjE1OTY5NTc1OTEsIm5iZiI6MTU5Njk1NzU5MSwiZXhwIjoxNTk3NTYyMzkxLCJzdWIiOiIzMzczMTcifQ.QuuLr-Eu66Uej1-IkxmqOZDU_VQoqHuD0y10yIP4nuc', 'VPSessionID': 'a5hcsr76cp1ki9tf0ulh36t6v7', 'bd6e328645187581_gr_last_sent_cs1': '337317', 'VPTimeZone': 'Asia%2FChongqing', '_ym_uid': '15969576281059558296', '_ym_d': '1596957628', 'acw_tc': '76b20fe915983466037372164e4b4716e72cd4dcbb66366c3acbc789d86ae6', 'bd6e328645187581_gr_session_id': '8d622948-2441-420b-8918-b75ca917d04c', 'bd6e328645187581_gr_last_sent_sid_with_cs1': '8d622948-2441-420b-8918-b75ca917d04c', 'bd6e328645187581_gr_session_id_8d622948-2441-420b-8918-b75ca917d04c': 'true', 'VPSiteGame': 'dota', 'VPSiteGame.sig': 'MAA6LxiyZ5SeXC0K2-rIKbAXakQ', 'Hm_lpvt_20c4cdf230856f4a4479a32ec8b13dd6': '1598347085', 'bd6e328645187581_gr_cs1': '337317'}
data = {}

html = requests.get(url, headers=headers, verify=False, cookies=cookies)
print(len(html.text))
print(html.text)
