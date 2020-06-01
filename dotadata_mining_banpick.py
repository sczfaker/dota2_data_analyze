from fake_useragent import UserAgent
import re
from re import search,findall
from bs4 import BeautifulSoup
from requests import get
import requests
import sys,io
from json import loads
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

"https://www.tuotugame.com/dota2/5ef8a9a94302e82c262a1add"
url="app.tuotuesports.com:443"
url_host="dragate.dc.oppomobile.com:443"
class Ban_Pick(object):
    """docstring for ClassName"""
    def __init__(self):
        self.ua = UserAgent()
        # req_session=requests.session()
        # requests.utils.add_dict_to_cookiejar(req_session.cookies,tu_cookie)
        self.get_live_match_id()
        self.matchid_list=self.id_list#[5502801030,5502737341]##5501387569,5501372492
        print (self.matchid_list)
        self.match_url=[]
        for one_match_id in self.matchid_list:
            self.url_score = 'https://api.tuotu.live/api/front/schedule/match/%s?game_category=dota2'%(one_match_id)
            self.match_url.append(self.url_score)
        self.headers = {'Host': 'api.tuotu.live', 'Connection': 'keep-alive', 'Accept': 'application/json, text/plain, */*', 'Origin': 'https://www.tuotugame.com', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.88 Safari/537.36 Vivaldi/2.4.1488.36', 'Referer': 'https://www.tuotugame.com/dota2/5ef8a98f4302e82c262a1ac2', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9'}
        #self.url_score="https://www.tuotugame.com/dota2/5ef8a98f4302e82c262a1ac2"
        self.cookies={}
    def get_content(self,url_score):
        req_object=requests.get(url_score,headers=self.headers,verify=False, cookies=self.cookies)
        html_text=req_object.text
        dic_data=loads(html_text)
        # print (dic_data)
        radiant_name,dire_name=dic_data["radiant_team"]['tag'],dic_data["dire_team"]['tag']
        # for i in dic_data:
            # print (i)
        # assert 1>2
        radiant,dire=dic_data["radiant_picks"],dic_data["dire_picks"]
        # print (radiant,dire)
        return radiant,dire,radiant_name,dire_name
    def clear(self):
        with open ("request.log","w+",encoding="utf-8") as f:
            pass
    def get_live_match_id(self):
        pattern=re.compile("(?<=match/)\d+")
        # print (findall("(?<=match/)\d+","match/3336"))
        with open ("request.log","r+",encoding="utf-8") as f:
            self.id_list=[search("(?<=match/)\d+",i).group() for i in f.readlines()]
        #print (html_text,type(html_text),len(html_text))
        # with open ("current_score.txt","w+",encoding="utf-8") as f:
        #     f.write(html_text)
        # with open("current_score.txt","r+",encoding="utf-8") as f:
        #     html_text=f.read()
        #     bs4_object=BeautifulSoup(html_text,"html.parser")
        #     scoreboard_div=bs4_object.find("div",class_="white_team_info TeamInfo__Wrap-sc-1rj3g80-0 bXJnGo")
        #     two_team_div=scoreboard_div.find_all("div",class_="team_info")
        #     for r_or_d,team in enumerate(two_team_div):
        #         player_info=team.find_all("div",class_="content T2Table__TableCol-pw2kep-2 jOGHdC")
        #         for player_div in player_info:
        #             teamname_id=player_div.find("span").get_text()
        #             heroname=player_div.find("p").get_text()
        #             if r_or_d==0:
        #                 radiant.append(heroname)
        #             else:
        #                 dire.append(heroname)
CLEAR=False
if __name__ == '__main__':
    instance=Ban_Pick()
    if CLEAR==True:
        instance.clear()
    instance.get_live_match_id()
    # len_match=len(instance.matchid_list)
    print (instance.match_url,"比赛实时列表长度:",len_match)
    # for one_full_url in instance.match_url:
    #     r,d,rn,dn=instance.get_content(one_full_url)
    #     print (r,d,rn,dn)
"""
var hosts = 'zkd.me develop.dog';
FiddlerApplication.Log.LogFormat("Logger session {0}, Url: {1}, isHttps: {2}, port: {3}", oSession.id, oSession.fullUrl, oSession.isHTTPS, oSession.port);
if(hosts.indexOf(oSession.host) > -1){
    FiddlerApplication.Log.LogFormat("Capture session {0}, Url: {1}, isHttps: {2}, port: {3}", oSession.id, oSession.fullUrl, oSession.isHTTPS, oSession.port);
    if(oSession.HTTPMethodIs('CONNECT')){
        FiddlerApplication.Log.LogString('create fake tunnel response');
        oSession['x-replywithtunnel'] = 'FakeTunnel';
        return;
    }

    if (oSession.isHTTPS){
        FiddlerApplication.Log.LogString('switch https to http request');
        oSession.fullUrl = oSession.fullUrl.Replace("https://","http://");
        oSession.port = 80;
    }   

    FiddlerApplication.Log.LogFormat("Processed session {0}, Url: {1}, isHttps: {2}, port: {3}", oSession.id, oSession.fullUrl, oSession.isHTTPS, oSession.port);
}
FiddlerApplication.Log.LogFormat("Logger session {0}, Url: {1}, isHttps: {2}, port: {3}", oSession.id, oSession.fullUrl, oSession.isHTTPS, oSession.port);
if(oSession.isHTTPS && oSession.url.indexOf(oSession.host)> -1){  
    oSession["ui-color"] = "blue";  
}  
if(!oSession.isHTTPS && oSession.url.indexOf(oSession.host)> -1){  
    oSession["ui-color"] = "green";  
}
"""