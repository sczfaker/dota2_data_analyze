
from os import chdir,listdir,rename
import requests
from requests import get
from bs4 import BeautifulSoup
from re import findall,compile,search
from random import randint
from time import sleep

"http://replay113.valve.net/570/3362113115_2087377833.dem.bz2"

#写个正则简化标题
def save_match_base_info(url):
	filepath=""
	matches={}
	headers=\
	{
		"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
	}
	page_obj=requests.get(url,headers=headers)
	page_content=page_obj.text	
	page_bs_obj=BeautifulSoup(page_content,"html.parser")
	title_raw=page_bs_obj.find("div",class_="header-content-title").get_text()
	abb=[i[0] for i in title_raw.split()[:-1]]+[title_raw.split()[-1]]
	abb_tit="".join(abb)
	state=page_bs_obj.find('span',class_="next")
	while state:
		page_obj=page_bs_obj.find('nav',class_="pagination")
		page_cur=page_obj.find("span",class_="page current")
		curpage=page_cur.get_text().strip()
		with open(abb_tit+"_page_"+curpage+".txt","w+",encoding="utf-8") as f:
			f.write(page_bs_obj.prettify())
			print("save"+curpage+"suc")
		nextpage=str(int(curpage)+1)
		next_tag=page_obj.find('a',attrs={'rel':'next'})
		next_href="https://www.dotabuff.com/"+next_tag['href']
		count=randint(2,7)
		sleep(count)
		page_obj=requests.get(next_href,headers=headers)
		page_content=page_obj.text	
		page_bs_obj=BeautifulSoup(page_content,"html.parser")
		state=page_bs_obj.find('span',class_="next")
	with open(abb_tit+"_page_"+nextpage+"(lastpage)"+".txt","w+",encoding="utf-8") as f:
		f.write(BeautifulSoup(page_bs_obj.text,"html.parser").prettify())
		print("save last page suc")


url="https://www.dotabuff.com/esports/leagues/10749-the-international-2019/series?original_slug=10749-the-international-2019"
url_2="https://www.dotabuff.com/esports/leagues/9870-the-international-2018/series"
save_match_base_info(url_2)








url_1="https://www.dotabuff.com/esports/leagues/10749-the-international-2019/series?original_slug=10749-the-international-2019"
url_2=""
