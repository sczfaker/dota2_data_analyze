import os,re,bs4,json
dic=json.load(open("data_in_json.json",encoding="utf-8"))
print (type(dic))

for i in os.listdir():
	if i[:4]=="hero":
		with open(i,"r+",encoding="utf-8") as f:
			content_hero=f.read()

t=open("data_in_json.json","w+",encoding="utf-8")
json.dump(new,t)