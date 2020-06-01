
from itertools import combinations,permutations
import itertools
for i in dir(itertools):
	print (help(i))

thdict={}
for i in range(1,6):
	thdict[i]=[]
print (thdict)
hero=["矮人直升机|工匠矮人5","谜团|元素术士5","巫妖|亡灵法师5","潮汐|娜迦猎人5","工程师|地精工匠5","船长|战士人类4","美杜莎|娜迦猎人4","圣堂|刺客精灵4",\
"光之守卫|法师人类4","炼金|地精术士4","dk|骑士人类龙4","利爪|德鲁伊野兽4","巨魔战将|战士巨魔4","末日守卫|战士恶魔4","死灵|亡灵术士4","干扰者|兽人萨满4","巫医|巨魔术士2","剑圣|战士兽人2",\
"影魔|恶魔术士3","火枪|矮人猎人3","幻影|刺客精灵3","斯拉克|娜迦刺客2","风行者|精灵猎人3","剃刀|法师元素3","火女|人类法师3","死亡|骑士亡灵3","全能|骑士人类3","灵魂守卫|恶魔猎手3","沙王|野兽刺客3",\
"剧毒|野兽术士3","狼人|战士人类野兽3","毒龙|龙刺客3","月骑|精灵骑士2","变体精灵|刺客元素2","痛苦女王|刺客恶魔2","冰女|法师人类2","混沌|骑士恶魔2","兽王|兽人猎人2","撕拉达|战士娜迦2","伐木机|地精工匠2","仙女|精灵龙法师2","先知|精灵德鲁伊2","大树|精灵德鲁伊2",\
"小小|战士元素1","发条|地精工匠1","海民|野兽战士1","小黑|亡灵猎人1","蓝胖|食人魔法师1","小鹿|野兽德鲁伊1","斧王|兽人战士1","赏金|地精刺客1","蝙蝠|巨魔骑士1","修补匠|地精工匠1","萨满|巨魔萨满1","敌法|精灵恶魔猎手1","隐刺|萨特刺客3","白虎|精灵猎人3","死亡先知|亡灵术士5"]
c="12345"
for i in hero:
	thdict[int(i[-1])].append(i[:i.find("|")])
for i in thdict:
	print (i,end=":")
	print (thdict[i],end="|||\n")

combo={1:[],2:[],3:[],6:[],9:[]}
print (combo)

un_occupations=["猎人hunter","人类human","亡灵deadghost","德鲁伊druidism",\
"战士warrior","骑士knight","矮人dwarf","地精goblin","工匠artisan","法师wiz\
zard","萨满shaman","野兽beast","兽人orc","元素element","刺客assasin","恶魔\
demon","恶魔猎手demonhunter","巨魔troll","术士warlock","食人魔eat","巫师"]

data_not_hash=[[100,0,0,0,0],[65,35,0,0,0],[65,35,5,0,0],[55,35,5,0,0],[40,35,23,2,0],[33,30,30,7,0],[30,30,30,10,0],[24,30,30,15,1],[0,0,0,0,0],[0,0,0,0,0]]

probability_model={}
for i in range(0,10):
	probability_model[str(i+1)+"级"]={}
	for j in range(5):
		probability_model[str(i+1)+"级"][j+1]=data_not_hash[i][j]

for i in probability_model:
	print(i,end="")
	print(probability_model[i],end="\n")




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
		if i.find("食人魔")!=-1:
			true_com_occpuations["食人魔eat"].append(i[:i.find("|")])

com_occpuations()

print(true_com_occpuations)
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


com6=[]

for i in thdict:
        if i==5:
                forcom=getoutpopulation(i)
                for choice in combinations(forcom,i):
                	com6.append(choice)

print (len(forcom))
print(len(com6))


# print (len([i for i in permutations(forcom,i)]))

#在职业组合里找每个组合

#在每个组合里找职业 找重复组合的公式(代码)
def getorc(h):#得到这个组合的职业
	return com












			# tmp_com[singlecom].append(i)






def d2():
	t1=7
	return

def decision(t,b=0,c=0,enemy=0):
	if t==1:
		return 1
	if t<=10 and t>=2:
		return 1
	if t>10 and t<=20:
		return 2
	if t>20 and t<=30:
		return 3
	if t>30:
		return 4



def Get_cost_fuc():
	recording_turn={}
	total=0
	rate=total*0.1
	flag1,flag2=False,False
	for i in range(1,41):#n轮循环每轮循环要  收入 购买 合成 卖出 摆放 
		recording_turn["回合"+str(i)]={"初始":total}
		if total%10==0 and total>=10:
			total+=(total%10)
		if i>3:
			total+=5
		else:
			total+=i
		recording_turn["回合"+str(i)]["开始"]=total
		turn=i
		cost=decision(turn)
		total-=cost
		recording_turn["回合"+str(i)]["结束"]=total

		if flag1==True:#胜负连胜连败
			total+=1

			
		if flag2==True:#利息一次性投资
			print (":")
			print ("")
			print (":")
			print (":")
			print (":")
			print (":")
			print (":")
			print (":")
	return recording_turn #返回一个每回合的战斗与决策分析,其中 胜负关系 财产 血量 目标阵列
a=Get_cost_fuc()


print (a)

"""
这段代码有Bug
"""
def max_add(A,lenth):
	if len(A)==1:
		return (A[0],mid-1,mid+1)
	mid=lenth/2
	lf_max,l_s_index,l_end_index=max_add(A[:mid],len(A[:mid]))
	rf_max,r_s_index,r_end_index=max_add(A[mid:],len(A[mid:]))
	cross_value,cross_index_l,cross_index_r=max_cross(A)
	max_s_index,min_e_index,=compare()
	return max_value,max_r_index,max_l_index




def zvdakrytia(svjiuuzu):
	ihdu=len(svjiuuzu)
	zozvda,zoxxbn=0
	for i in range(ihdu/2-1,-1,-1):
		ia=svjiuuzu[ihdu-1]-svjiuuzu[i]
		if ia>zozvda:
			zozvda,zoxxbn=ia,i
	yzzvda,yzxxbn=0
	for j in range(ihdu/2+1,ihdu):
		ia=svjiuuzu[j]-svjiuuzu[ihdu]
		if ia>yzzvda:
			yzzvda,yzxxbn=ia,j
	return zoxxbn,yzxxbn,yzxxbn+zoxxbn
