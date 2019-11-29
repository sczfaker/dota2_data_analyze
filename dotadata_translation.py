#coding:utf-8
from json import dump,load
from os import path,listdir
import os,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding="utf-8")
"""
troll-warlord 巨魔
shadow-fiend 影魔
witch-doctor 巫医
juggernaut 剑圣
phoenix 凤凰
sniper 矮人火枪手
anti-mage 敌法师
tinker 修补匠
oracle 神谕者
chen 陈
winter-wyvern 寒冬飞龙
legion-commander 军团指挥官
natures-prophet 先知
morphling 变体精灵
lina 莉娜
jakiro 杰奇洛
leshrac 拉西克
razor 剃刀
lion 莱恩
medusa 美杜莎
tidehunter 潮汐猎人
disruptor 干扰者
clockwerk 发条技师
mirana 米拉娜
omniknight 全能骑士
spirit-breaker 白牛
doom 末日使者
skywrath-mage 天怒法师
lycan 狼人
nyx-assassin 甲虫刺客
meepo 米波
faceless-void 虚空假面
techies 工程师
broodmother 育母蜘蛛
ancient-apparition 远古冰魄
ogre-magi 
necrophos 瘟疫法师
tusk 巨牙海明
chaos-knight 混沌骑士
magnus 马格纳斯
mars 马尔斯
keeper-of-the-light 光之守卫
templar-assassin 圣堂刺客
crystal-maiden 冰晶侍女
terrorblade 恐怖利刃
huskar 哈斯卡
slark 斯拉克
dark-willow 邪影芳灵
clinkz 克林克兹
arc-warden 天穹
rubick 拉比克
queen-of-pain 痛苦女王
slardar 斯拉达
warlock 术士
elder-titan 上古巨神
enchantress 魅惑魔女
bristleback 刚被猪
grimstroke 墨客
io 艾欧
vengeful-spirit 复仇之魂
lone-druid 德鲁伊
monkey-king 齐天大圣
lich 巫妖
centaur-warrunner 半人马
pangolier 剑客
zeus 宙斯
treant-protector 树精卫士
lifestealer 噬魂狗
underlord 地狱领主
death-prophet 死亡先知
dazzle 戴泽
pugna 帕格纳
wraith-king 骷髅王
beastmaster 兽王
ember-spirit 灰烬
earth-spirit 大地之灵
phantom-lancer 幻影骑士
night-stalker 夜魔
undying 不朽尸王
phantom-assassin 幻影刺客
dragon-knight 龙骑士
venomancer 剧毒术士
sand-king 沙王
silencer 沉默术士
shadow-demon 暗影恶魔
storm-spirit 风暴之灵
axe 斧王
alchemist 炼金术师
earthshaker 憾地者
outworld-devourer 殁境守护者
bounty-hunter 赏金猎人
gyrocopter 直升机
viper 冥界亚龙
drow-ranger 卓尔游侠
bane 霍乱之源
shadow-shaman 萨满
invoker 祈求者
brewmaster 酒仙
spectre 幽鬼
visage 飞龙
dark-seer 黑暗贤者
luna 月之骑士
kunkka 昆卡
sven 斯文
timbersaw 伐木机
enigma 恩格尼码
riki 隐形刺客
ursa 大熊
tiny 小小
naga-siren 娜迦海妖
puck 帕克
pudge 屠夫
weaver 蚂蚁
windranger 风行者
bloodseeker 血魔
abaddon 亚巴顿
batrider 蝙蝠
void-spirit 虚无之灵
snapfire 电炎绝手
"""
the_herolist_eng=['troll-warlord', 'shadow-fiend', 'witch-doctor', 'juggernaut', 'phoenix', 'sniper', 'anti-mage', 'tinker', 'oracle', 'chen', 'winter-wyvern', 'legion-commander', 'natures-prophet', 'morphling', 'lina', 'jakiro', 'leshrac', 'razor', 'lion', 'medusa', 'tidehunter', 'disruptor', 'clockwerk', 'mirana', 'omniknight', 'spirit-breaker', 'doom', 'skywrath-mage', 'lycan', 'nyx-assassin', 'meepo', 'faceless-void', 'techies', 'broodmother', 'ancient-apparition', 'ogre-magi', 'necrophos', 'tusk', 'chaos-knight', 'magnus', 'mars', 'keeper-of-the-light', 'templar-assassin', 'crystal-maiden', 'terrorblade', 'huskar', 'slark', 'dark-willow', 'clinkz', 'arc-warden', 'rubick', 'queen-of-pain', 'slardar', 'warlock', 'elder-titan', 'enchantress', 'bristleback', 'grimstroke', 'io', 'vengeful-spirit', 'lone-druid', 'monkey-king', 'lich', 'centaur-warrunner', 'pangolier', 'zeus', 'treant-protector', 'lifestealer', 'underlord', 'death-prophet', 'dazzle', 'pugna', 'wraith-king', 'beastmaster', 'ember-spirit', 'earth-spirit', 'phantom-lancer', 'night-stalker', 'undying', 'phantom-assassin', 'dragon-knight', 'venomancer', 'sand-king', 'silencer', 'shadow-demon', 'storm-spirit', 'axe', 'alchemist', 'earthshaker', 'outworld-devourer', 'bounty-hunter', 'gyrocopter', 'viper', 'drow-ranger', 'bane', 'shadow-shaman', 'invoker', 'brewmaster', 'spectre', 'visage', 'dark-seer', 'luna', 'kunkka', 'sven', 'timbersaw', 'enigma', 'riki', 'ursa', 'tiny', 'naga-siren', 'puck', 'pudge', 'weaver', 'windranger', 'bloodseeker', 'abaddon', 'batrider',"void-spirit","snapfire"]
the_herolist_ch=["巨魔","影魔","巫医","剑圣","凤凰","矮人火枪手","敌法师","修补匠","神谕者","陈","寒冬飞龙","军团指挥官","先知","变体精灵","莉娜","杰奇洛","拉西克","剃刀","莱恩","美杜莎","潮汐猎人","干扰者","发条技师","米拉娜","全能骑士","白牛","末日使者","天怒法师","狼人","甲虫刺客","米波","虚空假面","工程师","育母蜘蛛","远古冰魄","","瘟疫法师","巨牙海明","混沌骑士","马格纳斯","马尔斯","光之守卫","圣堂刺客","冰晶侍女","恐怖利刃","哈斯卡","斯拉克","邪影芳灵","克林克兹","天穹","拉比克","痛苦女王","斯拉达","术士","上古巨神","魅惑魔女","刚被猪","墨客","艾欧","复仇之魂","德鲁伊","齐天大圣","巫妖","半人马","剑客","宙斯","树精卫士","噬魂狗","地狱领主","死亡先知","戴泽","帕格纳","骷髅王","兽王","灰烬","大地之灵","幻影骑士","夜魔","不朽尸王","幻影刺客","龙骑士","剧毒术士","沙王","沉默术士","暗影恶魔","风暴之灵","斧王","炼金术师","憾地者","殁境守护者","赏金猎人","直升机","冥界亚龙","卓尔游侠","霍乱之源","萨满","祈求者","酒仙","幽鬼","飞龙","黑暗贤者","月之骑士","昆卡","斯文","伐木机","恩格尼码","隐形刺客","大熊","小小","娜迦海妖","帕克","屠夫","蚂蚁","风行者","血魔","亚巴顿","蝙蝠","虚无之灵","电炎绝手"]

the_hero_converted_dic={'troll-warlord':"巨魔",'shadow-fiend': '影魔', 'witch-doctor': '巫医','juggernaut': '剑圣', 'phoenix': '凤凰', 'sniper': '矮人火枪手', 'anti-mage': '敌法师', 'tinker': '修补匠', 'oracle': '神谕者', 'chen': '陈', 'winter-wyvern': '寒冬飞龙', 'legion-commander': '军团指挥官', 'natures-prophet': '先知', 'morphling': '变体精灵', 'lina': '莉娜', 'jakiro': '杰奇洛', 'leshrac': '拉西克', 'razor': '剃刀', 'lion': '莱恩', 'medusa': '美杜莎', 'tidehunter': '潮汐猎人', 'disruptor': '干扰者', 'clockwerk': '发条技师', 'mirana': '米拉娜', 'omniknight': '全能骑士', 'spirit-breaker': '白牛', 'doom': '末日使者', 'skywrath-mage': '天怒法师', 'lycan': '狼人', 'nyx-assassin': '甲虫刺客', 'meepo': '米波', 'faceless-void': '虚空假面', 'techies': '工程师', 'broodmother': '育母蜘蛛', 'ancient-apparition': '远古冰魄', 'ogre-magi': '', 'necrophos': '瘟疫法师', 'tusk': '巨牙海明', 'chaos-knight': '混沌骑士', 'magnus': '马格纳斯', 'mars': '马尔斯', 'keeper-of-the-light': '光之守卫', 'templar-assassin': '圣堂刺客', 'crystal-maiden': '冰晶侍女', 'terrorblade': '恐怖利刃', 'huskar': '哈斯卡', 'slark': '斯拉克', 'dark-willow': '邪影芳灵', 'clinkz': '克林克兹', 'arc-warden': '天穹', 'rubick': '拉比克', 'queen-of-pain': '痛苦女王', 'slardar': '斯拉达', 'warlock': '术士', 'elder-titan': '上古巨神', 'enchantress': '魅惑魔女', 'bristleback': '刚被猪', 'grimstroke': '墨客', 'io': '艾欧', 'vengeful-spirit': '复仇之魂', 'lone-druid': '德鲁伊', 'monkey-king': '齐天大圣', 'lich': '巫妖', 'centaur-warrunner': '半人马', 'pangolier': '剑客', 'zeus': '宙斯', 'treant-protector': '树精卫士', 'lifestealer': '噬魂狗', 'underlord': '地狱领主', 'death-prophet': '死亡先知', 'dazzle': '戴泽', 'pugna': '帕格纳', 'wraith-king': '骷髅王', 'beastmaster': '兽王', 'ember-spirit': '灰烬', 'earth-spirit': '大地之灵', 'phantom-lancer': '幻影骑士', 'night-stalker': '夜魔', 'undying': '不朽尸王', 'phantom-assassin': '幻影刺客', 'dragon-knight': '龙骑士', 'venomancer': '剧毒术士', 'sand-king': '沙王', 'silencer': '沉默术士', 'shadow-demon': '暗影恶魔', 'storm-spirit': '风暴之灵', 'axe': '斧王', 'alchemist': '炼金术师', 'earthshaker': '憾地者', 'outworld-devourer': '殁境守护者', 'bounty-hunter': '赏金猎人', 'gyrocopter': '直升机', 'viper': '冥界亚龙', 'drow-ranger': '卓尔游侠', 'bane': '霍乱之源', 'shadow-shaman': '萨满', 'invoker': '祈求者', 'brewmaster': '酒仙', 'spectre': '幽鬼', 'visage': '飞龙', 'dark-seer': '黑暗贤者', 'luna': '月之骑士', 'kunkka': '昆卡', 'sven': '斯文', 'timbersaw': '伐木机', 'enigma': '恩格尼码', 'riki': '隐形刺客', 'ursa': '大熊', 'tiny': '小小', 'naga-siren': '娜迦海妖', 'puck': '帕克', 'pudge': '屠夫', 'weaver': '蚂蚁', 'windranger': '风行者', 'bloodseeker': '血魔', 'abaddon': '亚巴顿', 'batrider': '蝙蝠',"void-spirit":"虚无之灵","snapfire":"电炎绝手"}

# for i,j in zip(the_herolist_eng,the_herolist_ch):
# 	the_convert_dic[i]=j
# for i in the_convert_dic:
# 	print (i+":"+the_convert_dic[i])
# print(the_convert_dic)

for i in the_hero_converted_dic:
	print (i,the_hero_converted_dic[i])
class Hotkey(object):
	def __init__(self):
		self.set={"":[],"":[]}

class CommandInsideGame(object):
	def __init__(self):
		self.set={"":[],"":}

