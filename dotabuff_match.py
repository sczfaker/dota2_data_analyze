#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import sys,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
url = 'https://www.dotabuff.com/matches/5496310819'
headers = {'Host': 'www.dotabuff.com', 'Connection': 'keep-alive', 'Cache-Control': 'max-age=0', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.88 Safari/537.36 Vivaldi/2.4.1488.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'Referer': 'https://www.dotabuff.com/players/92607797', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9'}
cookies = {'_tz': 'Asia%2FShanghai', '_ga': 'GA1.2.961090768.1592724898', '__qca': 'P0-368302978-1592724902240', '__gads': 'ID', '_ym_uid': '1590651080726563724', '_ym_d': '1592724907', 'pbjs-id5id': '%7B%22ID5ID%22%3A%22ID5-ZHMOrDEaxifVhvRNRZHJiq0L_-oXr7wWsAZNImUX5g%22%2C%22ID5ID_CREATED_AT%22%3A%222020-06-21T07%3A35%3A25.74Z%22%2C%22ID5_CONSENT%22%3Atrue%2C%22CASCADE_NEEDED%22%3Atrue%2C%22ID5ID_LOOKUP%22%3Atrue%2C%223PIDS%22%3A%5B%5D%7D', '_gid': 'GA1.2.590241721.1593564884', '_ym_isad': '2', '_ym_visorc_52686388': 'w', 'pbjs-id5id_last': 'Sat%2C%2004%20Jul%202020%2014%3A55%3A37%20GMT', '_s': 'TnRxSWNIY0VNdTBiaHI1NkFQRmFUa2JUdncrWmZRWWFrTnBHZ2VMUEttc01CZElDMy83aTVBYldqK0IxNCtueDk4NE0vdXVlVnd1RmI5bkd2YjMvRmZYUE8wc1pZaWp6TmFDSWdxMEZWVng2YmU1RWVncmNWQm1LUjVZS1Jxc2JsNmQzNUtTZnMxNkNzcDltWmZSSit1MzNEQmhxeVpaOWVLU3pTc1o1dlh0Y1hZendFNnl0UTZ5ckQ0dnNGVEVuLS0yNE51SHpXWHlEanFzWWlBcndCbWRRPT0%3D--0c2fb3b20691720d55da197d0b17605f996f716f', '_hi': '1593876164185'}
data = {}

html = requests.get(url, headers=headers, verify=False, cookies=cookies)
print(len(html.text))
print(html.text)
