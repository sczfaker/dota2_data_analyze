import os
from os import chdir,listdir
from re import compile,findall,search
from bs4 import BeautifulSoup
import json
import io,sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding="utf-8")

chdir("dota")
pattern_1=compile("primary-.*?")
pattern_2=compile("(agi|int|str)")
""
count=0
def abi():
	pass

items,hero={},{}
with open("cha_base_dic.txt","w+",encoding="utf-8") as f1,open("equi_base_dic.txt","w+",encoding="utf-8") as f2:
	for i in [xx for xx in listdir() if xx[:5]=="item_" or xx[:5]=="hero_" or xx[:6]=="detail"]:
		print (i)
		with open(i,"r+",encoding="utf-8") as f:
			need_to_clean=f.read()
			bs4_=BeautifulSoup(need_to_clean,"html.parser")
			if i[:5]=="hero_":
				z=bs4_.find(class_="hero-secondary-ability-icons r-none-mobile")
				ppp=z.find_all("img",alt=True)
				ability=[i.attrs["alt"] for i in ppp]
				link=z.find("a",href=True)["href"]
				pattern=compile("(?<= - ).*?(?= -)")
				t=search(pattern,bs4_.title.string).group()
				basic_=t.replace(" ","")
				talent=bs4_.find("table")
				talent=talent.find_all("td")
				talent_={}
				for j in range(10,30,5):
					talent_[j]=[]
				count,seed=0,25
				for j in talent:
					if j.string:
						if count%3==0:
							talent_[seed].append(j.string.strip())
						if count%3==2:
							talent_[seed].append(j.string.strip())
							seed-=5
					count+=1
				attr_=bs4_.find("section",class_="hero_attributes")
				primary_=attr_.find(class_=pattern_1)
				type_=primary_["class"]
				other_=attr_.find("table",class_="other")
				other_detail=other_.get_text().strip().split()
				base_=[(k['class'],k.get_text().strip()) for k in primary_.find_all("td",class_=pattern_2) if "\n\n"!=k.get_text() ]
				name_hero=i[5:-4]
				if name_hero not in hero:
					hero[name_hero]={}
					hero[name_hero]["ability"]=[]
				hero[name_hero]["type"]=str(type_)
				hero[name_hero]["ability"].append(ability)
				hero[name_hero]["talent"]=talent_
				hero[name_hero]["base"]=base_+other_detail
				hero[name_hero]["hotkey"]=[]
				hero[name_hero]["exp"]=[]



			if i[:5]=="item_":
				showdetail_=bs4_.find("div",attrs={"data-portable":"show-item-details"})
				price_=showdetail_.find("div",class_="price")
				price_=price_.find("span",class_="number")
				count+=1
				name_item=i[5:-4]
				if name_item not in items:
					items[name_item]={}
				name=showdetail_.find("div",class_="name")
				if name:
					items[name_item]["name"]=1
				items[name_item]["price"]=[]
				if price_:
					items[name_item]["price"].append(str(price_.get_text().strip()))
				attr_=showdetail_.find("div",class_="stats")
				items[name_item]["attr_"]=[]
				if attr_:
					items[name_item]["attr_"].append(str(attr_.get_text().strip().split()))
				to_=showdetail_.find("div",class_="item-build item-builds-into")
				items[name_item]["buildto"]=[]
				if to_:
					buildto=" ".join(to_.get_text().strip().split())
					items[name_item]["buildto"].append(buildto)
				from_=showdetail_.find("div",class_="item-build item-builds-from")
				items[name_item]["buildfrom"]=[]
				if from_:
					buildfrom=" ".join(from_.get_text().strip().split())
					items[name_item]["buildfrom"].append(buildfrom)
				des_=showdetail_.find("div",class_="description")
				if des_:
					items[name_item]["description"]=des_.get_text().strip().split()

			if i[:6]=="detail":
				name_hero=i[7:-4]
				if name_hero not in hero:
					hero[name_hero]={}
					hero[name_hero]["ability"]=[]
				block_=bs4_.find("div",class_="col-8")
				hero[name_hero]["ability"].append(block_.get_text().strip().split())

# t=open("hero.json","r+",encoding="utf-8")
# dic=load(t)
for i in hero:
	newdic_={}
	s_=" ".join(hero[i]['ability'][0])
	len_=len(hero[i]['ability'][1])
	t_=hero[i]['ability'][1]
	for j in range(len_):
		key=t_[j]
		if j==len_-1:
			newdic_[key]=None
			newdic_[key]=s_[s_.find(key)+len(key):]
			break
		newdic_[key]=s_[s_.find(key)+len(key):s_.find(t_[j+1])]
	# print (newdic_)
	hero[i]['ability'][0]=newdic_

he_=open("hero.json","w+")
# it_=open("item.json","w+")
json.dump(hero,he_)
# json.dump(items,it_)








