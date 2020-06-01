from requests import get
import sys,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
from bs4 import BeautifulSoup


import re
url_allpick="https://api.opendota.com/api/players/72312627/matches?limit=70&game_mode=3"
headers = {'Host': 'api.opendota.com', 'Connection': 'keep-alive', 'Cache-Control': 'max-age=0', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.88 Safari/537.36 Vivaldi/2.4.1488.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9'}
headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
req_object_allpick=get(url_allpick,headers=headers,verify=False)
print (req_object_allpick.status_code)
import chardet
# x=str(req_object_allpick.content.,"utf-8")

# req_object_allpick.encoding="utf-8"
# print (chardet.detect(req_object_allpick.content).get("encoding"))

dd=req_object_allpick.text.encode(req_object_allpick.encoding).decode("utf-8")
with open ("x.txt","w+",encoding="utf-8") as f:
    f.write(dd)

# print (req_object_allpick.text)
# print (req_object_allpick.json())
# req_object_allpick.content.decode("").encode("utf-8")
# print (req_object_allpick.text)
#from itertools import zip_longest
#a,b=[{1:2},{1:4},{1:6},{1:7}],[{1:3},{1:8},{1:4}]
#for i,j in zip_longest(a,b):
#    print (i[1],j[1])

with open("F:\\cl\\reqdotadata\\MATCH_JSON_DIR_0727\\normalmatch_5493138300.txt","r+",encoding="utf-8") as f:
    needto_extract_10_hero=f.read()
    bs4_object=BeautifulSoup(needto_extract_10_hero,"html.parser")
    print (len(needto_extract_10_hero))
    block_twoside=bs4_object.find_all("article",class_=re.compile("(r-tabbed-table|d-tabbed-table)"))
    for block in block_twoside:
        side_hero=block.find_all("a",href=re.compile("/heroes/.{1,}(?!abilities)"))                
        cside_hero=[i for i in side_hero if i["href"].split("/")[-1]!="abilities"]
        for i in side_hero:
            print (i["href"])
x="/heroes/silencer/abis"



x=re.match("/heroes/(\w|-){1,}(?!abis)",x).group()
print ("没有匹配",x)
