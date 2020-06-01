import sys,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
import pandas as pd
file_to_fix="./data_recent_mmr/matches_list_ranking_0710_1000.csv"
with open(file_to_fix,encoding="utf-8") as f:
	x=f.readlines()
	len_str=str(len(x)-1)
print(len_str)
row_title=x[0]
row_title=["mid","time","radiant_team","dire_team","radiant_win"]
new_list=[]
print (row_title)
for line in x[1:]:
	one_line_list=line.split(" ")		
	new_oneline_list=[one_line_list[0][:-1]," ".join([one_line_list[1],one_line_list[2][:-1]]),one_line_list[3][:-1],one_line_list[4][:-1],one_line_list[5][:-1]]
	new_list.append(new_oneline_list)


df=pd.DataFrame(new_list,columns=row_title)
df.to_csv("exp_"+len_str+".csv",index=False)
"['5496024009,', '2020-07-02', '22:29:16,', '54,2,14,106,87,', '67,18,22,112,25,', 'False\n']"
