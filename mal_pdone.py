import pandas as pd
from json import load,dump
with open ("MATCH_JSON_DIR_0726/"+"5321093000.json","r+",encoding="utf-8") as f:
	dic=load(f)
tfi=dic["teamfights"]
print (dic["game_mode"])
#for i in tfi:#
	# for j in i:
	# 	print (j,i[j])
	# break
for i in tfi:
	for j in i:
		print (j,i[j])