def phisical_armer(_damage,life,*kg):
	armdata=0
	print (kg)
	for i in kg[0]:
		armdata+=i
	print (armdata)
	d_1=0.052*armdata/(0.9+0.048*abs(armdata))
	d_2=13*armdata	/(225+12*abs(armdata	))
	# if d_2>0:
	# 	actual=d_2*_damage
	# if d_2<0:
	# 	actual=_damage-(_damage*(d_2))
	d=_damage*(1-d_2)
	resist=life/(1-d_2)
	return resist,d


def phisical_armer_final(_damage,life,kg):
	armdata=0
	print (kg)
	for i in kg:
		armdata+=kg[i]
	print (armdata)
	d_1=0.052*armdata/(0.9+0.048*abs(armdata))
	d_2=13*armdata	/(225+12*abs(armdata	))
	# if d_2>0:
	# 	actual=d_2*_damage
	# if d_2<0:
	# 	actual=_damage-(_damage*(d_2))
	d=_damage*(1-d_2)
	resist=life/(1-d_2)
	return resist,d

print (phisical_armer_final(500,1000,{"a":-9,"b":-5,"c":-6}))
