import os
import time
for i in os.listdir("MATCH_JSON_DIR_0727"):
	time_judge=os.stat("MATCH_JSON_DIR_0727/"+i).st_mtime
	print (time.localtime(time_judge))
	stimeobject=time.localtime(time_judge)
	if stimeobject[2]==4 and i[-4:]=="json" and i[:6]!="normal":
		os.rename("MATCH_JSON_DIR_0727/"+i,"MATCH_JSON_DIR_0727/"+"normalmatch_"+i)
	# print(dir(stimeobject))
		# print (i)
