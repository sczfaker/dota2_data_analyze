class net():
    def __init__(self):
        pass
    def function():
        pass
import os
import time
import random
from requests import get
from fake_useragent import UserAgent
ua = UserAgent()
#print (os.path.exists())
REPLAY_DIR="replay_full_files"
fcount=0
class Generate_rl_queue(object):
    """docstring for ClassName"""
    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg

REPLAY=True
if REPLAY:
    if not os.path.exists("replay_full_files"):
        os.mkdir("replay_full_files")
    with open("replays_url_versioncontrol.txt","r+") as f:
        list_of_replay_get_file=f.readlines()
        print (list_of_replay_get_file)
        headers={"user-agent":ua.random}
        for replay_url in list_of_replay_get_file:
            ffci=replay_url.split("/")
            #print(ffci)
            filename_dem_replay=ffci[4].strip()
            print (filename_dem_replay)
            absolute_path=REPLAY_DIR+'/'+filename_dem_replay
            if (os.path.exists(absolute_path) and os.path.getsize(absolute_path)<1e4) or os.path.exists(absolute_path)==False:
                with open(REPLAY_DIR+"/"+filename_dem_replay,"wb") as f:
                    replay_content=get(replay_url,headers=headers,timeout=15).content
                    print ("容量:",len(replay_content))
                    try:
                        f.write(replay_content)
                        print("ok")
                        fcount+=1
                        time_stamp=random.randint(6,12)
                        time.sleep(time_stamp)
                    except:
                        assert 1>10
            else:
                print (filename_dem_replay)
class Crawl_replay_from_fboard():
    def __init__(self):
        if not os.path.exists("replay_full_files"):
            os.mkdir("replay_full_files")
        with open("replays_url_versioncontrol.txt","r+") as f:
            list_of_replay_get_file=f.readlines()
print (fcount) 