#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests

url = 'https://www.raybet1.com/match/37243802'
headers = {'Host': 'www.raybet1.com', 'Connection': 'keep-alive', 'Cache-Control': 'max-age=0', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.88 Safari/537.36 Vivaldi/2.4.1488.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'Referer': 'https://www.raybet.club/', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9'}
cookies = {'visid_incap_1701736': 'ZeKFNDMdTmC/ZTeyyea3uG52BV8AAAAAQUIPAAAAAAA5baLt8/aynBTv6blwgKdq', '_ga': 'GA1.2.1398916668.1594193519', 'incap_ses_962_1701736': 'CzI5TGaieE5A0j0u9bVZDUarJl8AAAAAaM41sl3aIyifeM5JqTH//Q', 'incap_ses_625_1701736': 'Gf1KWeIJWFsxhOf0QnKsCDDBJl8AAAAAM3RSxUzyKdwv5dWBIVh5uw', 'incap_ses_1044_1701736': 'c88VY4TwBmGhc+mZigh9DvvZKl8AAAAA7vk7wXhvzTGgUNLClxoFhw', 'incap_ses_1045_1701736': 'q4a/DXtV+Cxf+wjrBpaADrYcK18AAAAABC+3m4pM/9GuOadJGEdzzw', 'incap_ses_573_1701736': 'pcahUB2gGkez3MXGi7TzB9Q9K18AAAAAaCQgOVSO7z0ZLw/FZvJ+GQ', 'incap_ses_956_1701736': 'QsJEW1zQ5gVIjCb4AWVEDYr3Ll8AAAAAJR3KSXqQZESh6a+gD9RouQ', '_gid': 'GA1.2.539561965.1596913548', 'incap_ses_795_1701736': 'jofpFkEcg3CR20YKWmgIC8P3Ll8AAAAAKa2kPrn9d7R1n/m5dnxkXQ', 'incap_ses_1047_1701736': 'BX/TUskKYExJOB3oAbGHDmOwL18AAAAAVfGYE2WyC3TSA3b+EIN66g'}
data = {}

html = requests.get(url, headers=headers, verify=False, cookies=cookies)
html.encoding="utf-8"
print(len(html.text))
print(html.text)
