from os import chdir,listdir,rename
import requests
from requests import get
from bs4 import BeautifulSoup
from re import findall,compile,search
from random import randint
from time import sleep

url_pre="https://www.dotabuff.com"
with open("abi_links.txt","r+",encoding="utf-8") as f:
	url_=[i[:-1] for i in f.readlines()]
print (url_)

def ability_detail(url):
	headers=\
	{
		"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
	}
	for i in url_:
		url=url_pre+i
		name_=search(compile("(?<=/).*(?=/)"),i[1:]).group()
		abi=get(url,headers=headers)
		if abi.status_code==200:
			print ("ok "+name_)
			content_=BeautifulSoup(abi.text,"html.parser").prettify()
			with open("detail_"+name_+".txt","w+",encoding="utf-8") as f:
				f.write(content_)
		count=randint(2,7)
		sleep(count)

