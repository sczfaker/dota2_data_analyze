from re import findall,compile,match
from os import chdir,listdir,rename
from json import load,dump,loads
from itertools import combinations

class Match_stat(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.match_catalog="MATCH_JSON_DIR"
		self.match_files = [file for file in listdir(self.match_catalog) if file[-4:]=="json" and match("\d{10,}",file[:-5])]
		with open(self.match_catalog+"/"+"hero_id_name.json","r+") as f:
			self.hero_id_name=load(f)
		self.match={}
		self.team_ana={}
		self.afight={}
		self.r_pick_score=0
		self.d_pick_score=0
		self.heao_value_measure={}
	def iterate_file(self):
		for match in self.match_files:
			with open (self.match_catalog+"/"+match,"r+",encoding="utf-8") as f:
				dict_match=load(f)
			#print (dict_match["game_mode"])
			if dict_match["game_mode"]==2:
				self.match[match[:-5]]=dict_match
		# with open(self.match_catalog+"/"+"captain_mode_matches.json","w+",encoding="utf-8") as f:
			# dump(self.match,f)
		print (len(self.match))
	def d(self):
		for i in self.match:
			r,d=self.match[i]["dire_team_id"],self.match[i]["radiant_team_id"]
			if r not in self.team_ana:#
				self.team_ana[r]={}
			if d not in self.team_ana:
				self.team_ana[r]={}
		for afight in combinations(self.team_ana.keys(),2):
			self.afight[afight]={}
		print (len(self.afight))
	def get_heroid_content(self):
		self.hero_id={}
		with open(self.match_catalog+"/"+"heroes.json") as f:
			hero_id_content=load(f)
		for hero in hero_id_content:
			self.hero_id[hero["id"]]=hero["localized_name"].replace(" ","-").lower()
		# with open(self.match_catalog+"/"+"hero_id_name.json","w+") as f:
		# 	dump(self.hero_id,f)
	def performance_measure(self,test_set):
		total,t,f=len(test_set),0,0
		for i in test_set:
			if self.all_match_bp(i):
				t+=1
			else:
				f+=1
		accurate_rate=t/total
		return accurate_rate
	def all_match_bp(self):
		ban_pick_result={}
		for match in self.match:
			p,direid,rid=self.match[match]["picks_bans"],self.match[match]["dire_team_id"],self.match[match]["radiant_team_id"]
			win_object=lambda:"radiant" if self.match["randiant_win"] else "dire"
			amatch_combination={"dire":[],"rand":[]}
			for i in p:
				if i["is_pick"]==True:
						hero_id=i["hero_id"]
						hero_name=self.hero_id_name[str(hero_id)]
						if i["team"]==1:
							amatch_combination["dire"].append(hero_name)
						else:
							amatch_combination["rand"].append(hero_name)
			ban_pick_result[match]={"sequence":p,"diretid":direid,"rid":rid,"win_object":win_object,"combination":amatch_combination}
		for i in ban_pick_result:
			print (i)
			print (ban_pick_result[i]["combination"])
		#求二分组合后的二分排列
		#求二分组后的子集,求10的子集,求10,<5的子集
		#创造特征向量([1,1,0,1,1,0])
		#根据特征向量的值决定预测值
		#调整特征向量的取值决定,调整特征向量本身

	def build_team_hero_dict(self):
		a=0
		for i in self.team_ana:
			self.team_ana[i]={}
			a=i
			for j in self.hero_id:
				self.team_ana[i][self.hero_id[j]]=50
		return #输的一方时间越长 经验值越高 潜力越大 赢的一方时间越短经验值越低 潜力越小 时间越长 经验值越高
		#强队选大团控提高胜率,弱队选大团控加快输的速度
	def feture_vector_space(self):
		
		return
	def match_duration(self):
		return
	def match_team(self):
		return


 
instance=Match_stat()
instance.iterate_file()
instance.d()
instance.get_heroid_content()
instance.build_team_hero_dict()
#instance.all_match_bp()
# x=instance.get_heroid_content()
# print (x)
