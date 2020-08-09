
a=[1,2,3,4,5,6,7]
b=[3,4,5,11]
c=set(a).difference(set(b))
print (c)
aset=set(a)
bset=set(b)

#discard

print (aset.discard(set({1,2})))
print (aset)

#intersection
print (aset.intersection(bset))


with open("matchid_file_2020-10-03.txt","r+",encoding="utf-8") as f:
	x=set(f.readlines())
print (len(x))

#union
print (aset.union(bset))