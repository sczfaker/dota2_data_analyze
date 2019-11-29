import io,sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding="utf-8")
import json
import os
os.chdir("dota")
dic=json.load(open("item.json","r"))

for i in dic:
	if "position" not in dic[i]:
		dic[i]["position"]=[]
	if dic[i]['price']:
		new=dic[i]["price"][0].replace(",","")
		dic[i].update({"price":new})



t=open("item.json","w+")
json.dump(dic,t)


