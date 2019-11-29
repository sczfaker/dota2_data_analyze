from time import sleep
from requests import get
from json import dump,load,loads
from random import randint
import datetime
from fake_useragent import UserAgent

MATCH_JSON_DIR="MATCH_JSON_DIR"
class OpendotaReq(object):
	"""docstring for ClassName"""
	def __init__(self):
		#super(ClassName, self).__init__()
		self.ua = UserAgent()
		self.matchurl = "https://api.opendota.com/api/matches/"
		#self.playerurl = "https://api.opendota.com/api/players/"
		self.headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
		self.heroes="https://api.opendota.com/api/heroes"
		self.teams_id="https://api.opendota.com/api/teams/"
		self.teamid="https://api.opendota.com/api/teams/"
		self.headers={"user-agent":self.ua.random}
	def match_info(self,matchid):
		s=get(self.matchurl+matchid,headers=self.headers)
		print (s.status_code)
		if s.status_code==200:
			print (len(s.text))
			return s.text
	def account_info(self,accountid):
		s=get(self.playerurl+accountid,headers=self.headers)
		return s.text
	def get_hero_id(self):
		s=get(self.heroes,headers=self.headers)
		d=load(s.text)
		print (type(d))
		if s.status_code==200:
			with open (MATCH_JSON_DIR+"/"+"heroes_id.json","w+",encoding="utf-8") as f:
				dump(f,d,ensure_ascii=False)
		print (d)
	def get_team_id(self):
		s=get(self.teamid,headers=self.headers)
		d=load(s.text)
		if s.status_code==200:
			with open (MATCH_JSON_DIR+"/"+"team_id.json","w+",encoding="utf-8") as f:
				dump(f,d,ensure_ascii=False)
		print (d,len(d))		

instance=OpendotaReq()
if True:
	instance.get_team_id()

if False:
	instance.get_hero_id()

if False:
	with open("matchid_file_"+str(datetime.date.today())+".txt","r+") as f:
		matchid=[i.strip() for i in f.readlines()]
		print (len(matchid))
	num=0
	fail_id_list=[]
	with open (MATCH_JSON_DIR+"/"+"queue.txt","a+") as f:
		f.seek(0)
		queue_list=[i.strip() for i in f.readlines()]
		for m_id in matchid:
			if m_id not in queue_list:
				try:
					match_str=t.match_info(m_id)
					match_dict=loads(match_str)
					sleep(randint(1,3))
				except:
					fail_id_list.append(m_id)
					num+=1
					print("fail:",num)
					continue
				if match_dict:
					with open(MATCH_JSON_DIR+"/"+m_id+".json","w+",encoding="utf-8") as f_0:#open("myaccount.json","w+",encoding="utf-8") as f_a:
						dump(match_dict,f_0,ensure_ascii=False)
						print (m_id+" ok")
						queue_list.append(m_id)
						f.write(m_id+"\n")
			else:
				print ("already in queue.")
	print (len(matchid),len(queue_list))
	#account_str=t.account_info("226124774")
	#account_dict=loads(account_str)
#assert 1>2+#2print (s,s1)

		#dump(account_dict,f_a,ensure_ascii=False)
# if True:
# 	with open("data.json","r+",encoding="utf-8") as f,open("myaccount.json","r+",encoding="utf-8") as f_a:
# 		s=load(f)
# 		s1=load(f_a)
# 	for i in s:
# 		print (i)
