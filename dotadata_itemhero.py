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
class Get_Item_and_Hero():
	def __init__(self):
		self.headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
		self.item_url="https://www.dotabuff.com/items"
		self.hero_url="https://www.dotabuff.com/heroes"
		self.item_key=self.get_item_eng_name()
		self.hero_key=self.get_hero_eng_name()
		self.df_hero=self.pd_hero()#创建空的
		self.df_item=self.pd_item()#创建空的
	def item_general_page(self):
		rr=requests.get(self.item_url,headers=self.headers)
		with open("dota_items_src.txt","w+",encoding="utf-8") as f:
			f.write(rr.text)
	def get_item_eng_name(self):
		with open("dota_items_src.txt","r+",encoding="utf-8") as f:
			str_html=f.read()
			item_key=findall("(?<=cell-icon\" data-value=\").*?(?=\")",str_html)
		new_key_with=[]
		for i in item_key:
			word=i.split(" ")
			if len(word)>1:
				new_word="-".join(word)
			else:
				new_word=word[0]
			new_word=new_word.lower()
			new_key_with.append(new_word)
		return new_key_with[:-6]
	def pd_hero(self):
		self.hero_attributes={"英雄名称":self.hero_key,"初始属性":[],"属性成长":[],"技能":[],"天赋树":[],"常规打法":[],"键位设置":[],"装备搭配":[],"英雄搭配":[]}
		df=pd.DataFrame.from_dict(dict([(k,pd.Series(v))for k,v in self.hero_attributes.items()]))#columns=["英雄名称","技能","天赋树","常规打法","键位设置","初始属性","属性成长"]
		df=df.set_index("英雄名称")
		df.to_csv("pd_hero.csv")
		return df
	def item_file(self):
		max_count=0
		for i in self.item_key:
			url="https://www.dotabuff.com/items"+"/"+i
			rr=requests.get(url,headers=self.headers)
			if rr.status_code==200:
				max_count+=1
				print ("物品:",max_count,i)
			else:
				with open("error_info.txt","w+",encoding="utf-8") as f:
					f.write("物品次数访问后被拒绝:"+str(max_count))
				continue
			text=BeautifulSoup(rr.text,"html.parser")
			with open("hero_item_datafile/item_"+i+".txt","w+",encoding="utf-8") as f:
				f.write(text.prettify())
			count=random.randint(2,5)
			sleep(count/5)
		return -1
	def fill_itemdata_intocsv(self):
		pd_csv_object=read_csv("pd_hero.csv")
	def fill_herodata_intocsv(self):
		pd_csv_object=read_csv("pd_item.csv")
	def hero_general_page(self):
		rr=requests.get(self.hero_url,headers=self.headers)
		with open("dota_hero_src.txt","r+",encoding="utf-8") as f:
			f.write(rr.text)
	def get_hero_eng_name(self):
		with open("dota_hero_src.txt","r+",encoding="utf-8") as f:
			str_hrml=f.read()
			hero_key=findall("(?<=name\">).*?(?=<)",str_hrml)
		new_key_with=[]
		for i in hero_key:
			word=i.split(" ")
			if len(word)>1:
				new_word="-".join(word)
			else:
				new_word=word[0]
			new_word=new_word.lower()
			new_key_with.append(new_word)
		return new_key_with
	def hero_file(self):#3.5*117 decorator
		max_count=0
		print(self.hero_key)
		for i in self.hero_key:
			url="https://www.dotabuff.com/heroes"+"/"+i
			rr=requests.get(url,headers=self.headers)
			if rr.status_code==200:
				max_count+=1
				print ("英雄:",max_count,i)
			else:
				with open("info.txt","w+",encoding="utf-8") as f:
					f.write("次数访问后被拒绝:"+str(max_count))
				continue
			text=BeautifulSoup(rr.text,"html.parser")
			with open("hero_item_datafile/hero_"+i+".txt","w+",encoding="utf-8") as f:
				f.write(text.prettify())
			sleep(random.randint(2,5)/5)
	def pd_item(self):
		self.hero_attributes={"物品名称":self.item_key,"物品作用":[],"价格":[],"合成":[],"组成":[],"购买时间":[],"英雄":[]}
		df=pd.DataFrame.from_dict(dict([(k,pd.Series(v))for k,v in self.hero_attributes.items()]))#columns=["英雄名称","技能","天赋树","常规打法","键位设置","初始属性","属性成长"]
		df=df.set_index("物品名称")
		df.to_csv("pd_item.csv")
		return df



def rename_to_stdname():
	for i in listdir():
		if i[:4]!="hero_" and i[:4]!="item_":
			tmp="item_"+i
			rename(i,tmp)
def get_basic_name_from_local():
	data_json={}
	for item,hero in zip_longest(item_key,hero_key):
		if hero:
			hero_="hero_"+hero
		if item:
			item_="item_"+item
		if item_ not in data_json:
			data_json[item_]={}
		if hero_ not in data_json:
			data_json[hero_]={}

	assert(len(data_json)==117+218)
	file_in_json=open("data_in_json.json","w+")
	json.dump(data_json,file_in_json)

def ability_detail(url):
	headers=\
	{
		"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
	}
	abi=get(url)
	BeautifulSoup(abi.text).prettify()

