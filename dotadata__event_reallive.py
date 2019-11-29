from os import getcwd,path,listdir,walk
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from json import load,dump
from requests import get
from io import BytesIO
from time import sleep
from PIL import Image


headers=\
{
	"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}

teams_and_players={}
def ajacentwith_ol(tag):
	return tag.next_siblings=="ol"

def getChengDumajorplayers():
	#从文章介绍中获取所有参赛选手的数据页面链接,然后获取数据页面,此函数可以获取0.2以上的选手信息
	url="https://www.dotabuff.com/blog/2019-11-14-mdl-chengdu-major-team-previews"
	preurl="https://www.dotabuff.com"
	ua.UserAgent()
	headers=\
	{
		"user-agent":ua.random
	}
	with open("teams_and_players_成都.txt","r+",encoding="utf-8") as f:
		seedtext_local=f.read()
		rpage_bs4object_local=BeautifulSoup(seedtext_local,"html.parser")
		div_tag_of_main=rpage_bs4object_local.find("div",class_="body")
		for team,teammates in zip(div_tag_of_main.find_all("h1"),div_tag_of_main.find_all("ol")):
			teamname=team.find("span",class_="team-text team-text-full").text.strip()
			teamlink=preurl+team.find("a",class_="object")["href"]
			teamlogo=team.find("img",class_="img-team img-tinyicon")["src"]
			teammates_link=[(atag.find("span",class_="player-text player-text-full").text.strip(),preurl+atag["href"]) for atag in teammates.find_all("a")]
			teams_and_players[teamname]={}
			teams_and_players[teamname]["队标"]=teamlogo
			teams_and_players[teamname]["队员"]=teammates_link
	with open("dotadata_tournament_成都.json","w+",encoding="utf-8") as f:
		dump(teams_and_players,f,ensure_ascii=False)


def handle_team_data():
	with open("dotadata_tournament_成都.json","r+",encoding="utf-8") as f:
		dic=load(f)
	for teamname in dic:
		online_link=dic[teamname]["队标"]
		img_request_object=get(online_link,headers=headers)
		image = Image.open(BytesIO(img_request_object.content))
		captcha=image.convert('RGB')
		captcha.save("major_"+teamname+'.jpg')
		sleep(2.5)
			#f.write(img_request_object.content)
			
handle_team_data()
def handle_team_data():
	with open("dotadata_tournament_成都.json","r+",encoding="utf-8") as f:
		dic=load(f)






"dota