
from itertools import combinations


thdict={}
for i in range(2,11):
	thdict[i]={}
print (thdict)
hero=["矮人直升机|工匠矮人5","谜团|元素术士5","巫妖|亡灵法师5","潮汐|娜迦猎人5","工程师|地精工匠5","船长|战士人类4","美杜莎|娜迦猎人4","圣堂|刺客精灵4",\
"光之守卫|法师人类4","炼金|地精术士4","dk|骑士人类龙4","利爪|德鲁伊野兽4","巨魔战将|战士巨魔4","末日守卫|战士恶魔4","死灵|亡灵术士4","干扰者|兽人萨满4","巫医|巨魔术士2","剑圣|战士兽人2",\
"影魔|恶魔术士3","火枪|矮人猎人3","幻影|刺客精灵3","斯拉克|刺客3","风行者|精灵猎人3","剃刀|法师元素3","火女|人类法师3","死亡|骑士亡灵3","全能|骑士人类3","灵魂守卫|恶魔猎手3","沙王|野兽刺客3",\
"剧毒|野兽术士3","狼人|战士人类野兽3","毒龙|龙刺客3","月骑|精灵骑士2","变体精灵|刺客元素2","痛苦女王|刺客恶魔2","冰女|法师人类2","混沌|骑士恶魔2","兽王|兽人猎人2","撕拉达|战士娜迦2","伐木机|地精工匠2","仙女|精灵龙法师2","先知|精灵德鲁伊2","大树|精灵德鲁伊2",\
"小小|战士元素1","发条|地精工匠1","海民|野兽战士1","小黑|亡灵猎人1","蓝胖|食人魔法师1","小鹿|野兽德鲁伊1","斧王|兽人战士1","赏金|地精刺客1","蝙蝠|巨魔骑士1","修补匠|地精工匠1","萨满|巨魔萨满1","敌法|精灵恶魔猎手1"]



combo={1:[],2:[],3:[],6:[],9:[]}
print (combo)

un_occupations=["猎人hunter","人类human","亡灵deadghost","德鲁伊druidism",\
"战士warrior","骑士knight","矮人dwarf","好斗goblin","发明家artisan","法师wiz\
zard","萨满shaman","野兽beast","兽人orc","元素element","刺客assasin","恶魔\
demon","恶魔猎手demonhunter","巨魔troll","术士warlock",""]

true_com_occpuations={}
for i in un_occupations:
	true_com_occpuations[i]=[]
def com_occpuations():
	for i in hero:
		if i.find("猎人")!=-1:
			true_com_occpuations["猎人hunter"].append(i[:i.find("|")])
		if i.find("人类")!=-1:
			true_com_occpuations["人类human"].append(i[:i.find("|")])
		if i.find("亡灵")!=-1:
			true_com_occpuations["亡灵deadghost"].append(i[:i.find("|")])
		if i.find("德鲁伊")!=-1:
			true_com_occpuations["德鲁伊druidism"].append(i[:i.find("|")])
		if i.find("战士")!=-1:
			true_com_occpuations["战士warrior"].append(i[:i.find("|")])
		if i.find("骑士")!=-1:
			true_com_occpuations["骑士knight"].append(i[:i.find("|")])
		if i.find("矮人")!=-1:
			true_com_occpuations["矮人dwarf"].append(i[:i.find("|")])
		if i.find("地精")!=-1:
			true_com_occpuations["地精goblin"].append(i[:i.find("|")])
		if i.find("工匠")!=-1:
			true_com_occpuations["工匠artisan"].append(i[:i.find("|")])
		if i.find("萨满")!=-1:
			true_com_occpuations["萨满shaman"].append(i[:i.find("|")])
		if i.find("野兽")!=-1:
			true_com_occpuations["野兽beast"].append(i[:i.find("|")])
		if i.find("兽人")!=-1:
			true_com_occpuations["兽人orc"].append(i[:i.find("|")])
		if i.find("元素")!=-1:
			true_com_occpuations["元素element"].append(i[:i.find("|")])
		if i.find("刺客")!=-1:
			true_com_occpuations["刺客assasin"].append(i[:i.find("|")])
		if i.find("恶魔")!=-1:
			true_com_occpuations["恶魔demon"].append(i[:i.find("|")])
		if i.find("恶魔猎手")!=-1:
			true_com_occpuations["恶魔猎手demonhunter"].append(i[:i.find("|")])
		if i.find("巨魔")!=-1:
			true_com_occpuations["巨魔troll"].append(i[:i.find("|")])
		if i.find("术士")!=-1:
			true_com_occpuations["术士warlock"].append(i[:i.find("|")])
		if i.find("法师")!=-1:
			true_com_occpuations["法师wizzard"].append(i[:i.find("|")])
com_occpuations()


# for i in true_com_occpuations:
# 	print (i,end="")
# 	print("----------------------------",end="")
# 	print (true_com_occpuations[i])





def getoutpopulation(n):
	li=[]
	if n<=6:
		for i in hero:
			if int(i[-1])<=3:
				li.append(i[:i.find("|")])
	if n==7:
		for i in hero:
			if int(i[-1])<=4:
				li.append(i[:i.find("|")])
	if n>7:
		for i in hero:
			if int(i[-1])<=5:
				li.append(i[:i.find("|")])

	return li



# c=0
# for i in thdict:
# 	if i==6:
# 		forcom=getoutpopulation(i)
# 	    # for choice in combinations(forcom,i):
# 	    	# if c==100:
# 	    	# 	break
# 	    	# for j in choice:
# 	    	# # 	getherooc(j)
# 	    	# c+=1


def getherooc(h):
	for i in true_com_occpuations:
		if h in true_com_occpuations[i]:
			if h not in tmp_com[singlecom]:
				tmp_com[singlecom][i]=1
			else:
				tmp_com[singlecom][i]+=1




com9=[]
forcom=getoutpopulation(8)
c=500
for i in combinations(forcom,10):
	c+=1
	if c==520:
		break
	com9.append(i)
# print (com9)


com_strength={}
com_strength["输出能力"]={}
tmp_com={}
for singlecom in com9:
	tmp_com[singlecom]={}
	for i in singlecom:
		getherooc(i)
print (tmp_com)
print(tmp_com)
c=0
for i in tmp_com:
	c+=1
	print (str(c),end=":")
	print (i,end="")
	print (tmp_com[i])

def select_userful_com(com8):
	pass
