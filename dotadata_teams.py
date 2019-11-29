class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
	def get_teampage_from_dotabuff(self):
		self.team_info_page="teaminfo_page.txt"
		url=self.url+self.tour_keywords['teams']
		print (url)
		req_object=requests.get(url,headers=self.headers,timeout=30)
		with open(self.team_info_page,"w+",encoding="utf-8") as f:
			f.write(req_object.text)
			print("save file ok")
	def team_info(self):
		with open(self.team_info_page,"r+",encoding="utf-8") as f:
			t_base_content=f.read()
			bs4_object=BeautifulSoup(t_base_content,"html.parser")
		teams_table_object=bs4_object.find("table",class_="table sortable table-striped table-condensed r-tab-enabled")
		tbody=teams_table_object.find("tbody")
		tr_list=tbody.find_all("tr")
		team_names=[]
		for i in tr_list:
			team_names.append(i.find("span",{"class":"team-text team-text-full"}))
		team_info={i.get_text():{"team_mates":{},"team_current_states":{"skill":{},"potential":{},"demand":{},"lower_bound":{}},"possibles":{},"heros_preference":{}} for i in team_names}
		with open ("team_info.json","w+",encoding="utf-8") as f:
			dump(team_info,f)