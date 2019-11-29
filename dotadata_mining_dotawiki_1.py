from os import chdir,listdir,rename
import requests
from requests import get
from bs4 import BeautifulSoup
from re import findall,compile
headers=\
{
	"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}
url_1="https://dota2-zh.gamepedia.com/小兵"
rr=requests.get(url_1,headers=headers)
if rr.status_code==200:
	chdir("dota")
	with open("tips"+".txt","w+",encoding="utf-8") as f:
		text=BeautifulSoup(rr.text,"html.parser")		
		f.write(text.prettify())


