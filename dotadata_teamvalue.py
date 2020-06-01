from json import dump
from os import chdir,listdir,rename
from re import findall,compile
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import sys,io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

from json import load,dump,loads
from requests import get
from time import sleep
from re import findall,compile,match

class TeamValue(object):#选择英雄统计,击败战队统计
    def __init__(self):
        self.CREATE_DICT_TEAM_PLAYERID=True
        self.match_catalog="MATCH_JSON_DIR_0727"
        self.ua = UserAgent()
        self.prefix_team="https://www.dotabuff.com/esports/teams"
        self.prefix_team="http://dotamax.com/match/tour_famous_team_list/"
        self.match_files = [file for file in listdir(self.match_catalog) if file[-4:]=="json" and (match("\d{10,}",file[:-5]))]
    #def iterate_file(self):#创建所以重要比赛的dict字典,并且验证id是否正确.
        print("统计比赛长度",len(self.match_files))
        self.rigth_count,need_to_fix=0,[]
        self.real_match={}
        self.headers={"user-agent":self.ua.random}
        self.teamid_to_name={}
        if False:
            for amatch in self.match_files:
                with open (self.match_catalog+"/"+amatch,"r+",encoding="utf-8") as f:
                    dict_match=load(f)
                if dict_match["game_mode"]==2:
                    self.real_match[amatch[:-5]]=dict_match
            #print (len(self.real_match))
            for rm in self.real_match:
                if self.real_match[rm]["match_id"]==int(rm):
                    self.rigth_count+=1
                else:
                    print (rm,"!=",rm["match_id"])
                    need_to_fix.append(rm)
        self.game_version="0727"
        if False:
            with open("teamid_to_name_"+self.game_version+".json","r+",encoding="utf-8") as f:
                self.teamid_to_name=load(f)
        self.create_team_dict()
        self.other_stats()
        self.visulize_team_winlose()
    def get_teamid_tostr(self,rtid,dtid):
        urlprefix="https://api.opendota.com/api/teams/"
        if rtid not in self.teamid_to_name:
            req_object_1=get(urlprefix+str(rtid),headers=self.headers)
            self.teamid_to_name[rtid]={}
            self.teamid_to_name[rtid]['fullname']=""
            if req_object_1.status_code==200:
                try:
                    rname=loads(req_object_1.text)["name"]
                except:
                    print("load error")
                self.teamid_to_name[rtid]['fullname']=rname
            self.teamid_to_name[rtid]['winlose']={"win":0,'lose':0}
        if dtid not in self.teamid_to_name6:
            req_object_2=get(urlprefix+str(dtid),headers=self.headers)
            self.teamid_to_name[dtid]={}
            self.teamid_to_name[dtid]['fullname']=""
            if req_object_2.status_code==200:
                try:
                    dname=loads(req_object_2.text)["name"]
                except:
                    print("load error")
                self.teamid_to_name[dtid]['fullname']=dname
            self.teamid_to_name[dtid]['winlose']={"win":0,'lose':0}
        print ("afight with team record",len(self.teamid_to_name))
        sleep(1)
    def create_team_dict(self):
        for match in self.real_match:
            rtid=self.real_match[match]['dire_team_id']
            dtid=self.real_match[match]['radiant_team_id'] 
            self.get_teamid_tostr(rtid,dtid)
            rad_winlose=self.real_match[match]["radiant_win"]
            if rad_winlose:
                winid=self.real_match[match]["radiant_team_id"]
                loseid=self.real_match[match]["dire_team_id"]
            else:
                loseid=self.real_match[match]["radiant_team_id"]
                winid=self.real_match[match]["dire_team_id"]
            self.teamid_to_name[winid]["winlose"]["win"]+=1
            self.teamid_to_name[loseid]["winlose"]["lose"]+=1
        with open("teamid_to_name_"+self.game_version+".json","w+",encoding="utf-8") as f:
            dump(self.teamid_to_name,f,ensure_ascii=False)
    def other_stats(self):
        with open("teamid_to_name_"+self.game_version+".json","r+",encoding="utf-8") as f:
            self.full_team_dic=load(f)
        for i in self.full_team_dic:
            total=self.full_team_dic[i]["winlose"]["win"]+self.full_team_dic[i]["winlose"]["lose"]
            self.full_team_dic[i]["winlose"]["total"]=total
            self.full_team_dic[i]["winrate"]=self.full_team_dic[i]["winlose"]["win"]/self.full_team_dic[i]["winlose"]["total"]
        with open("teamid_to_name_"+self.game_version+".json","w+",encoding="utf-8") as f:
            dump(self.full_team_dic,f,ensure_ascii=False)
    def visulize_team_winlose(self):
        with open("teamid_to_name_"+self.game_version+".json","r+",encoding="utf-8") as f:
            self.full_team_dic=load(f)
        list_fullteam=self.full_team_dic.items()
        totalgame_sort=[i for i in sorted(list_fullteam,key=lambda x:x[1]["winlose"]["total"],reverse=True) if i[1]["winlose"]["total"]>=10]
        winrate_sort=[i for i in sorted(list_fullteam,key=lambda x:x[1]["winrate"],reverse=True) if i[1]["winlose"]["total"]>=10]
        for team in winrate_sort:
            print (team)
    def get_teammate_id_from_docs(self):
        pass
    def team_players(self):
        #headers = {'Host': 'www.dotabuff.com', 'Connection': 'keep-alive', 'Cache-Control': 'max-age=0', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.88 Safari/537.36 Vivaldi/2.4.1488.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'Referer': 'https://www.dotabuff.com/', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9'}
        #cookies url = 'http://dotamax.com/accounts/login/'
        self.pagelimit=10
        self.nextpage=False
        self.url_login="http://dotamax.com/accounts/login/"
        headers = {'Host': 'dotamax.com', 'Connection': 'keep-alive', 'Content-Length': '1335', 'Cache-Control': 'max-age=0', 'Origin': 'http://dotamax.com', 'Upgrade-Insecure-Requests': '1', 'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.88 Safari/537.36 Vivaldi/2.4.1488.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'Referer': 'http://dotamax.com/accounts/logout/?src=bets', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'}
        cookies = {'_ga': 'GA1.2.917068991.1593764201', '_gid': 'GA1.2.981710910.1593764201', 'Hm_lvt_575895fe09d48554a608faa5ef059555': '1593764202', 'csrftoken': 'PP0Xh0PvPbiSWlk7tzkeVaJf7Cc9gUPe', '_gat': '1', 'Hm_lpvt_575895fe09d48554a608faa5ef059555': '1593768133'}
        data = {'csrfmiddlewaretoken': 'PP0Xh0PvPbiSWlk7tzkeVaJf7Cc9gUPe', 'phoneNumCipherb64': 'UI0XFR3urBNVZ2ZhsAP6fdKLZQqmCW13D4m3Ol0vAcpcSi4V8mU9k4T%2Bzw%2FLlDsE%0D%0A65LU0FXmRQFiSbgIwh%2FU%2F%2BNtI%2F2t0ULb8Pj29S%2BOwbCTzVdAu1kIEuNPOFIKllMy%0D%0ATvJ9MQLnw22CPRWWZIGY5QEPZPAgpwsk%2FftrmQ4QmL3X%2BU0PiJ1bBE0rXt8N%2BHXN%0D%0AEZaZ97w1En2umsVdwk4lSZrS%2Fg4iB%2Bgi82bwAx8oWIaL%2FHRBuFqxFYa1iCS4T6S9%0D%0AFf0bDFMMYdKvatLAvnnCP1HIwMOYPSddHgfOvVFLOdvm3Uo00vu%2Fh9ELNzHR%2Fz4g%0D%0AGKn5nlrcGyx3di1FR2sQMA%3D%3D', 'usernameCipherb64': 'Shga8IDmEK1HIIqZc3EGtVd4QpQtbC70aJOxA3La6SKzwqNsrx%2BblNY9LgOfreCr%0D%0AiGxBQdEgm0yKVja5RsIT4SMUSvIpf08xxGAwGK53KDwbRMuw3WMU4ZCJIAOaArMW%0D%0AiY8yb%2BsDFh%2BtKxOyW60MG3bYIVjDYWMwTeiGllqO%2FzsLMXJdlXhM2x%2BC5txlILjm%0D%0ALQAaBYMkW%2F%2BZt0YE9MwUyVIrBLcamhMaTM9jLzwV8DT289LAR7JCzDoWGP%2FHT%2FEz%0D%0AvNXm33KGhhhas3zYvvLrieUuA2nytbvtvJHZzmcn1aALuDzjWvDm%2FdCR1bnOQJj9%0D%0AnWZ1w3bVnI7imZFqd4%2B93Q%3D%3D', 'passwordCipherb64': 'YbFgL6BLlMLlX1s957%2FOBSbUiPIo3GUevWF%2BJAmPUrQDkHhicgZQKEnSkVQOnvSC%0D%0A8pmKhawfIjoRFP4hfWxhCSeDU6ZWlKyZc2zxQSkJE34FYKVgEjPdsq0lgB7mK%2BMS%0D%0ArL1c2l%2BZoHMWnz3sTf3EeIAljenoL4uKpc8l60uGkdYjdQZ%2Fg9hJB4KQp7BaSXYX%0D%0AbOSIaBppwHXPXdBoU%2BnIFUMff91QS8SO%2FklN5T5cswRKW60mxeMuiEhVQXQCTEDL%0D%0AtpsMAVWJgyH15292A2YuAahVT6u5BstvkXxUN5fQEQUGKYhHFKWBV2SmYDVWE0te%0D%0Ad04vmBSkUmoms%2BvD1cj4Lg%3D%3D', 'account-type': '2', 'src': 'bets'}
        if self.CREATE_DICT_TEAM_PLAYERID:
            # html = requests.post(self.url_login, headers=headers, verify=False, cookies=cookies, data=data)= {'_tz': 'Asia%2FShanghai', '_ga': 'GA1.2.961090768.1592724898', '__qca': 'P0-368302978-1592724902240', '__gads': 'ID', '_ym_uid': '1590651080726563724', '_ym_d': '1592724907', 'pbjs-id5id': '%7B%22ID5ID%22%3A%22ID5-ZHMOrDEaxifVhvRNRZHJiq0L_-oXr7wWsAZNImUX5g%22%2C%22ID5ID_CREATED_AT%22%3A%222020-06-21T07%3A35%3A25.74Z%22%2C%22ID5_CONSENT%22%3Atrue%2C%22CASCADE_NEEDED%22%3Atrue%2C%22ID5ID_LOOKUP%22%3Atrue%2C%223PIDS%22%3A%5B%5D%7D', '_s': 'ZUUyb0ZqNzU1SldBSklybk5yWUk2UzZDL0ViTGNaMVpiZzFhcmkzMXYvQUZPSWwrbkY3WjZralJrcy9vMEdaeFVJa0psUW5tb21vOUpYYnVFUFVVTHNiRjErRGhOZkE1QVBiejNDeUxDcmUzZWplVS9KZDJ5dW5VL296NWJkc2N5Wk01dG9ROFM3TEF1Qll4cWpMa0dOVkI5K3RHYmxCTVZkT0Y0a0lXaVJkOXRxS3lrUmNLVlhrYXVrUUpBSzFoLS15OFJwUkJKWFVJSzF1Qm1OZ3Vsa1h3PT0%3D--ac927341bcffe876cc4f814411d07ae4e96c3637', '_gid': 'GA1.2.590241721.1593564884', '_ym_visorc_52686388': 'w', '_ym_isad': '2', 'pbjs-id5id_last': 'Fri%2C%2003%20Jul%202020%2008%3A18%3A43%20GMT', '_hi': '1593765578384'}
            # url = 'http://dotamax.com/match/tour_famous_team_list/'
            # teampage_headers = {'Host': 'dotamax.com', 'Connection': 'keep-alive', 'Cache-Control': 'max-age=0', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.88 Safari/537.36 Vivaldi/2.4.1488.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'Referer': 'http://dotamax.com/bets/index/', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'}
            # teampage_cookies = {'_ga': 'GA1.2.917068991.1593764201', '_gid': 'GA1.2.981710910.1593764201', 'Hm_lvt_575895fe09d48554a608faa5ef059555': '1593764202', 'csrftoken': 'PP0Xh0PvPbiSWlk7tzkeVaJf7Cc9gUPe', 'pkey': 'MTU5Mzc2ODE0My42MnNjel8wMDBfMnNjbHBlY2x3dGxzbnVrYWg__', '_gat': '1', 'Hm_lpvt_575895fe09d48554a608faa5ef059555': '1593768539'}
            # req_object=get(self.prefix_team,headers=teampage_headers,cookies=teampage_cookies)
            #with open (".txt","w+",encoding="utf-8") as f:
            #    f.write(req_object.text)
            team_and_player={}
            file_page_list=["team_page1.htm","team_page2.htm","team_page3.htm","team_page4.htm","team_page5.htm"]
            for file_page in file_page_list:
                with open (file_page,"r+",encoding="utf-8") as f:
                    text_teampage=f.read()
                    # player_id=findall("/player/detail/\d{7,}",text_teampage)
                    # for tag in player_id:
                    #     one_player_id=tag.split("/")[-1]
                    #     if one_player_id!="226124774":
                    #         print ("----")
                    bs4_object=BeautifulSoup(text_teampage,"html.parser")
                    team_tag=bs4_object.find_all("tr",id=compile("matchrow_\d{1,2}"))
                    print (len(team_tag))
                    for tag in team_tag:
                        team_name=tag.find("td",class_="table-title-font").get_text().strip()
                        team_and_player[team_name]=[]
                        all_teammates_id=tag.find_all("a",href=compile("/player/detail/\d{7,}"))
                        for tid_tag in all_teammates_id:
                            tid=tid_tag['href'].split("/")[-2]
                            team_and_player[team_name].append(tid)
            print (team_and_player)
        if True:                            
            with open ("team_and_player.json","w+",encoding="utf-8") as f:
                dump(team_and_player,f,ensure_ascii=False)
            return team_and_player
    def compute_value(self):
        pass
if True:
    teva=TeamValue()
    # teva.visulize_team_winlose()
    # teva.team_players()
    # teva.other_stats()
    # teva.visulize_team_winlose()