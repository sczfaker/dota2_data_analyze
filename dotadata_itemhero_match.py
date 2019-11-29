from os import chdir,listdir,rename
from fake_useragent import UserAgent
from itertools import zip_longest
from re import findall,compile
from bs4 import BeautifulSoup
from random import randint
from requests import get
from time import sleep
from json import dump
import pandas as pd
import datetime
import requests
import random
import json
import re
pattern="(?=)(?<=)"
#match_basic_url是一组dotabuff或者其他数据平台的,replayurl输入是比赛规划的新闻字符串或者网页
class Tournament_Plan(object):
	def __init__(self):
		self.match_basic_url=[]
		self.replayurl=[]
		self.pr_match=""
		self.ua=UserAgent()
		self.headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
		self.page_num=1
	def get_data_from_dotabuff(self):
		pass
class Tournament_id_dotabuff(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.page_num=1
		self.ua = UserAgent()
		self.league_record=[]
		self.next_url=None
		self.urlbasic="https://www.dotabuff.com/"
		self.headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
		self.teamfight_url="https://www.dotabuff.com/esports/leagues/11831-weplay-pushka-league/series"
		self.dpl="https://www.dotabuff.com/esports/leagues/11898-2020-dpl-cda-dota2/"
		#self.teamfight_url="https://www.dotabuff.com/esports/leagues/11831-weplay-pushka-league/series"#"https://www.dotabuff.com/esports/leagues/11898-2020-dpl-cda-dota2/series"
		#self.teamfight_url="https://www.dotabuff.com/esports/leagues/11975-amd-sapphire-oga-dota-pit-china-region/series"
		self.teamfight_url="https://www.dotabuff.com/esports/leagues/11370-dota2/series"
		self.current_url=self.teamfight_url
		self.tour_keywords={"heroes":"heroes","picks":"picks","teams":"teams","drafts":"drafts","players":"players"}
		self.dotamax_url_weplay="http://dotamax.com/match/tour_league_overview/?league_id=11975"
		self.dotamax_url_pit="http://dotamax.com/match/tour_league_overview/?league_id=11831"

		self.gamers_without_borders="https://www.dotabuff.com/esports/leagues/12028-gamers-without-borders/series"
		self.dpl_cda="https://www.dotabuff.com/esports/leagues/11898-2020-dpl-cda-dota2/series"
		self.pit_eu="https://www.dotabuff.com/esports/leagues/11974-amd-sapphire-oga-dota-pit-eu-cis-region/series"
		count_dpl,count_gwb,count_piteu=0,0,0
		self.getmatchid_url={"GWB":[self.gamers_without_borders,count_gwb],"dpl":[self.dpl_cda,count_dpl],"pit_eu":[self.pit_eu,count_piteu]}#,
	def get_data_from_dotabuff(self):
		req_obejct=get(self.url,headers=self.headers)		
		with open("weplay-$70704_20200506.txt","w+",encoding="utf-8") as f:
			f.write(req_obejct.text)
	def get_each_match(self):
		for league in self.getmatchid_url:
			self.teamfight_url=self.getmatchid_url[league][0]
			self.current_url=self.teamfight_url
			print ("当前主URL:",self.current_url)
			while self.next_url or self.teamfight_url:
				team_fight={}
				## 检测 数据 更新 差了 几天 , 如果 查了很多天 就要更新了 更新代码在下面
				# day_of_get_teamfight_page="2020_04_23_team_fights"
				day_of_get_teamfight_page=str(datetime.date.today()).replace("-","_")+"_team_fights"
				try:
					req_object=requests.get(self.current_url,headers=self.headers,timeout=30)
				except:
					print ("team figth page error.")
				with open(day_of_get_teamfight_page+".txt","w+",encoding="utf-8") as f:
					f.write(req_object.text)
				with open(day_of_get_teamfight_page+".txt","r+",encoding="utf-8") as f:
					bs4_obejct=BeautifulSoup(f.read(),"html.parser")
					tbody=bs4_obejct.find("tbody")
					tr_obejct_list=tbody.find_all("tr")
				if_next_page=bs4_obejct.find("span",class_="next")			
				rigth_tr=[]
				print ("tr总数需筛选",len(tr_obejct_list))
				for i in tr_obejct_list:
					content=i.find_all("a",attrs={"title":compile("Series \d{7,}")})
					if content and len(content)==1:
						seriesid,serieslink=content[0]["title"],content[0]["href"]
						rigthcontent=i
						rigth_tr.append([seriesid,serieslink,rigthcontent])
				matches_url=[]
				for i in rigth_tr:
					try:
						judge=i[2].find_all("a",attrs={"rel":"tooltip"})
						if judge:
							for link in judge:
								 if "trackdota" in link["href"]:
								 	#href="/"+"/".join(link['href'].split("/")[-2:])
								 	print(link["href"])
								 	print("数据错误 trackdota")
								 elif "esports" in link["href"]:
								 	print (link["href"])
								 	print ("数据错误 esports")
								 else:
								 	href=link['href']
								 	matches_url.append([i[0],i[1],href,href.split("/")[-1]])
					except:
						continue
				print(matches_url)
				print ("当页总比赛数",len(matches_url))
				print (self.getmatchid_url[league][1])
				self.getmatchid_url[league][1]+=len(matches_url)
				#matches_url=[[url[0],self.urlbasic+url[1],self.urlbasic+url[2]] for url in matches_url]
				matches_id=[url[3] for url in matches_url]
				print ("比赛数字id集:",matches_id,len(matches_id))
				print ("当前页数",self.page_num)
				with open("matchid_file_"+str(datetime.date.today())+".txt","a+") as f:
					f.seek(0)
					ifexist=[i.strip() for i in f.readlines()]
					print ("此页比赛数,",len(ifexist))
					for i in matches_id:
						if i not in ifexist:
							f.write(i+"\n")
				if if_next_page:
					self.next_url=self.urlbasic+if_next_page.a["href"]
					self.current_url=self.next_url
					self.teamfight_url=None
					self.page_num+=1
				else:
					self.teamfight_url,self.next_url=None,None
			aleague="|".join([league,"比赛数量",str(self.getmatchid_url[league][1])])
			self.league_record.append(aleague)
		for le in self.league_record:
			print (le)

class Tournament_id_dotamax(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.weplay = "http://dotamax.com/match/tour_league_overview/?league_id=11831"
		self.pit="http://dotamax.com/match/tour_league_overview/?league_id=11975"
	def get_match_id(self):
		self.x=x
	def get_team_name(self):
		pass
	def get_player_name(self):
		pass

if __name__ == '__main__':
	instance_t=Tournament_id_dotabuff()
	#instance_t.get_data_from_dotabuff()
	instance_t.get_each_match()

#print (matches_url)
# for match in matches_url:
# 	try:
# 		self.headers={"user-agent":self.ua.random}
# 		matchid=match[2].split("/")[-1]
# 		if not re.match("\d{8,}",matchid):
# 			break
# 		# print (matchid,type(matchid))
# 		with open ("dplcda_matches/dpl_matches_queue.txt","a+",encoding="utf-8") as f_queue:
# 			f_queue.seek(0)
# 			queue_list=f_queue.readlines()
# 			url_linebreak=match[2]+"\n"
# 			print(url_linebreak,"当前页数",self.page_num)
# 			if url_linebreak not in queue_list:
# 				sleep(random.randint(5,12))	
# 				req_object=requests.get(match[2],headers=self.headers,timeout=30)
# 				print("当前状态码",req_object.status_code,len(req_object.text))
# 				if req_object.status_code!=200:
# 					#print (req_object.status_code,match[2])
# 					assert 1>2,"request too many maybe."
# 				try:
# 					with open("dplcda_matches/"+i[0]+"_"+matchid+".txt","w+",encoding="utf-8") as f:
# 						f.write(req_object.text)
# 					f_queue.write("\n"+match[2])
# 				except:
# 					print (matchid,"filename error",i[0])
# 					continue
# 			else:
# 				print ("already crawled page match.")
# 	except:
# 		print ("fail one url")
# 		continue
# 	print("ok")