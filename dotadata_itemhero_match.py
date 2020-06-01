

print ("excute!")
from os import chdir,listdir,rename
from fake_useragent import UserAgent
from itertools import zip_longest
from re import findall,compile
from bs4 import BeautifulSoup
from random import randint
from requests import get
from time import sleep
from json import dump
import pandas as pd
import datetime
import requests
import random
import json
import re
import time
# from time import strptime,mktime
pattern="(?=)(?<=)"
# match_basic_url是一组dotabuff或者其他数据平台的,replayurl输入是比赛规划的新闻字符串或者网页
#模拟
class Tournament_id_dotabuff(object):
    """docstring for ClassName"""
    def __init__(self):
        self.page_num=1
        self.ua = UserAgent()
        print (self.ua.random)
        self.league_record=[]
        self.matchid_0726=[]
        self.time_limit="2020-06-30 08:54:01"#版本更新比赛的日期格式
        self.time_limit=time.strptime(self.time_limit,"%Y-%m-%d %H:%M:%S")
        self.time_to_compare=time.mktime(self.time_limit)
        self.next_url=None
        self.urlbasic="https://www.dotabuff.com/"
        self.headers={"user-agent":self.ua.random}
        self.teamfight_url="https://www.dotabuff.com/esports/leagues/11831-weplay-pushka-league/series"
        self.dpl="https://www.dotabuff.com/esports/leagues/11898-2020-dpl-cda-dota2/"
        #self.teamfight_url="https://www.dotabuff.com/esports/leagues/11831-weplay-pushka-league/series"#"https://www.dotabuff.com/esports/leagues/11898-2020-dpl-cda-dota2/series"
        #self.teamfight_url="https://www.dotabuff.com/esports/leagues/11975-amd-sapphire-oga-dota-pit-china-region/series"
        self.teamfight_url="https://www.dotabuff.com/esports/leagues/11370-dota2/series"
        self.dpl="https://www.dotabuff.com/esports/leagues/12139-2020-dpl-cda-s2-dota2-s2/series"
        self.pit="https://www.dotabuff.com/esports/leagues/12182-amd-sapphire-oga-dota-pit-china/series"
        self.asian_gold="https://www.dotabuff.com/esports/leagues/11382-asian-dota2-gold-occupation-competition/series"
        self.one_runtime_newmatch=0
        self.arena_blood=""
        count_dpl,count_arena,count_pit=0,0,0
        # self.getmatchid_url={"GWB":[self.gamers_without_borders,count_gwb],"dpl":[self.dpl_cda,count_dpl],"pit_eu":[self.pit_eu,count_piteu],"berg":[self.berg_eu,count_berg],"esllos":[self.esl_los,count_esllos],"blast":[self.blast_eu,count_blast],"epic_eucn":[self.epic_eucn,count_eucn]}#,
        self.getmatchid_url={"dpl2":[self.dpl,count_dpl],"OGApit":[self.pit,count_pit],"asian_gd":[self.asian_gold,count_arena]}
        print (self.getmatchid_url)
    def get_live_matchid(self):
        self.matchurl="https://www.dotabuff.com/esports"
    def get_match_info(self):
        pass
    def htmltime_to_strptime(self,time_htmlpage):
        """time format 时间格式"""
        # struct_time_limit=time.strptime(self.time_limit,"%Y-%m-%d %H:%M:%S")
        day_format=time_htmlpage.split("T")
        time_format=day_format[1].split("+")[0]
        match_time_day=" ".join([day_format[0],time_format])
        struct_match_time_day=time.strptime(match_time_day,"%Y-%m-%d %H:%M:%S")
        return struct_match_time_day#struct_time_limit
    def Match_from_player(self):
        from dotadata_findteamate import TeamMate
        instance=TeamMate()
    def get_each_match(self):
        for league in self.getmatchid_url:
            self.teamfight_url=self.getmatchid_url[league][0]
            self.current_url=self.teamfight_url
            print ("当前主URL:",self.current_url)
            while self.next_url or self.teamfight_url:
                team_fight={}
                ## 检测 数据 更新 差了 几天 , 如果 查了很多天 就要更新了 更新代码在下面
                # day_of_get_teamfight_page="2020_04_23_team_fights"
                day_of_get_teamfight_page=str(datetime.date.today()).replace("-","_")+"_team_fights"
                #print (10)
                #break
                try:
                    req_object=requests.get(self.current_url,headers=self.headers,timeout=30)#cookies=self.cookies
                except:
                    print ("team figth page error.")
                with open(day_of_get_teamfight_page+".txt","w+",encoding="utf-8") as f:
                    f.write(req_object.text)
                with open(day_of_get_teamfight_page+".txt","r+",encoding="utf-8") as f:
                    bs4_obejct=BeautifulSoup(f.read(),"html.parser")
                    tbody=bs4_obejct.find("tbody")
                    tr_obejct_list=tbody.find_all("tr")
                if_next_page=bs4_obejct.find("span",class_="next")          
                rigth_tr=[]
                print ("tr总数需筛选",len(tr_obejct_list))
                for tr_seri_obj in tr_obejct_list:
                    content=tr_seri_obj.find_all("a",attrs={"title":compile("Series \d{7,}")})
                    if content and len(content)==1:
                        seriesid,serieslink=content[0]["title"],content[0]["href"]
                        rigthcontent=tr_seri_obj
                        rigth_tr.append([seriesid,serieslink,rigthcontent])
                matches_url=[]

                outdated=False
                for i in rigth_tr:
                    try:
                        one_seri_content=i[2].find_all("a",attrs={"rel":"tooltip"})
                        if one_seri_content:
                            for link in one_seri_content:
                                 if "trackdota" in link["href"]:
                                    #href="/"+"/".join(link['href'].split("/")[-2:])
                                    print(link["href"])
                                    print("数据错误 trackdota")
                                 elif "esports" in link["href"]:
                                    print (link["href"])
                                    print ("数据错误 esports")
                                 else:
                                    href=link['href']
                                    one_matchid=href.split("/")[-1]
                                    urlprefix="https://www.dotabuff.com/matches/"
                                    try:
                                        fullurl=urlprefix+one_matchid
                                        print ("legal url",fullurl)
                                        headers = {'Host': 'www.dotabuff.com', 'Connection': 'keep-alive', 'Cache-Control': 'max-age=0', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.88 Safari/537.36 Vivaldi/2.4.1488.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9'}
                                        cookies = {'_tz': 'Asia%2FShanghai', '_ga': 'GA1.2.961090768.1592724898', '__qca': 'P0-368302978-1592724902240', '__gads': 'ID', '_ym_uid': '1590651080726563724', '_ym_d': '1592724907', 'pbjs-id5id': '%7B%22ID5ID%22%3A%22ID5-ZHMOrDEaxifVhvRNRZHJiq0L_-oXr7wWsAZNImUX5g%22%2C%22ID5ID_CREATED_AT%22%3A%222020-06-21T07%3A35%3A25.74Z%22%2C%22ID5_CONSENT%22%3Atrue%2C%22CASCADE_NEEDED%22%3Atrue%2C%22ID5ID_LOOKUP%22%3Atrue%2C%223PIDS%22%3A%5B%5D%7D', '_s': 'ZUUyb0ZqNzU1SldBSklybk5yWUk2UzZDL0ViTGNaMVpiZzFhcmkzMXYvQUZPSWwrbkY3WjZralJrcy9vMEdaeFVJa0psUW5tb21vOUpYYnVFUFVVTHNiRjErRGhOZkE1QVBiejNDeUxDcmUzZWplVS9KZDJ5dW5VL296NWJkc2N5Wk01dG9ROFM3TEF1Qll4cWpMa0dOVkI5K3RHYmxCTVZkT0Y0a0lXaVJkOXRxS3lrUmNLVlhrYXVrUUpBSzFoLS15OFJwUkJKWFVJSzF1Qm1OZ3Vsa1h3PT0%3D--ac927341bcffe876cc4f814411d07ae4e96c3637', '_gid': 'GA1.2.590241721.1593564884', '_ym_isad': '2', 'pbjs-id5id_last': 'Thu%2C%2002%20Jul%202020%2009%3A28%3A11%20GMT', '_ym_visorc_52686388': 'w', '_hi': '1593694438452'}
                                        req_match_object=get(fullurl,headers=headers,cookies=cookies,timeout=40,verify=False)
                                        sleep(2,randint(4,6))
                                        match_content=req_match_object.text
                                        with open(day_of_get_teamfight_page+".txt","w+",encoding="utf-8") as f:
                                            f.write(req_object.text)
                                        with open(day_of_get_teamfight_page+".txt","r+",encoding="utf-8") as f:
                                            bs4_obejct=BeautifulSoup(f.read(),"html.parser")
                                        bs4_match_content=BeautifulSoup(match_content,"html.parser")
                                        match_time=bs4_match_content.find("time")["datetime"]
                                        matchtime=self.htmltime_to_strptime(match_time)
                                        print (self.time_to_compare,time.mktime(matchtime))
                                        if matchtime>self.time_to_compare:
                                            matches_url.append([i[0],i[1],href,one_matchid])
                                            print (one_matchid,"go into crawl list.")
                                        else:
                                            print ("outdated match,left match are outdated from now:",one_matchid)
                                            outdated=True
                                            break
                                    except:
                                        assert 1>2,"get url time error"
                    except:
                        assert 1>2,"get match page id error"
                    if outdated==True:
                        break
                outdated=False
                print(matches_url)
                print ("当页总比赛数",len(matches_url))
                print (self.getmatchid_url[league][1])
                self.getmatchid_url[league][1]+=len(matches_url)
                #matches_url=[[url[0],self.urlbasic+url[1],self.urlbasic+url[2]] for url in matches_url]
                matches_id=[url[3] for url in matches_url]
                print ("当前页数",self.page_num,":比赛数字id集:",matches_id,len(matches_id))
                with open("matchid_file_"+str(datetime.date.today())+".txt","a+") as f:
                    f.seek(0)
                    ifexist=[i.strip() for i in f.readlines()]
                    print ("此页比赛数,",len(ifexist))
                    for i in matches_id:
                        if i not in ifexist:
                            f.write(i+"\n")
                            self.one_runtime_newmatch+=1
                        else:
                            print ("match in:",i)
                if if_next_page:
                    self.next_url=self.urlbasic+if_next_page.a["href"]
                    self.current_url=self.next_url
                    self.teamfight_url=None
                    self.page_num+=1
                    self.teamfight_url,self.next_url=None,None
            aleague="|".join([league,"比赛数量",str(self.getmatchid_url[league][1])])
            self.league_record.append(aleague)
        for le in self.league_record:
            print (le)
        print ("新增比赛id队列数:",self.one_runtime_newmatch)

# class Tournament_id_dotamax(object):
#   """docstring for ClassName"""
#       super(ClassName, self).__init__()
#       self.weplay = "http://dotamax.com/match/tour_league_overview/?league_id=11831"
#       self.pit="http://dotamax.com/match/tour_league_overview/?league_id=11975"
#   def get_match_id(self):
#       self.x=x
#   def get_team_name(self):
#       pass
#   def get_player_name(self):
#       pass

if __name__ == '__main__':
    import sys,io
    # sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
    print ("excute!")
    instance_t=Tournament_id_dotabuff()
    #instance_t.get_data_from_dotabuff()
    instance_t.get_each_match()

#print (matches_url)
# for match in matches_url:
#   try:
#       self.headers={"user-agent":self.ua.random}
#       matchid=match[2].split("/")[-1]
#       if not re.match("\d{8,}",matchid):
#           break
#       # print (matchid,type(matchid))
#       with open ("dplcda_matches/dpl_matches_queue.txt","a+",encoding="utf-8") as f_queue:
#           f_queue.seek(0)
#           queue_list=f_queue.readlines()
#           url_linebreak=match[2]+"\n"
#           print(url_linebreak,"当前页数",self.page_num)
#           if url_linebreak not in queue_list:
#               sleep(random.randint(5,12)) 
#               req_object=requests.get(match[2],headers=self.headers,timeout=30)
#               print("当前状态码",req_object.status_code,len(req_object.text))
#               if req_object.status_code!=200:
#                   #print (req_object.status_code,match[2])
#                   assert 1>2,"request too many maybe."
#               try:
#                   with open("dplcda_matches/"+i[0]+"_"+matchid+".txt","w+",encoding="utf-8") as f:
#                       f.write(req_object.text)
#                   f_queue.write("\n"+match[2])
#               except:
#                   print (matchid,"filename error",i[0])
#                   continue
#           else:
#               print ("already crawled page match.")
#   except:
#       print ("fail one url")
#       continue
#   print("ok")