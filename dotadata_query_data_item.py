import json
import os
from re import compile,search
import io,sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
os.chdir(os.getcwd())
os.chdir("dota")
dic=json.load(open("item.json"))
# new_key=None

print ()
for i in dic:
	print (i)
	# print (dic[i]["price"])
	


# pattern=compile(".*(?=\()")
# t=price.split("\n")[1:-1]#[1:-1]]{i[0]:[",".join[i[1:]]]}
# newt=[i.split() for i in t]
# final=[{i[0]:i[1:]} for i in newt]
# print (len(final))
# # print (final)
# cc="bbb-"
# # print (search(pattern,cc).group())

# d=new_key.split("\n")
# dd=[i.split("::")[0] for i in d[:-1]]
# print (dd[10:20])


# ddd=[[search(pattern,i),i] for i in dd if "(" in i]
# dddd={}
# for i in ddd:
# 	try:
# 		c=i[0].group()
# 		dddd[c]=i[1]
# 	except:
# 		continue
# pairs={}
# for i in dic:
# 	if i in dddd:
# 		key=dddd[i]
# 		value=dic[i]
# 		pairs[key]=value
# for i in pairs:		
# 	dic.update({i:pairs[i]})
# for i in range(10):
# 	c=dic.popitem()
# 	print (c)



# for i in dic:
# 	print(i,end="::")
# 	# break
# 	# print (dic[i],end=":::")
# 	print (dic[i]["price"],end="")
# 	print (dic[i]["buildto"],end="")
# 	print (dic[i]["buildfrom"])


	# if i=="shivas-guard":
	# 	print (i,end="::")
	# 	print (dic[i])
	
	# print (i,end="------")
	# print (dic[i]["buildfrom"])

