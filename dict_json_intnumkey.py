from json import load,dump,loads,dumps

with open ("hero_id_name.json","r+") as f:
    hero_dict=load(f)
x=list(hero_dict.items())
for i in x:
	t=int(i[0])
	c=i[1]
	hero_dict.update({t:c})
	hero_dict.pop(i[0])
# for i in range(129):
# 	t=str(i)
# 	try:
# 		hero_dict.pop(t)
# 	except:
# 		continue

a=dumps(hero_dict)
with open ("hero_id_name_id.json","w+") as f:
	f.write(a)



s="['dajhwjkewk','wkehkk',{1231,3},True]"
k=eval(s)
print (k)


a={1:3,4:5}
b={3:5,2:7}
print (a.update(b))
print (a)

c="[1,2,3,4]"
print (eval(c))