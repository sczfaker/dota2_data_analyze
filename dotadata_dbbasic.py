import json
with open("D:\\cl\\reqdotadata\\dotadata_hero.json","r+") as f1,open("D:\\cl\\会用库_reqdotadata\\dotadata_item.json") as f2:
    d1,d2=json.load(f1),json.load(f2)
    p1,p2=d1.keys(),d2.keys()
    q1,q2=d1.values(),d2.values()

for i in q1:
   # for j in i:
   # print (len(i))
   # print (j)
   break
print ("-")
"""
hero [['ability', 9292], ['type', 24], ['talent', 264], ['base', 229], ['hotkey', 2], ['exp', 2]]
item [['name', 1], ['price', 4], ['attr_', 209], ['buildto', 57], ['buildfrom', 39], ['description', 953], ['position', 2]]
"""
# for i in q2:
#    for j in i:
#        print (j)#i[j],type(i[j]))
#    break

hero_max_len={}
for i in q1:
    for j in i:
        if j not in hero_max_len:
            hero_max_len[j]=[]
        hero_max_len[j].append(len(str(i[j])))

item_max_len={}
for i in q2 :
    for j in i:
        if j not in item_max_len:
            item_max_len[j]=[1]
        if type(i[j])!=int:
            item_max_len[j].append(len(str(i[j])))



hero_max_len=[[i,max(hero_max_len[i])]for i in hero_max_len]
item_max_len=[[i,max(item_max_len[i])]for i in item_max_len]
    #break
#for j in d2:



from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, Numeric, String
from sqlalchemy.orm import sessionmaker 
Base=declarative_base()
engine4 = create_engine('sqlite:///C:\\1cl\\dota_data.db')

def change_language():
    pass

class Points_position_team(Base):
    __tablename__ = 'cookies'
    uid=Column(Integer(), primary_key=True)
    teamname=Column(String(50), index=True)
    points=Column(Integer())
    potiential=Column(String(55))

class Hero_data(Base):
    __tablename__ = 'hero'
    uid=Column(Integer(), primary_key=True)
    hero_name=Column(String(40), index=True)
    ability=Column(String(hero_max_len[0][1]))
    type=Column(String(hero_max_len[1][1]))
    talent=Column(String(hero_max_len[2][1]))
    base=Column(String(hero_max_len[3][1]))
    hotkey=Column(String(hero_max_len[4][1]))
    exp=Column(String(hero_max_len[5][1]))

class Item_data(Base):
    __tablename__ = 'item'
    """docstring for Item_data"""
    uid=Column(Integer(), primary_key=True)
    item_name=Column(String(40), index=True)
    name=Column(String(item_max_len[0][1]))
    price=Column(String(item_max_len[1][1]))
    attr_=Column(String(item_max_len[2][1]))
    buildto=Column(String(item_max_len[3][1]))
    buildfrom=Column(String(item_max_len[4][1]))
    description=Column(String(item_max_len[5][1]))
    position=Column(String(item_max_len[6][1]))



class Personal_and_single_match(Base):
    __tablename__ = 'my'
    uid=Column(Integer(), primary_key=True)
    hero_name=Column(String(50), index=True)
#    initial_status=Column()
    potiential=Column(String(55))   




Session=sessionmaker(bind=engine4)
if __name__ == '__main__':
    Base.metadata.create_all(engine4)
    Session=sessionmaker(bind=engine4)
    session_instance=Session()
    count=0
    for name in d1:
        session_instance.add(Hero_data(uid=count,hero_name=name,ability=str(d1[name]["ability"]),type=str(d1[name]["type"]),talent=str(d1[name]["talent"]),base=str(d1[name]["base"]),hotkey=str(d1[name]["hotkey"]),exp=str(d1[name]["exp"])))
        count+=1
        # break
    session_instance.commit()