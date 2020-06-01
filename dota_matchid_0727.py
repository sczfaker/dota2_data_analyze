print ("excute!")
from os import chdir,listdir,rename
from fake_useragent import UserAgent
from itertools import zip_longest
from re import findall,compile
from bs4 import BeautifulSoup
from random import randint
from requests import get
from time import sleep
from json import dump,load
import pandas as pd
import datetime
import requests
import random
import json
import os
import re
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# import sys,io 
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

# from time import strptime,mktime
pattern="(?=)(?<=)"
# match_basic_url是一组dotabuff或者其他数据平台的,replayurl输入是比赛规划的新闻字符串或者网页
#模拟
class Tournament_id_dotabuff(object):
    """docstring for ClassName"""
    def __init__(self):
        self.match_tier1,self.match_tier2,self.match_tier3,self.match_tier4=[],[],[],[]
        self.page_num=1
        self.ua = UserAgent()
        print (self.ua.random)
        self.league_record=[]
        self.matchid_0726=[]
        self.time_limit="2020-07-10 08:54:01"#版本更新比赛的日期格式
        self.next_url=None
        self.urlbasic="https://www.dotabuff.com/"
        self.headers={"user-agent":self.ua.random}
        self.teamfight_url="https://www.dotabuff.com/esports/leagues/11831-weplay-pushka-league/series"
        self.dpl="https://www.dotabuff.com/esports/leagues/11898-2020-dpl-cda-dota2/"
        self.teamfight_url="https://www.dotabuff.com/esports/leagues/11370-dota2/series"
        self.dpl="https://www.dotabuff.com/esports/leagues/12139-2020-dpl-cda-s2-dota2-s2/series"
        self.pit="https://www.dotabuff.com/esports/leagues/12182-amd-sapphire-oga-dota-pit-china/series"
        #self.asian_gold="https://www.dotabuff.com/esports/leagues/11382-asian-dota2-gold-occupation-competition/series"
        self.parimatch="https://www.dotabuff.com/esports/leagues/12175-parimatch-league-season-3-play-offs/series"
        self.ONE_Esports_Dota2_SEA_League="https://www.dotabuff.com/esports/leagues/12069-one-esports-dota-2-sea-league/series"
        self.The_Great_American_Rivalry="https://www.dotabuff.com/esports/leagues/12116-the-great-american-rivalry/series"
        # session=requests.session
        # session.cookies=cookielib.LWPCookieJar(filename='cookies')
        # session.cookies
        self.pit_na="https://www.dotabuff.com/esports/leagues/12183-amd-sapphire-oga-dota-pit-na-latam/series"#https://liquipedia.net/dota2/Dota_Pit_League/Online/2/Americas
        self.moon_aisa="https://www.dotabuff.com/esports/series?league_tier=professional_plus"
        self.one_runtime_newmatch=0
        #self.arena_blood=""
        count_dpl,count_ONE_Esports_Dota2_SEA_League,count_pit=0,0,0
        count_pit_na=0
        count_GAR=0
        count_parimatch=0
        count_moon_aisa=0
        self.DIR="MATCH_JSON_DIR_0727"
        # self.getmatchid_url={"GWB":[self.gamers_without_borders,count_gwb],"dpl":[self.dpl_cda,count_dpl],"pit_eu":[self.pit_eu,count_piteu],"berg":[self.berg_eu,count_berg],"esllos":[self.esl_los,count_esllos],"blast":[self.blast_eu,count_blast],"epic_eucn":[self.epic_eucn,count_eucn]}#,
        #"asian_gd":[self.asian_gold,count_arena]
        #"Parimatch":[self.parimatch,count_parimatch]
        self.getmatchid_url={"dpl2":[self.dpl,count_dpl],"OGApit":[self.pit,count_pit],"SEA":[self.ONE_Esports_Dota2_SEA_League,count_ONE_Esports_Dota2_SEA_League],"GAR":[self.The_Great_American_Rivalry,count_GAR],"count_pit_na":[self.pit_na,count_pit_na],"moon_aisa":[self.moon_aisa,count_moon_aisa]}
        print (self.getmatchid_url)
    def delete_outdated_data(self):
        league_id=[11382]
    def Tournament_preview(self):
        update_mainpage=True
        dict_tournament={"ongoing":{},"upcoming":{},"recent":{}}
        with open("Tournaments_Preview.json","r+",encoding="utf-8") as f:
            dict_tournament=load(f)
        tournament_page_html=str(datetime.date.today()).replace("-","_")+"tournament_page"    
        if update_mainpage:
            self.tournament_page="https://liquipedia.net/dota2/Portal:Tournaments"
            req_object=requests.get(self.tournament_page,headers=self.headers,timeout=30)
            with open(tournament_page_html+".txt","w+",encoding="utf-8") as f:
                f.write(req_object.text)
                print("write new page ok.")
        with open(tournament_page_html+".txt","r+",encoding="utf-8") as f:
            bs4_obejct=BeautifulSoup(f.read(),"html.parser")
            upcoming_ongogin=bs4_obejct.find_all("h3")
            print (len(upcoming_ongogin))
            upcoming_ongogin_tag=[]
            for tag in upcoming_ongogin[:3]:
                table=tag.next_sibling.next_sibling
                upcoming_ongogin_tag.append(table.div)
        # print (upcoming_ongogin_tag)
        prefix="https://liquipedia.net/"
        for type_tag,tag in enumerate(upcoming_ongogin_tag):
            div_row=tag.find_all("div",class_="divRow")
            div_hea=tag.find("div",class_="divHeaderRow")
            title_list=div_hea.find_all("divCell")
            print ("tag长度不对",len(div_row))
            print (type_tag)
            for one_row in div_row:
                dict_info_tour={}
                one_attr_list=one_row.find_all("div",class_=re.compile("divCell.{10,}"))
                tournament_headtag=one_attr_list[0].find("b").find("a")
                tournament_link,title=tournament_headtag["href"],tournament_headtag.get_text()
                full_url=prefix+tournament_link
                date=one_attr_list[1].get_text()
                pricepoul=one_attr_list[2].get_text()
                pricepoul="".join(pricepoul[1:].split(","))
                # print ("金额:",pricepoul)
                if pricepoul:
                    pricepoul=int(pricepoul)
                # print (pricepoul)
                team_num=one_attr_list[3].get_text()
                location=one_attr_list[4].span.get_text()
                dict_info_tour["date"]=date
                dict_info_tour["pricepoul"]=pricepoul
                dict_info_tour["team_num"]=team_num
                dict_info_tour["location"]=location
                dict_info_tour["url"]=full_url
                if type_tag==0:
                    dict_tournament["upcoming"][title]=dict_info_tour
                elif type_tag==1:
                    dict_tournament["ongoing"][title]=dict_info_tour
                elif type_tag==2:
                    dict_tournament["recent"][title]=dict_info_tour
        # print (len(dict_tournament["upcoming"]),len(dict_tournament["ongoing"]),len(dict_tournament["recent"]))
        with open("Tournaments_Preview.json","w+",encoding="utf-8") as f:
            dump(dict_tournament,f,ensure_ascii=True)
                # tr_obejct_list=tbody.find_all("tr")

    def get_live_matchid(self):
        self.matchurl="https://www.dotabuff.com/esports"
    def get_match_info(self):
        pass
    def htmltime_to_strptime(self,time_htmlpage):
        struct_time_limit=time.strptime(self.time_limit,"%Y-%m-%d %H:%M:%S")
        day_format=time_htmlpage.split("T")
        time_format=day_format[1].split("+")[0]
        match_time_day=" ".join([day_format[0],time_format])
        struct_match_time_day=time.strptime(match_time_day,"%Y-%m-%d %H:%M:%S")
        return struct_time_limit,struct_match_time_day
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
                    req_object=requests.get(self.current_url,headers=self.headers,timeout=30)
                except:
                    print ("team fight page error.")
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
                        time_bs4_object=i[2].find("time")['datetime']
                        print ("系列赛时间:",time_bs4_object)
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
                                        print ("legal url:",fullurl)
                                        ctime,matchtime=self.htmltime_to_strptime(time_bs4_object)
                                        print (time.mktime(ctime),time.mktime(matchtime))
                                        if matchtime>ctime:
                                            matches_url.append([i[0],i[1],href,one_matchid])
                                        else:
                                            print ("此时间后的比赛已过期:",one_matchid)
                                            outdated=True
                                            break
                                    except:
                                        assert 1>2,"get url time error"
                    except:
                        assert 1>2,"get match page id error"
                    if outdated==True:
                        break
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
                            print ("match already in:",i)
                if if_next_page and not outdated:
                    self.next_url=self.urlbasic+if_next_page.a["href"]
                    self.current_url=self.next_url
                    self.teamfight_url=None
                    self.page_num+=1
                else:
                    self.teamfight_url,self.next_url=None,None
            aleague="|".join([league,"比赛数量",str(self.getmatchid_url[league][1])])
            self.league_record.append(aleague)
        for le in self.league_record:
            print (le)
        print ("新增比赛id队列数:",self.one_runtime_newmatch)
    def clean_normal_banpick(self):
        self.match_normal= [file for file in listdir(self.DIR) if file[-4:]=="json" and file[:6]=="normal"]#file[:-5].split("_")[-1]
        #self.headers = {'Host': 'www.dotabuff.com', 'Connection': 'keep-alive', 'Cache-Control': 'max-age=0', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.88 Safari/537.36 Vivaldi/2.4.1488.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'Referer': 'https://www.dotabuff.com/players/92607797', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9'}
        cookies = {'_tz': 'Asia%2FShanghai', '_ga': 'GA1.2.961090768.1592724898', '__qca': 'P0-368302978-1592724902240', '__gads': 'ID', '_ym_uid': '1590651080726563724', '_ym_d': '1592724907', 'pbjs-id5id': '%7B%22ID5ID%22%3A%22ID5-ZHMOrDEaxifVhvRNRZHJiq0L_-oXr7wWsAZNImUX5g%22%2C%22ID5ID_CREATED_AT%22%3A%222020-06-21T07%3A35%3A25.74Z%22%2C%22ID5_CONSENT%22%3Atrue%2C%22CASCADE_NEEDED%22%3Atrue%2C%22ID5ID_LOOKUP%22%3Atrue%2C%223PIDS%22%3A%5B%5D%7D', '_gid': 'GA1.2.590241721.1593564884', '_ym_isad': '2', '_ym_visorc_52686388': 'w', 'pbjs-id5id_last': 'Sat%2C%2004%20Jul%202020%2014%3A55%3A37%20GMT', '_s': 'TnRxSWNIY0VNdTBiaHI1NkFQRmFUa2JUdncrWmZRWWFrTnBHZ2VMUEttc01CZElDMy83aTVBYldqK0IxNCtueDk4NE0vdXVlVnd1RmI5bkd2YjMvRmZYUE8wc1pZaWp6TmFDSWdxMEZWVng2YmU1RWVncmNWQm1LUjVZS1Jxc2JsNmQzNUtTZnMxNkNzcDltWmZSSit1MzNEQmhxeVpaOWVLU3pTc1o1dlh0Y1hZendFNnl0UTZ5ckQ0dnNGVEVuLS0yNE51SHpXWHlEanFzWWlBcndCbWRRPT0%3D--0c2fb3b20691720d55da197d0b17605f996f716f', '_hi': '1593876164185'}
        self.total_count=0
        for one_file in self.match_normal:
            # with open (self.DIR+"/"+one_file,"r+",encoding="utf-8") as f:
            #     dict_f=load(f)    
            try:
                if os.path.exists(self.DIR+"/"+str(one_file.split(".")[0])+".txt")==False:
                    match_id=one_file[:-5].split("_")[-1]
                    self.urlbasic="https://www.dotabuff.com/matches/"+match_id
                    print (self.urlbasic)
                    req_object=get(self.urlbasic,headers=self.headers,verify=False,timeout=30)#cookies=cookies
                    print(req_object.status_code)
                    sleep(randint(3,7))
                    with open(self.DIR+"/"+str(one_file.split(".")[0])+".txt","w+",encoding="utf-8") as f:
                        f.write(req_object.text)
                        self.total_count+=1
                        print ("write",match_id,"OK.",self.total_count)
            except:
                print ("miss one match.",str(one_file.split(".")[0]))
                continue
                # assert len([picks["is_pick"] for picks in dict_f["picks_bans"] if picks["is_pick"]==True])==10,"need to crawl on dotabuff."
                # radiant,dire=[],[]
                # for picks in dict_f["picks_bans"]:
                #     if picks["is_pick"]==True:
                #         if picks["team"]==0:
                #             radiant.append(picks["hero_id"])
                #         else:
                #             dire.append(picks["hero_id"])
                # assert len(radiant)==5 and len(dire)==5
        print (self.total_count)
    def confirm(self):
        print ("start...confirm")
        match_normal= [file for file in listdir(self.DIR) if file[-4:]==".txt" and file[:6]=="normal" and os.stat(self.DIR+"/"+file).st_size<3000]#file[:-5].split("_")[-1]
        # self.headers = {'Host': 'www.dotabuff.com', 'Connection': 'keep-alive', 'Cache-Control': 'max-age=0', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.88 Safari/537.36 Vivaldi/2.4.1488.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'Referer': 'https://www.dotabuff.com/players/92607797', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9'}
        print ("这么多json txt都需要补充:",len(match_normal))
        count=0
        for one_file in match_normal:
            if os.stat(self.DIR+"/"+one_file).st_size<3000:
                match_id=one_file.split(".")[0].split("_")[-1]
                self.urlbasic="https://www.dotabuff.com/matches/"+match_id
                print (self.urlbasic)
                self.headers={"user-agent":self.ua.random}
                # s=requests.Session()
                # r=s.get(self.urlbasic+'/cookies',headers=self.headers)
                # print (r.text)
                req_object=get(self.urlbasic,headers=self.headers,verify=False,timeout=30)#cookies=cookies
                sc=req_object.status_code
                if sc==200:
                    sleep(randint(3,7))
                    print(len(req_object.text),len(match_normal),count)
                    with open(self.DIR+"/"+str(one_file.split(".")[0])+".txt","w+",encoding="utf-8") as f:
                        f.write(req_object.text)
                        print ("write",match_id,"OK.")
                        count+=1
                else:
                    print(len(req_object.text))
                    sleep(randint(30,60))
                    print ("write",match_id,"not OK.")
                    continue                    
    def update_normal_randint_dire_to_match_json(self):
        print ("start update_normal_randint_dire_to_match_json")
        self.success_count=0
        self.already_count=0
        normal_text_need_clean=[file for file in listdir(self.DIR) if file[-4:]==".txt" and file[:6]=="normal" and os.stat(self.DIR+"/"+file).st_size>5000]#file[:-5].split("_")[-1]
        print("待检验和清洗长度team picks:",len(normal_text_need_clean))
        # with open("hero_id_name.json","r+",encoding="utf-8") as f:
            # dict_id_hero=load(f)  
        with open("hero_name_id.json","r+",encoding="utf-8") as f:
            dict_name_id=load(f)  
            # for k,v in dict_hero_id.items():
                # hero_name_id[v]=k
        #     dump(hero_name_id,f,ensure_ascii=False)
        for file_clean in normal_text_need_clean:
            radiant_name,dire_name=[],[]
            with open(self.DIR+"/"+str(file_clean),"r+",encoding="utf-8") as f:
                needto_extract_10_hero=f.read()
            bs4_object=BeautifulSoup(needto_extract_10_hero,"html.parser")
            block_twoside=bs4_object.find_all("article",class_=compile("(r-tabbed-table|d-tabbed-table)"))
            json_file=file_clean.split(".")[0]+".json"
            match_id_in_json=file_clean.split(".")[0].split("_")[-1]
            print (match_id_in_json)
            print (len(block_twoside))
            with open(self.DIR+"/"+json_file,"r+",encoding="utf-8") as f:
                dict_check_need_update=load(f)
                try:
                    if dict_check_need_update["radiant_team"] and dict_check_need_update["dire_team"]:
                        self.already_count+=1
                        print (json_file,"阵容已经赋值.")
                        continue
                except:
                    pass
            try:
                assert len(block_twoside)==2
            except:
                print ("错误block",block_twoside)
                assert 1>2
            for side,block in enumerate(block_twoside):
                side_str=block["class"][0]
                print (side_str)
                side_hero=block.find_all("a",href=compile("/heroes/(\w|-){1,}"))                
                side_hero=[i for i in side_hero if i["href"].split("/")[-1]!="abilities"]
                print (len(side_hero))
                try:
                    assert len(side_hero)==5,"长度不对"
                except:
                    for i in side_hero:
                        print (i["href"])
                    assert 1>2
                for one_hero in side_hero:
                    hero_name=one_hero["href"].split("/")[-1]
                    hero_id=dict_name_id[hero_name]
                    print (hero_id,type(hero_id),hero_name)
                    if side==0:
                        radiant_name.append(hero_id)
                    else:
                        dire_name.append(hero_id)
                with open(self.DIR+"/"+json_file,"r+",encoding="utf-8") as f:
                    dict_to_update=load(f)
                dict_to_update["radiant_team"]=",".join(radiant_name)
                # dict_to_update.pop("radiant_name")
                # dict_to_update.pop("dire_name")
                dict_to_update["dire_team"]=",".join(dire_name)
                print ("radiant",dict_to_update["radiant_team"])
                print ("dire",dict_to_update["dire_team"])
                # print(type(dict_to_update))
                with open(self.DIR+"/"+json_file,"w+",encoding="utf-8") as f,open("clean_log.txt","a+",encoding="utf-8") as f_log:
                    f_log.seek(0)
                    dump(dict_to_update,f,ensure_ascii=False)
                    print ("success",match_id_in_json,file_clean+"\n",file=f_log)
                    self.success_count+=1
        print("成赋值",self.success_count," 几个normal json文件",self.already_count,"文件之前已经赋值")
        return 

CRAWL_NEW_TOUR_MATCH=True
CLEAN_NORMAL_DATA_BANPICK=False#从最长的normal_queue(get from team_pid->pid/match/selectrecent->opendota的crawlnormal)中判断是否存在.txt存在则不抓取 不存在就从dotabuff抓取页面信息
CONFIRM=False
CLEAN_TXT=False
TOUR_PREVIEW=False
print ("excute!")
if __name__ == '__main__':
    instance_t=Tournament_id_dotabuff()
    #instance_t.get_data_from_dotabuff()
    if CRAWL_NEW_TOUR_MATCH==True:
        instance_t.get_each_match()
    if CLEAN_NORMAL_DATA_BANPICK==True:
        instance_t.clean_normal_banpick()
    if CONFIRM==True:
        import sys,io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
        instance_t.confirm()
    if CLEAN_TXT==True:
        instance_t.update_normal_randint_dire_to_match_json()
    if TOUR_PREVIEW==True:
        instance_t.Tournament_preview()
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