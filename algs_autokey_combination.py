#coding:utf-8
import pandas as pd
import sys,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

DICT_HOTKEY={}
DICT_HOTKEY_DOTA={}

class Autokey_combination(object):
    """docstring for Autokey"""
    def __init__(self):
        self.arg_righthand_pad=0
        exclude_cha=["!","@","#","$","%","^","&","*","(",")",'\x00', '\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07', '\x08', '\t', '\n', '\x0b', '\x0c', '\r', '\x0e', '\x0f', '\x10', '\x11', '\x12', '\x13', '\x14', '\x15', '\x16', '\x17', '\x18', '\x19', '\x1a', '\x1b', '\x1c', '\x1d', '\x1e', '\x1f']+list(range(64,91))+["\\","[","]",";","'","/",",",".","-","="]
        self.latter_set=[chr(i) for i in range(126) if chr(i) not in exclude_cha if i not in exclude_cha]+["F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","F11","F12"]+["Numpad0","Numpad1","Numpad2","Numpad3","Numpad4","Numpad5","Numpad6","Numpad7","Numpad8","Numpad9","NumpadDot","NumpadDiv","NumpadMult","NumpadAdd","NumpadSub","NumpadEnter","Up","Down","Left","Right"]
        self.machine_3={"4460":{},"4460S":{},"2200":{},"8100":{}}
        print (len(self.latter_set))
        self.prefix_control_ahk=self.subsequence(["^(ctrl)","#(win)","+(shift)","!(alt)"])
        print (self.latter_set,len(self.latter_set))
        self.arg_lefthand_pad=0
        self.default_mouse_binding={"按钮左上1":"1","按钮左上2":"2","按钮右上":"3","按钮侧上1":"4","按钮侧上2":"5","按钮侧上3":"6","侧下1":"8","侧下2":"9","侧中":"7","CPI":""}
        self.arg_righthand_mouse=0
        self.arg_doublehand_pad=0
        self.latterfix_control_ahk=[""]
        self.coding_smouse_binding={}
        self.simple_hero_type_set={"树精卫士":{},"天涯墨客":{},"杰奇落":{},"艾欧":{},"灰烬之灵":{},"复仇之魂":{},"邪影芳灵":{},"上古巨神":{},"水晶室女":{},"暗影萨满":{},"暗影恶魔":{},"干扰者":{},"龙骑士":{},"光之守卫":{},"军团指挥官":{},"莱恩":{},"莉娜":{},"拉比克":{},"沉默术士":{},"电炎绝手":{},"凤凰":{},"船长":{},"":{},"巫医":{},"宙斯":{},"沙王":{},"小小":{},"维萨吉":{},"石磷剑客":{},"谜团":{},"剧毒术士":{},"狙击手":{},"帕克":{},"怕个那":{},"巫妖":{},"祈求者":{},"魅惑魔女":{},"发条技师":{},"全能骑士":{},"司夜刺客":{}}
        print(self.simple_hero_type_set)
    def coding_combination(self):#机器的功能
        #现在我有三台可用机器,两台链接,一台链接互联网
        web_brower_set=["关闭标签1-12","新建标签","打开设置","打开网页截图","网页1-500"]
        codefile_set=[]
        sublime_editor_set=["wrap","打开","查找行","查找字符串","多相同值选择"]
        documentation_set=["打开图片内容","打开文档内容","打开文件夹内容","打开代码内容"]
        current_system_set=["打开网络设置","打开邻近电脑的其他同类设置(已共享)","打开文档库","打开单文件代码文件夹","打开常用软件文件夹","打开下载包文件夹","打开安装后文件夹","打开浏览器","打开指定目录emulator","打开代码库文件夹","打开笔记文件夹","打开搜索","打开图片库","打开截图工具","刷新快捷文件","打开比对工具","打开账本应用","打开指定网页","打开指定文件位置","打开sublime编辑器","删除文本","删除单行文本","删除指定规则文本"]
        developing_set=[]
        compare_software_set=[""]
        newauto_set=["在sublime打开指定前缀的单代码文件","打开一常用代码库","插入开发模板","打开常用图片","打开指定单个文件","打开代码库中指定单个文件","打开树json编辑器","打开图编辑器","执行日常数据抓取操作集合","执行单个据抓取操作集合","执行移动数据抓取操作","定时任务","打开一些笔记","打开指定笔记","打开/关闭语音识别采集","执行简单机器操作:旋转显示器","执行简单机器操作:倒水,浇水,打开关闭制冷制热","打开关闭ac","打开关闭n台pc服务器手机","查看互联网数据流向"]
        possible_hotkey={"双手键盘":[],"左手键盘":[],"右手鼠标":[],"右手键盘":[]}
        for machine in self.machine_3:
            if machine in ["4460","2200"]:#只要大部分文件夹可以同步,那么就只需要一套设置
                for key in ["sublime_editor_set","documentation_set","newauto_set","codefile_set","current_system_set"]:
                    self.machine_3[machine][key]={}
                    for value in eval(key):
                        self.machine_3[machine][key][value]={"hotkey":{},"address":{}}
            if machine in ["4460S","8100"]:
                for key in ["sublime_editor_set","newauto_set","web_brower_set","current_system_set"]:
                    self.machine_3[machine][key]={}
                    for value in eval(key):
                        self.machine_3[machine][key][value]={"hotkey":{},"address":{}}
        #一个操作对应一个hotkey
    def multiple_set_rules_combination(self,aset,possble_combination,n,cur):
        if n==len(aset):
            d=cur[:]
            possble_combination.append(d)
            return 
        else:
            for i in aset[n]:
                cur.append(i)
                self.multiple_set_rules_combination(aset,possble_combination,n+1,cur)
                cur.remove(i)
        return possble_combination
    def subsequence(self,nums):#def subsets(nums):
        n = len(nums)
        total = 1 << n
        res = set()
        for i in range(total):
            subset = tuple(num for j, num in enumerate(nums) if i & 1 << j)
            res.add(subset)
        return res
    def dota_combination(self):
        gui_set_element=["施法1","施法2","施法3","施法4","施法5","施法6","快速施法1","快速施法2","快速施法3","快速施法4","快速施法5","快速施法6","物品1","物品2","物品3","物品4","物品5","物品6","物品7","物品8","快速物品1","快速物品2","快速物品3","快速物品4","快速物品5","快速物品6","快速物品7","快速物品8","选中英雄","选中所有控制单位","攻击/强制攻击","固守原位","选中信使","信使运送物品","一键快速购买","下个单位","上个单位","第1组","第2组","第3组","第4组","第5组","第6组","第7组","第8组","第9组","第10组","镜头地点1","镜头地点1","镜头地点1","镜头地点1","镜头地点1","镜头地点1","镜头地点1","镜头地点1","镜头地点1","镜头地点1","信使爆发","信使护盾","一键购买部件","去除储仓储物品","打开商店","学习天赋","升级天赋","移动","径直走动","巡逻","取消当前动作","全选其他单位","激活符文","嘲讽物品","切换自动攻击","启用高级快速施法/智能施法","双击对自身施法","替换alt键","控制台","聊天","聊天所有人","语音聊天黑点","语音聊天所有人","聊天轮盘1","聊天轮盘2","英雄聊天轮盘","暂停","计分板","防止视角切换","选择队友1","选择队友2","选择队友3","选择队友4","选择队友5","屏蔽所有聊天","屏蔽敌方玩家聊天信息","频道中聊天信息在其他频道中显示","收到的消息显示未悄悄话","按住显示英雄位置","按住显示野怪刷新范围","按住显示防御塔攻击范围","施法时显示技能距离","禁用状态文字","隐藏伤害数值","单位查询覆盖英雄控制面板","在游戏界面上显示排队中的指令","色盲模式","区分队友血条","自动选择指针大小"]#"激活扫描"
        gui_set_element_2=["召唤单位自动攻击","按住停止键时禁用自动攻击","自动切换自动攻击","按键后快速施法","总是使用快捷键购买装备","商店打开时聚焦搜索框","智能攻击移动","自动点击鼠标右键","显示解说员所用数据","寻找到比赛时回到游戏","开始挑选英雄和比赛开始时回到游戏","暂停结束时回到游戏","就绪状态检测时回到游戏","启用控制台","使用plus助手","左键点击激活镜头反握","启用画面晃动","观战时视角平滑拖拽","视角减速","公开比赛数据","屏蔽来自非好友的组队邀请","未开放组队时隐藏组队状态","开放组队时不自动接受邀请","工会伙伴和好友","仅限好友","任何人","网络质量","动态调整小地图英雄图表","取消对目标施放的技能后移动","死亡后视角颜色改变","显示网络信息","隐藏载入界面中的小贴士","默认不泄露联赛结果","新物品自动添加到收藏室","使用鼠标实现主界面","绝对单排比赛"]
        self.group_controlset_normal=["selfhero","allother_unit_without_hero","fu_illution1","fu_illution2","item_illution1","item_illution2","control_musk","dead_book1","dead_book2"]#dota2有十二个编队
        self.skill_illusion=["ilusion1","ilusion2","ilusion3","ilusion4"]
        self.animal_call=["地狱火1","地狱火2","地狱火3","地狱火4","地狱火5"]
        self.mini_enigma=["小谜团1","小谜团2","小谜团3","小谜团4","小谜团5","小谜团6"]
        self.mini_wolf=["小狼1","小狼2"]
        self.mini_treeman=["树人1","树人2","树人3","树人4","树人5"]
        self.gree_guard=["蛇棒绿"]
        self.yellow_guard=["蛇棒红"]
        self.jungle_control=["","","","","","","","","","","","","","","","","",""]
        self.hog=["hog1","hog2"]
        self.grooup_control_13=["1","2","3","4","5","6","7","8","9","10","selfhero","allother_unit_without_hero","all_unit"]
        x=pd.read_csv("pd_hero.csv")
        for i in x:
            print (i)
        for hero in self.simple_hero_type_set:
            for operation in gui_set_element+gui_set_element_2:
                self.simple_hero_type_set[hero][operation]={"place":"","command_name":"","binding":"","cfg_code_place":""}
        print(len(gui_set_element))
    def hotkey_combination(self):
        self.p_opereations=self.multiple_set_rules_combination([self.prefix_control_ahk,self.latter_set],[],0,[])
        self.simple_hero_type_set_2={}
        # self.hotkey={"documentation":{},"codefile":{},"website":{},"notes":{},"folder":{"2ts","pv","3wea","1cl_0505","4tup","",""},"software":{"sublime","selfrefresh","vivaldi","sumatra","emulator","emulator_git","bccompare","lantern","capture","snipaste"}}

    #   command_set_element=[]

    #   possible_hotkey={"双手键盘":[],"左手键盘":[],"右手鼠标":[],"右手键盘":[]}
    #   return hero_dict#一个操作英雄对应一个鼠标和cfg rsetting
instance=Autokey_combination()
#a.hotkey_combination()
DOTA,Hotkey=True,True
if DOTA:
    instance.dota_combination()