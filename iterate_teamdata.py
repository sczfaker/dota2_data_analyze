from os import chdir,listdir,rename
from fake_useragent import UserAgent

from json import load,dump,loads
from requests import get
from time import sleep
from re import findall,compile,match
import sys,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')




import d2api
# api = d2api.APIWrapper("0EDC80399A001A7ECA91DB1B41F194EB")
# x=api.get_match_details("5493469070")
# print (x)


# with open ("normal_match_info.json","r+",encoding="utf-8") as f:
    # dict_match=load(f)
# print (len(dict_match))
# for i in dict_match:
    # print (len(dict_match[i]))
    # for j in dict_match[i]:
        # print (len(dict_match[i][j]))

# for i in x:
    # print (x[i])
# import dota2api
# api = dota2api.Initialise("0EDC80399A001A7ECA91DB1B41F194EB")
# # hist = api.get_match_history(account_id=41231571)
# match = api.get_match_details(match_id="5493469070")
# for i in match:
#   print (i)
# print (match)
class ClassName(object):
    """docstring for ClassName"""
    def __init__(self):
        self.match_catalog="MATCH_JSON_DIR_0727/"
        # self.match_files  = [file for file in listdir(self.match_catalog) if file[-4:]=="json" and match("\d{10,}",file[:-5])]
        self.match_normal= [file for file in listdir(self.match_catalog) if file[-4:]=="json" and file[:6]=="normal"]
        # self.match_normal=[]
        self.match_files=self.match_normal#+self.match_files
        print (len(self.match_files))
        self.c=0
        for match_file in self.match_files:
            with open(self.match_catalog+match_file,"r+",encoding="utf-8") as f:
                dic_one_match=load(f)
            #if 1:   #assert dic_one_match["radiant_team"]
            # if dic_one_match["game_mode"]==2:
            #     self.c+=1
            # elif 1:
            try:
                assert dic_one_match["radiant_team"]
                print (len(dic_one_match["radiant_team"].split(",")),len(dic_one_match["radiant_team"].split(",")))
                self.c+=1
            except:
                continue
import pandas as pd

# df=pd.read_csv("matches_0727.csv")
# df_test=pd.read_csv("matches_testset_0727.csv")
# dfx=df.append(df_test)
# print (len(dfx),len(df),len(df_test))

d=ClassName()
print (d.c)
# x=[i["hero_id"] for i in match["picks_bans"] if i["is_pick"]==True]
# print (x)


