from dota_base_info_dota import creep,tower,wilding,callcreep
import sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding="utf-8")
base_info={}


attr=['攻击力','攻击速度','攻击范围','生命值','护甲','视野','移动速度']
for i in creep:
	base_info[i]={}
	base_info[i]["name"]=i
	base_info[i]["exp"]=creep[i][2][0]
	base_info[i]["gold"]=[creep[i][0],creep[i][1]]
	base_info[i]["attr"]={}
	for j in attr:
		base_info[i]["attr"][j]=None
	base_info[i]["type"]="A"

attr=['攻击力','攻击速度','攻击范围','视野','生命值','护甲','移动速度']
for i in tower:
	base_info[i]={}
	base_info[i]["name"]=i
	base_info[i]["exp"]=[]
	base_info[i]["gold"]=[tower[i][0],tower[i][1]]
	base_info[i]["attr"]={}
	for j in attr:
		base_info[i]["attr"][j]=None
	base_info[i]["type"]="D"

attr=['攻击力','攻击速度','攻击范围','视野','生命值','护甲','移动速度']
for i in wilding:
	base_info[i]={}
	base_info[i]["name"]=i
	base_info[i]["exp"]=wilding[i][-1]
	base_info[i]["gold"]=[wilding[i][0],wilding[i][1]]
	base_info[i]["attr"]={}
	for j in attr:
		base_info[i]["attr"][j]=None	
	base_info[i]["type"]="B"
attr=['攻击力','攻击速度','攻击范围','视野','生命值','护甲','移动速度']
for i in callcreep:
	base_info[i]={}
	base_info[i]["name"]=i
	base_info[i]["exp"]=callcreep[i][-1]
	base_info[i]["gold"]=[callcreep[i][0]]
	base_info[i]["attr"]={}
	base_info[i]["type"]="C"

	for j in attr:
		base_info[i]["attr"][j]=None


for i in base_info:
	print (i,end=":")
	print (base_info[i]['exp'])