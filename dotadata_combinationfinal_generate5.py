from itertools import combinations
from os import path,listdir
from time import time
from json import dump
import pandas as pd
import os	
def path_hero_item_file():
	mainpath="D:\\cl\\reqdotadata"
	#os.chdir(mainpath+"\\dataset\\")
	if not os.path.exists("combination_data"):
		os.mkdir("combination_data")
	t=pd.read_csv("pd_hero.csv")
	heros=t['英雄名称'].tolist()
	item_df=pd.read_csv("pd_hero.csv")
	items=item_df['物品名称'].tolist()
	return heros,items
def get_combination_hero():
	picks={}
	file_count=0
	RAM_storage=7000000
	pick_count=0
	for pick in combinations(heros,5):
		start_time=time()
		pick_count+=1
		picks[str(pick)]=0
		if pick_count>=RAM_storage:
			end_time=time()
			print("迭代写入7e6条数据用时:",abs(start_time-end_time),"秒")
			with open("heropicks"+"_"+str(file_count)+".json","w+",encoding="utf-8") as f:
					dump(picks,f)
			file_count+=1
			picks={}
			pick_count=0
			start_time=time()
	with open("hero_picks"+"_"+str(file_count)+".json","w+",encoding="utf-8") as f:
		dump(picks,f)


def get_combination_item():
	picks={}
	file_count=0
	RAM_storage=7000000
	pick_count=0
	for pick in combinations(items,9):
		start_time=time()
		pick_count+=1
		picks[str(pick)]=0
		if count>=RAM_storage:
			with open("item"+"_"+str(file_count)+".json","w+",encoding="utf-8") as f:
					dump(picks,f)
			end_time=time()
			print("迭代写入7e6)用时:",start_time-end_time,"秒")
			file_count+=1
			picks={}
			pick_count=0
	with open("item"+"_"+str(file_count)+".json","w+",encoding="utf-8") as f:
		dump(picks,f)		

if __name__=='__main__':
	heros=path_hero_item_file()
	get_combination_hero()