#coding:utf-8
import os
from sklearn.model_selection import cross_val_score
from sklearn.metrics import roc_auc_score, accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from fake_useragent import UserAgent
from re import findall,compile,match
from os import chdir,listdir,rename
from itertools import combinations
from json import load,dump,loads
from requests import get
from time import sleep
from random import choice
import numpy as np
import pandas as pd
import operator
import random
import logging
import sys,io
import datetime
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
import joblib
import matplotlib.pyplot as plt
# import plotly.graph_objects as go
# import plotly as py
# plt = py.offline.plot
# fh = logging.FileHandler(path,encoding='utf-8')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# console log
#formatter = logging.Formatter('%(message)s')
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger = logging.getLogger(__name__)
logger.addHandler(ch)
# logger.addHandler(fh)
class Match_stat(object):
    """Models before 6/30"""
    def __init__(self):
        self.match_catalog="MATCH_JSON_DIR_7.26"
        self.match_files = [file for file in listdir(self.match_catalog) if file[-4:]=="json" and match("\d{10,}",file[:-5])]
        with open("hero_id_name.json","r+") as f:
            self.hero_id_name=load(f)
        self.real_match={}
        self.team_ana={}
        self.afight={}
        self.game_version="0726"
        self.r_pick_score=0
        self.d_pick_score=0
        self.heao_value_measure={}
        self.count=[0,0]
        self.ua = UserAgent()
        self.headers={"user-agent":self.ua.random}
        print (self.headers)
        self.heroes_released=129
    def gethero_frombanpick(self,banpick):
        direteam,radiantteam=0,0
    def save_everymatch_tocsv(self):
        fname="matches.csv"
        COLUMNS = ['match_id','radiant_win','radiant_team','dire_team','avg_mmr','num_mmr','game_mode', 'lobby_type','duration','draft_timings','dire_score','radiant_score']#teamfights
        for single_match in self.real_match:
            radiant,dire=[],[]
            #win_object=lambda:"radiant" if self.real_match[single_match]["randiant_win"] else "dire"
            pickbans,direid,rid=self.real_match[single_match]["picks_bans"],self.real_match[single_match]["dire_team_id"],self.real_match[single_match]["radiant_team_id"]
            for pickbanseq in pickbans:
                if pickbanseq["is_pick"]==True:
                        hero_id=pickbanseq["hero_id"]
                        hero_name=self.hero_id_name[str(hero_id)]
                        if pickbanseq["team"]==1:
                            dire.append(hero_id)
                        else:
                            radiant.append(hero_id)
#                        if hero_id==34:
#                            self.count[0]+=1
#                            if self.real_match[single_match]["radiant_win"]==True and hero_id in radiant:
#                                self.count[1]+=1
#                            elif self.real_match[single_match]["radiant_win"]==False and hero_id in dire:
#                                self.count[1]+=1
            self.real_match[single_match]["dire_team"]=",".join([str(i) for i in dire])
            # print (self.real_match[single_match]["dire_team"])
            self.real_match[single_match]["radiant_team"]=",".join([str(i) for i in radiant])
            # print (self.real_match[single_match]["radiant_team"])
            self.real_match[single_match]["avg_mmr"]=choice(range(6000,6500,20))
            self.real_match[single_match]["num_mmr"]=random.randint(0,9)
        self.RATIO_TESET=len(self.real_match)//5
        self.test_files=random.sample(self.real_match.items(),self.RATIO_TESET)
        self.test_files_dict={}
        for testfile in self.test_files:
            self.test_files_dict[testfile[0]]=testfile[1]
        for tfdict in self.test_files_dict:
            self.real_match.pop(tfdict)
        result_dataframe=pd.DataFrame()
        for single_match in self.real_match:
            current_dataframe=pd.json_normalize(self.real_match[single_match])
            # print (len(result_dataframe))
            result_dataframe=result_dataframe.append(current_dataframe)
        print (len(self.real_match),len(self.test_files_dict))
        pd.DataFrame(result_dataframe,columns=COLUMNS).to_csv(fname,index=False)
        print (self.count)
        return result_dataframe

    def iterate_file(self):#创建所以重要比赛的dict字典,并且验证id是否正确.
        self.rigth_count,need_to_fix=0,[]
        for match in self.match_files:
            with open (self.match_catalog+"/"+match,"r+",encoding="utf-8") as f:
                dict_match=load(f)
            if dict_match["game_mode"]==2:
                self.real_match[match[:-5]]=dict_match
        print (len(self.real_match))
        for rm in self.real_match:
            if self.real_match[rm]["match_id"]==int(rm):
                self.rigth_count+=1
            else:
                print (rm,"!=",rm["match_id"])
                need_to_fix.append(rm)
        print("过滤掉中单模式的比赛")
        # print(need_to_fix)
    def two_team_futuremeet(self):
        for i in self.match:
            r,d=self.match[i]["dire_team_id"],self.match[i]["radiant_team_id"]
            if r not in self.team_ana:#
                self.team_ana[r]={}
            if d not in self.team_ana:
                self.team_ana[r]={}
        for afight in combinations(self.team_ana.keys(),2):
            self.afight[afight]={}
        print (len(self.afight))
    def get_heroid_content(self):
        self.heroes_released = 129
        self.hero_id={}
        hero_release=[]
        with open ("hero_id_name_id.json","r+") as f:
            self.hero_id=load(f)
        version={}
        with open(self.match_catalog+"/"+"heroes.json") as f:
            hero_id_content=load(f)
        t=[]
        for hero in hero_id_content:
            t.append(hero["id"])
        dd=set(range(1,130))
        self.x=dd.difference(t)
        for hero in hero_id_content:
            #self.hero_id[hero["id"]]=hero["localized_name"].replace(" ","-").lower()
            hero_release.append({"id":hero["id"],"name":hero["localized_name"],"primary_attribute":hero["primary_attr"]})
        version["heroes_7.26c"]=hero_release
        return version
    def all_match_bp(self):
        ban_pick_result={}
        for match in self.real_match:
            p,direid,rid=self.real_match[match]["picks_bans"],self.real_match[match]["dire_team_id"],self.real_match[match]["radiant_team_id"]
            win_object=lambda:"radiant" if self.real_match["randiant_win"] else "dire"
            amatch_combination={"dire":[],"rand":[]}
            for i in p:
                if i["is_pick"]==True:
                        hero_id=i["hero_id"]
                        hero_name=self.hero_id_name[str(hero_id)]
                        if i["team"]==1:
                            amatch_combination["dire"].append(hero_name)
                        else:
                            amatch_combination["rand"].append(hero_name)
            ban_pick_result[match]={"sequence":p,"diretid":direid,"rid":rid,"win_object":win_object,"combination":amatch_combination}
        for i in ban_pick_result:
            print (i)
            print (ban_pick_result[i]["combination"])
    def build_team_hero_dict(self):
        a=0
        for i in self.team_ana:
            self.team_ana[i]={}
            a=i
            for j in self.hero_id:
                self.team_ana[i][self.hero_id[j]]=50
        return 
    def read_dataset(self,csv_path,low_mmr=None,high_mmr=None,advantages=False):
        global logger
        dataset_df = pd.read_csv(csv_path)
        if low_mmr:
            dataset_df = dataset_df[dataset_df.avg_mmr > low_mmr]
        if high_mmr:
            dataset_df = dataset_df[dataset_df.avg_mmr < high_mmr]
        logger.info("The dataset contains %d games", len(dataset_df))
        if advantages:
            logger.info("Computing advantages...")
            advantages_list = self.compute_advantages(dataset_df)
            # print (advantages_list[0]["winrate"].max())
            # print (advantages_list[1]["winrate"].max())
            # assert 1>2
            # for i in advantages_list:
                # print (i.shape)
        else:
            logger.info("Loading advantages from files...")
            synergies = np.loadtxt('pretrained/synergies_all.csv')
            counters = np.loadtxt('pretrained/counters_all.csv')
            advantages_list = [synergies, counters]
        # assert 1>2
        logger.info("Transforming dataframe in feature map...")
        feature_map = self.dataset_to_features(dataset_df, advantages=advantages_list)
        return [feature_map, advantages_list]
    def compute_advantages(self,dataset_df):
        self.synergy = dict()
        self.synergy['wins'] = np.zeros((self.heroes_released, self.heroes_released))
        self.synergy['games'] = np.zeros((self.heroes_released, self.heroes_released))
        self.synergy['winrate'] = np.zeros((self.heroes_released, self.heroes_released))
        self.counter = dict()
        self.counter['wins'] = np.zeros((self.heroes_released, self.heroes_released))
        self.counter['games'] = np.zeros((self.heroes_released, self.heroes_released))
        self.counter['winrate'] = np.zeros((self.heroes_released, self.heroes_released))
        dataset_np = dataset_df.values
        #print (len(dataset_np))
        for row_amatch in dataset_np:
            self.update_dicts(row_amatch, self.synergy, self.counter)
        self.compute_winrates(self.synergy, self.counter, self.heroes_released)
        self.synergy_matrix,self.counter_matrix =self.calculate_advantages(self.synergy, self.counter, self.heroes_released)
        #print (self.synergy_matrix)
        #print (self.counter_matrix)
        # assert 1>2
        np.savetxt('pretrained/synergies_all.csv', self.synergy_matrix)
        np.savetxt('pretrained/counters_all.csv',self.counter_matrix)
        return [self.synergy_matrix, self.counter_matrix]
    def update_dicts(self,game, synergy, counter):
        self.radiant_wincount,self.dire_wincount=0,0
        radiant_win, radiant_heroes, dire_heroes = game[1], game[2], game[3]
        if radiant_win:
            self.radiant_wincount+=1
        else:
            self.dire_wincount+=1
        radiant_heroes = list(map(int, radiant_heroes.split(',')))
        dire_heroes = list(map(int, dire_heroes.split(',')))
        assert len(set(radiant_heroes).intersection(set(dire_heroes)))==0
        for i in range(5):
            for j in range(5):
                if i != j:
                    synergy['games'][radiant_heroes[i] - 1, radiant_heroes[j] - 1] += 1
                    synergy['games'][dire_heroes[i] - 1, dire_heroes[j] - 1] += 1

                    if radiant_win:
                        synergy['wins'][radiant_heroes[i] - 1, radiant_heroes[j] - 1] += 1
                    else:
                        synergy['wins'][dire_heroes[i] - 1, dire_heroes[j] - 1] += 1

                counter['games'][radiant_heroes[i] - 1, dire_heroes[j] - 1] += 1
                counter['games'][dire_heroes[i] - 1, radiant_heroes[j] - 1] += 1

                if radiant_win:
                    counter['wins'][radiant_heroes[i] - 1, dire_heroes[j] - 1] += 1
                else:
                    counter['wins'][dire_heroes[i] - 1, radiant_heroes[j] - 1] += 1
    def compute_winrates(self,synergy, counter, heroes_released):
        for i in range(heroes_released):
            for j in range(heroes_released):
                if i!=j:
                    if synergy['games'][i, j] != 0:
                        synergy['winrate'][i, j] = synergy['wins'][i, j]/float(synergy['games'][i, j])
                            # print ("hero",i,j,synergy['winrate'][i, j])
                    if counter['games'][i, j] != 0:
                        counter['winrate'][i, j] = counter['wins'][i, j]/float(counter['games'][i, j])
                        # print ("hero",i,j,counter['winrate'][i, j])
    def calculate_advantages(self,synergy, counter, heroes_released):
        synergies = np.zeros((heroes_released, heroes_released))
        counters = np.zeros((heroes_released, heroes_released))                                
        base_winrate = np.zeros(heroes_released)
        for i in range(heroes_released):
            if np.sum(synergy['games'][i])!=0:
                base_winrate[i] = np.sum(synergy['wins'][i]) / np.sum(synergy['games'][i])
                #print (synergy["wins"][i],synergy["games"][i],synergy["winrate"][i])
                # print (base_winrate[i],i)
        for i in range(heroes_released):
            for j in range(heroes_released):
                if i!=j:
                    if synergy['games'][i, j] > 0:
                        synergies[i, j] = self.adv_synergy(synergy['winrate'][i, j],
                                                       base_winrate[i],
                                                       base_winrate[j])
                    else:
                        synergies[i, j] = 0
                        if counter['games'][i, j] > 0:
                            counters[i, j] = self.adv_counter(counter['winrate'][i, j],
                                                          base_winrate[i],
                                                          base_winrate[j])
                        else:
                            counters[i, j] = 0 
        return synergies, counters
    def adv_synergy(self,winrate_together, winrate_hero1, winrate_hero2):
        return winrate_together
    def adv_counter(self,winrate_together, winrate_hero1, winrate_hero2):
        return winrate_together
    def dataset_to_features(self,dataset_df, advantages=None):
        heroes_released = 129
        synergy_matrix, counter_matrix = None, None
        if advantages:
            x_matrix = np.zeros((dataset_df.shape[0], 2 * heroes_released + 3))
            [synergy_matrix, counter_matrix] = advantages
        else:
            x_matrix = np.zeros((dataset_df.shape[0], 2 * heroes_released))
        y_matrix = np.zeros(dataset_df.shape[0])
        dataset_np = dataset_df.values
        for i, row in enumerate(dataset_np):
            radiant_win = row[1]
            radiant_heroes = list(map(int, row[2].split(',')))
            dire_heroes = list(map(int, row[3].split(',')))

            for j in range(5):
                x_matrix[i, radiant_heroes[j] - 1] = 1
                x_matrix[i, dire_heroes[j] - 1 + heroes_released] = 1
                if advantages:
                    x_matrix[i, -3:] = self.augment_with_advantages(synergy_matrix,
                                                               counter_matrix,
                                                               radiant_heroes,
                                                               dire_heroes)
            y_matrix[i] = 1 if radiant_win else 0
        return [x_matrix, y_matrix]
    def augment_with_advantages(self,synergy, counter, radiant_heroes, dire_heroes):
        synergy_radiant = 0
        synergy_dire = 0
        counter_score = 0
        for i in range(5):
            for j in range(5):
                if i > j:
                    synergy_radiant += synergy[radiant_heroes[i] - 1][radiant_heroes[j] - 1]
                    synergy_dire += synergy[dire_heroes[i] - 1][dire_heroes[j] - 1]
                counter_score += counter[radiant_heroes[i] - 1][dire_heroes[j] - 1]
        return np.array([synergy_radiant, synergy_dire, counter_score])
    def create_testset(self):
        result_dataframe=pd.DataFrame()
        fname="matches_testset.csv"
        COLUMNS = ['match_id','radiant_win','radiant_team','dire_team','avg_mmr','num_mmr','game_mode', 'lobby_type','duration','draft_timings','dire_score','radiant_score']#teamfights
        for single_testset_match in self.test_files_dict:
            current_dataframe=pd.json_normalize(self.test_files_dict[single_testset_match])
            result_dataframe=result_dataframe.append(current_dataframe)
        pd.DataFrame(result_dataframe,columns=COLUMNS).to_csv(fname,index=False)
        return result_dataframe
    def train(self):
        dataset_train, _ = self.read_dataset('matches.csv', low_mmr=6000)
        dataset_test, _ = self.read_dataset('matches_testset.csv', low_mmr=6000)
        result=self.evaluate(dataset_train, dataset_test, cv=7, save_model='model_'+str(datetime.date.today())+'.pkl')
        return result
    def evaluate(self,train_data, test_data, cv=5, save_model=None):
        x_train, y_train = train_data
        x_test, y_test = test_data
        scaler = StandardScaler()
        scaler.fit(x_train)
        x_train = scaler.transform(x_train)
        x_test = scaler.transform(x_test)
        cross_val_mean = -1
        if cv > 0:
            model = LogisticRegression(C=0.005, random_state=42)
            cross_val_scores = cross_val_score(model, x_train, y_train, cv=cv, scoring='roc_auc',
                                               n_jobs=-1)
            cross_val_mean = np.mean(cross_val_scores)
            logger.info("Cross validation scores over the training set (%d folds): %.3f +/- %.3f", cv,
                        cross_val_mean,
                        np.std(cross_val_scores))
        model = LogisticRegression(C=0.005, random_state=42)
        model.fit(x_train, y_train)
        probabilities = model.predict_proba(x_test)
        roc_auc = roc_auc_score(y_test, probabilities[:, 1])
        labels = model.predict(x_test)
        acc_score = accuracy_score(y_test, labels)
        if save_model:
            model_dict = {}
            model_dict['scaler'] = scaler
            model_dict['model'] = model
            joblib.dump(model_dict, save_model)
        logger.info("Test ROC AUC: %.3f", roc_auc)
        logger.info("Test accuracy score: %.3f", acc_score)
        return (x_train.shape[0], x_test.shape[0], cross_val_mean, roc_auc, acc_score)
    def query_missing(self,model,scaler,radiant_heroes,dire_heroes,synergies,counters,similarities,heroes_released):
        all_heroes = radiant_heroes + dire_heroes
        base_similarity_radiant = 0
        base_similarity_dire = 0
        radiant = len(radiant_heroes) == 4
        for i in range(4):
            for j in range(4):
                if i > j:
                    base_similarity_radiant += similarities[radiant_heroes[i], radiant_heroes[j]]
                    base_similarity_dire += similarities[dire_heroes[i], dire_heroes[j]]
        query_base = np.zeros((heroes_released, 2 * heroes_released + 3))
        for i in range(heroes_released):
            if radiant:
                radiant_heroes.append(i + 1)
            else:
                dire_heroes.append(i + 1)
            for j in range(5):
                query_base[i][radiant_heroes[j] - 1] = 1
                query_base[i][dire_heroes[j] - 1 + heroes_released] = 1
            query_base[i][-3:] = augment_with_advantages(synergies,
                                                         counters,
                                                         radiant_heroes,
                                                         dire_heroes)
            if radiant:
                del radiant_heroes[-1]
            else:
                del dire_heroes[-1]
        if radiant:
            probabilities = model.predict_proba(scaler.transform(query_base))[:, 1]
        else:
            probabilities = model.predict_proba(scaler.transform(query_base))[:, 0]

        heroes_dict = get_hero_dict()
        similarities_list = []

        results_dict = {}
        for i, prob in enumerate(probabilities):
            if i + 1 not in all_heroes and i != 23:
                if radiant:
                    similarity_new = base_similarity_radiant
                    for j in range(4):
                        similarity_new += similarities[i + 1][radiant_heroes[j]]
                    similarities_list.append(similarity_new)
                else:
                    similarity_new = base_similarity_dire
                    for j in range(4):
                        similarity_new += similarities[i + 1][dire_heroes[j]]
                    similarities_list.append(similarity_new)

                results_dict[heroes_dict[i + 1]] = (prob, similarity_new)
        results_list = sorted(results_dict.items(), key=operator.itemgetter(1), reverse=True)
        similarities_list.sort()
        max_similarity_allowed = similarities_list[len(similarities_list) / 4]
        filtered_list = [x for x in results_list if x[1][1] < max_similarity_allowed]
        return filtered_list        
    def query_full(self,model,scaler,radiant_heroes,dire_heroes,synergies,counters,heroes_released):
        features = np.zeros(2 * heroes_released + 3)
        for i in range(5):
            features[radiant_heroes[i] - 1] = 1
            features[dire_heroes[i] - 1 + heroes_released] = 1
        extra_data = self.augment_with_advantages(synergies, counters, radiant_heroes, dire_heroes)
        features[-3:] = extra_data

        features_reshaped = features.reshape(1, -1)
        features_final = scaler.transform(features_reshaped)

        probability = model.predict_proba(features_final)[:, 1] * 100

        if probability > 50:
            return "Radiant has %.3f%% chance" % probability
        else:
            return "Dire has %.3f%% chance" % (100 - probability)
    def query(self,mmr,radiant_heroes, dire_heroes, synergies=None, counters=None, similarities=None):
        # if similarities is None:
        #     sims = np.loadtxt('pretrained/similarities_all.csv')
        # else:
        #     sims = np.loadtxt(similarities)
        if counters is None:        
            cnts = np.loadtxt('pretrained/counters_all.csv')
        else:
            cnts = np.loadtxt(counters)            
        if synergies is None:
            syns = np.loadtxt('pretrained/synergies_all.csv')
        else:
            syns = np.loadtxt(synergies)
        if mmr < 2000:
            model_dict = joblib.load(os.path.join("pretrained", "2000-.pkl"))
            logger.info("Using 0-2000 MMR model")
        #elif mmr > 5000:
        model_dict = joblib.load("model_"+str(datetime.date.today())+".pkl")
        logger.info("Using 5000-10000 MMR model")
        # else:
        #     file_list = [int(valid_file[:4]) for valid_file in listdir('pretrained')
        #                  if '.pkl' in valid_file]
        #     file_list.sort()            
        #     min_distance = 10000
        #     final_mmr = -1000
        #     for model_mmr in file_list:
        #         if abs(mmr - model_mmr) < min_distance:
        #             min_distance = abs(mmr - model_mmr)
        #             final_mmr = model_mmr
        #     logger.info("Using closest model available: %d MMR model", final_mmr)            
        #     model_dict = joblib.load(os.path.join("pretrained", str(final_mmr) + ".pkl"))
        scaler = model_dict['scaler']
        model = model_dict['model']
        heroes_released = self.heroes_released
        if len(radiant_heroes) + len(dire_heroes) == 10:
            return self.query_full(model,scaler,radiant_heroes,dire_heroes,syns,cnts,heroes_released)
        return self.query_missing(model,scaler,radiant_heroes,dire_heroes,syns,cnts,sims,heroes_released)
    def query_example(self):
        full_result = self.query(6000,
                            [59, 56, 54, 48, 31],
                            [40, 41, 52, 68, 61])
        logger.info("The result of the full query is: %s", full_result)

        # query for the result given the 4v5 or 5v4 configuration in a game around 3000 average MMR
        # radiant team: Huskar, Clinkz, Lifestealer, Luna, Lich
        # dire team: Venomancer, Faceless Void, Leshrac, Ancient Apparition
        # the missing element of the 2nd list is the one the suggestion is made for
        # the result is a list of (hero, (win_chance, overall_team_similarity)) sorted by win_chance
        # partial_result = self.query(6000,
        #                        [59, 56, 54, 48, 31],
        #                        [40, 41, 52, 68])
        # logger.info("The result of the partial query is: \n%s", partial_result)
    def get_teamid_tostr(self,rtid,dtid):
        urlprefix="https://api.opendota.com/api/teams/"
        print(rtid,dtid,len(self.teamid_to_name))

        if rtid in self.teamid_to_name:
            rname=self.teamid_to_name[rtid]["fullname"]
        if dtid in self.teamid_to_name:
            dname=self.teamid_to_name[dtid]["fullname"]
        return rname,dname
        # else:
        #     req_object_1=get(urlprefix+str(rtid),headers=self.headers)
        #     if req_object_1.status_code==200:
        #         rname=loads(req_object_1.text)["name"]
        #         teamid_to_name[rtid]=rname
        # else:
        #     req_object_2=get(urlprefix+str(dtid),headers=self.headers)
        #     if req_object_2.status_code==200:
        #         dname=loads(req_object_2.text)["name"]
        #         teamid_to_name[dtid]=dname
        # with open("teamid_to_name.json","w+",encoding="utf-8") as f:
        #     dump(teamid_to_name,f,ensure_ascii=True)
        #sleep(1)
    def get_match_bp(self):
        self.match_url=[]
        from dotadata_mining_banpick import Ban_Pick
        radiant,dire=[],[]
        req=Ban_Pick()
        radiant_full,dire_full,rname,dname=req.get_content()
        for i,j in zip(radiant_full,dire_full):
            radiant.append(i["_id"])
            dire.append(j["_id"])
        return radiant,dire,rname,dname
    def single_query(self):
        radiant,dire,rname,dname=self.get_match_bp()
        full_result=self.query(6000,radiant,dire)
        confirm=full_result.split(" ")[0].lower()
        # self.get_teamid_tostr(str(rtid),str(dtid))
        print ("预测结果:%s ----r:%s vs d:%s"%(full_result,rname,dname))
    def real_validation_set(self):
        with open("teamid_to_name_0726.json","r+",encoding="utf-8") as f:
            self.teamid_to_name=load(f)
        df1,df2=pd.read_csv("matches.csv"),pd.read_csv("matches_testset.csv")
        test_and_data_set=list(df1.match_id)+list(df2.match_id)
        correct,total=0,0
        self.real_validation=[i for i in os.listdir("real_validation_0726")]
        print(len(self.real_validation))
        self.predict_wrong=[]
        for amatch in self.real_validation:
            radiant,dire=[],[]
            mid=amatch[:-5]
            with open("real_validation_0726/"+amatch,"r+",encoding="utf-8") as f:
                amatch_dict=load(f)
            if mid not in test_and_data_set:
                print("实际验证的id:",mid)
                total+=1
                w=lambda:"radiant" if amatch_dict["radiant_win"] else "dire"
                # for i in self.real_match:
                #     for j in self.real_match[i]:
                #         print (j)
                rtid,dtid=amatch_dict["radiant_team_id"],amatch_dict["dire_team_id"]
                print (type(rtid))
                rname,dname=self.get_teamid_tostr(str(rtid),str(dtid))
                win_object=w()
                pickbans=amatch_dict["picks_bans"]
                self.no_pickbans_match=0
                if pickbans:
                    for a_pickban in pickbans:
                        if a_pickban["is_pick"]==True:
                                hero_id=a_pickban["hero_id"]
                                hero_name=self.hero_id_name[str(hero_id)]
                                if a_pickban["team"]==1:
                                    dire.append(int(hero_id))
                                else:
                                    radiant.append(int(hero_id))                
                    print("双方阵容:",radiant,dire)
                    full_result=self.query(6000,radiant,dire)
                    confirm=full_result.split(" ")[0].lower()
                    print ("预测结果:%s ----r:%s vs d:%s"%(full_result,rname,dname))
                    if win_object==confirm:
                        correct+=1
                    else:
                        self.predict_wrong.append([mid,rname,dname])
                else:
                    self.no_pickbans_match+=1
        print (correct,total,correct/total)#"缺少banpick数据的",self.no_pickbans_match
        print("预测错误的:",self.predict_wrong)
            # print (mid)
    def team_value(self):
    	return
    def pick_statistics(self,dataset_df, mmr_info="1"):
        x_data, y_data = dataset_df
        wins = np.zeros(129)
        games = np.zeros(129)
        pick_rate = np.zeros(129)

        for idx, game in enumerate(x_data):
            for i in range(258):
                if game[i] == 1:
                    games[i % 129] += 1

                    if y_data[idx] == 1:
                        if i < 129:
                            wins[i] += 1
                    else:
                        if i >= 129:
                            wins[i - 129] += 1
        pick_rate = games / np.sum(games)
        df=pd.read_csv("matches.csv")
        for heronum in range(129):
            # print ("%d号英雄使用情况"%(heronum+1),games[heronum],wins[heronum])#pick_rate[0])
            for i,j,rw in zip(df.radiant_team,df.dire_team,df.radiant_win):
                a,b=i.split(","),j.split(",")
                if str(heronum+1) in a:
                    if rw:
                        self.count[1]+=1  
                    self.count[0]+=1
                elif str(heronum+1) in b:
                    if not rw:
                        self.count[1]+=1
                    self.count[0]+=1
                #win_object=lambda:"radiant" if self.real_match[single_match]["randiant_win"] else "dire"
                # if False:
                #     self.count[0]+=1
                #     if self.real_match[single_match]["radiant_win"]==True and hero_id in radiant:
                #         self.count[1]+=1
                #     elif self.real_match[single_match]["radiant_win"]==False and hero_id in dire:
                #         self.count[1]+=1
            # print ("%d号英雄的情况"%(heronum+1),self.count[1],self.count[0])        
            self.count=[0,0]
        # assert 1>2
        pick_rate_dict = dict()
        win_dcit=dict()
        hero_dict = self.hero_id
        for heronum in range(1,130):
            try:
                pick_rate_dict[hero_dict[str(heronum)]] = [games[heronum-1],wins[heronum-1],games[heronum-1]-wins[heronum-1],(wins[heronum-1])/games[heronum-1]]#wins[heronum-1]/games[heronum-1]]
            except:
                continue
        sorted_pickrates = sorted(pick_rate_dict.items(), key=operator.itemgetter(1))
        print (sorted_pickrates[0])
        # assert 1>2
        print (len(sorted_pickrates))
        x_plot_data = [x[0] for x in sorted_pickrates]
        total_plot_data = [x[1][0] for x in sorted_pickrates]
        win_plot_data=[x[1][1] for x in sorted_pickrates]
        lose_plot_data=[x[1][2] for x in sorted_pickrates]

        xrange_num=np.arange(1,450,25)
        # print (x_plot_data,len(x_plot_data))
        # print (y_plot_data,len(y_plot_data))
        title = 'Hero pick rates at ' + ' MMR'
        y=np.arange(119)
        # plot1=plt.barh(y,total_plot_data,align='center')
        plot1=plt.barh(y,win_plot_data+lose_plot_data,align='center')
        #plot1=plt.barh(y,lose_plot_data,left=win_plot_data,align='center')

        # plot2=plt.barh(win_plot_data,x_plot_data,align='center')
        plt.yticks(y,x_plot_data)
        plt.xticks(xrange_num)

        # ax.invert_yaxis()
        plt.xlabel("pick num")
        plt.title("hero picks")
        plt.show()
        sorted_pickrates = sorted(pick_rate_dict.items(), key=lambda r:r[1][3])
        lose_rate=[x[1][3] for x in sorted_pickrates]
        x_plot_data = [x[0] for x in sorted_pickrates]
        plt.barh(y,lose_rate,align='center')
        xrange_num=np.arange(0,1,0.05)
        plt.yticks(y,x_plot_data)    
        plt.title("hero loserate")
        plt.xticks(xrange_num)
        plt.show()
    def winrate_statistics(self,dataset_df, mmr_info="1"):
        x_data, y_data = dataset_df

        wins = np.zeros(129)
        games = np.zeros(129)
        winrate = np.zeros(129)

        for idx, game in enumerate(x_data):
            for i in range(258):
                if game[i] == 1:
                    games[i % 129] += 1

                    if y_data[idx] == 1:
                        if i < 129:
                            wins[i] += 1
                    else:
                        if i >= 129:
                            wins[i - 129] += 1
        winrate = wins / games
        winrate_dict = dict()
        hero_dict = self.hero_id
        for i in range(129):
            try:
                winrate_dict[hero_dict[str(i)]] = winrate[i]
            except:
                continue
        sorted_winrates = sorted(winrate_dict.items(), key=operator.itemgetter(1))
        x_plot_data = [x[0] for x in sorted_winrates]
        y_plot_data = [x[1] for x in sorted_winrates]
        title = 'Hero winrates at ' + mmr_info + ' MMR'
        data = [go.Bar(
            y=x_plot_data,
            x=y_plot_data,
            orientation='h'
        )]
        layout = go.Layout(
            title=title,
            width=1000,
            height=1400,
            yaxis=dict(title='hero',
                       ticks='',
                       nticks=129,
                       tickfont=dict(
                           size=8,
                           color='black')
                       ),
            xaxis=dict(title='win rate',
                       nticks=30,
                       tickfont=dict(
                           size=10,
                           color='black')
                       )
        )
        fig = go.Figure(data=data, layout=layout)
        plt(data, filename='hero_win_1.html')
    def plot_learning_curve(self,x_train, y_train, subsets=200, mmr=None, cv=5, tool='matplotlib'):
        x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size=0.2)
        subset_sizes = np.exp(np.linspace(3, np.log(len(y_train)), subsets)).astype(int)
        results_list = [[], []]
        for subset_size in subset_sizes:
            logger.info('Performing cross validation on subset_size %d', subset_size)
            _, _, cv_score, roc_auc, _ = self.evaluate([x_train[:subset_size], y_train[:subset_size]],
                                                  [x_test, y_test], cv=cv)
            results_list[0].append(1 - cv_score)
            results_list[1].append(1 - roc_auc)
        if tool == 'matplotlib':
            self.plot_matplotlib(subset_sizes, results_list, mmr)
        #else:
            #plot_plotly(subset_sizes, results_list, mmr)
    def plot_matplotlib(self,subset_sizes, data_list, mmr):
        """ Plots learning curve using matplotlib backend.
        Args:
            subset_sizes: list of dataset sizes on which the evaluation was done
            data_list: list of ROC AUC scores corresponding to subset_sizes
            mmr: what MMR the data is taken from
        """
        plt.plot(subset_sizes, data_list[0], lw=2)
        plt.plot(subset_sizes, data_list[1], lw=2)
        plt.legend(['Cross validation error', 'Test error'])
        plt.xscale('log')
        plt.xlabel('Dataset size')
        plt.ylabel('Error')
        if mmr:
            plt.title('Learning curve plot for %d MMR' % mmr)
        else:
            plt.title('Learning curve plot')
        plt.show()
    def plot_plotly(self,subset_sizes, data_list, mmr):
        """ Plots learning curve using plotly backend.
        Args:
            subset_sizes: list of dataset sizes on which the evaluation was done
            data_list: list of ROC AUC scores corresponding to subset_sizes
            mmr: what MMR the data is taken from
        """
        if mmr:
            title = 'Learning curve plot for %d MMR' % mmr
        else:
            title = 'Learning curve plot'

        trace0 = go.Scatter(
            x=subset_sizes,
            y=data_list[0],
            name='Cross validation error'
        )
        trace1 = go.Scatter(
            x=subset_sizes,
            y=data_list[1],
            name='Test error'
        )
        data = go.Data([trace0, trace1])

        layout = go.Layout(
            title=title,

            xaxis=dict(
                title='Dataset size (logspace)',
                type='log',
                autorange=True,
                titlefont=dict(
                    family='Courier New, monospace',
                    size=15,
                    color='#7f7f7f'
                )
            ),
            yaxis=dict(
                title='Error',
                titlefont=dict(
                    family='Courier New, monospace',
                    size=15,
                    color='#7f7f7f'
                )
            )
        )
        fig = go.Figure(data=data, layout=layout)
        py.iplot(fig, filename='learning_curve_%dMMR' % mmr)
    def feture_vector_space(self,model,scalar,radiant_heroes,dire_heroes,synergies,counters,similarities,hero_released):
        return
    def match_duration(self,model,scalar,radiant_heroes,dire_heroes,synergies,counters,similarities,hero_released):
        return
    def match_team(self):
        return 
update_model=False
show_image=False
if update_model==True:
    pass
else:
    instance=Match_stat()
    # instance.iterate_file()
    # instance.save_everymatch_tocsv()#create dataset
    # instance.create_testset()#create testset
    # x=instance.train()
    # print (x)
    instance.single_query()
    instance.real_validation_set()
    if show_image:
        a,al=instance.read_dataset("matches.csv",advantages=True)
        instance.get_heroid_content()
        instance.pick_statistics(a)
    # instance.winrate_statistics(a)
# instance.get_heroid_content()
# b,al=instance.read_dataset("matches_testset.csv",advantages=True)
# evl_result=instance.evaluate(a,b,cv=5,save_model="model_"+str(datetime.date.today())+".pkl")
# instance.plot_learning_curve(a[0],a[1],subsets=200,cv=3,mmr=6000,tool='matplotlib')
# print (evl_result)
# instance.query_example()
# print (evl_result)

#instance.get_heroid_content()

#logger.info("First 5 rows from the mined dataframe are: \n%s", mined_df.head().to_string())



# instance.iterate_file()
#求二分组合后的二分排列
#求二分组后的子集,求10的子集,求10,<5的子集
#创造特征向量([1,1,0,1,1,0])
#根据特征向量的值决定预测值
#调整特征向量的取值决定,调整特征向量本身
#instance.d()
#instance.get_heroid_content()
#instance.build_team_hero_dict()
#instance.all_match_bp()
# x=instance.get_heroid_content()
# print (x)
