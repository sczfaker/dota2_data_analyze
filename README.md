# 电竞游戏比赛数据分析(dota2)


## Author:suigvc

## 相关链接
[项目链接](https://github.com/tisttsf/esports_dota2_data_analyze.git)
[github个人账户链接](https://github.com/tisttsf)
[gitee个人账户链接](https://gitee.com/DataTraveler_0817)
## 主要功能概述

### 从dotabuff,liquidpedia(获取比赛参赛队伍,奖金,日期等相关信息),dotamax(未完成登录部分),opendota,抓取游戏相关数据,从抓取实时BP数据

### 主要文件功能描述
+  dota_matchid_0727.py 
> 训练生成天梯比赛的逻辑预测模型
> 使用实时比赛的选人数据进行预测(需要联网抓取实时)
+ compare_and_backup.py
> 手动验证模型的正确率与随机预测比较
+ replay_check.py
+ dotadata_deepkeras.py
> keras深度的模型预测
> 抓取录像文件
+ fiddler_to_py.py
> 将fiddler抓到的请求转为python requests请求,主要附带了请求的cookie参数和,避免了反复手动编写请求头
+ dotadata_opendota
> 从opendota获取数据提供网站整理好的提前比赛数据
+ dota2_ingame_data_analysis.py
> 相比bp数据分析进行更加复杂的模型生成
+ auto_chess_one.py
> 刀塔自走棋概率计算
+ dota_matchid_0727.py
> 从dotabuff网站抓取相关tournament比赛id 生成的idfile用于
+ dotadata_mining_banpick.py
> 从实时比赛数据提供网站抓取BP数据(可扩展抓取其他相关数据)
+ dota_pro.py
> 生成只有职业比赛BP数据的逻辑回归模型
+ train_data_helper.py
> 检测为生成模型准备的清洗过后的数据集是否正确
+ dotadata_normal_matchid.py
> 获取指定id的近期比赛数据
+ dotadata_ch_eng_item.py
> 游戏基本数据(物品,英雄,建筑,野怪,地图)
+ dotadata_teamvalue.py
> 获取比赛参赛队伍的数据,保存到currenet_p_team,其中"current_state"的Player_dict保存了5名选手的信息1,表示核心,2表示中单,3表示劣单,4表示辅助,5表示辅助


## 具体步骤描述
### 使用pandas,numpy,sklearn,keras等数据分析与机器学习工具进行建模
		1.使用numpy,pandas进行数据清洗,比如moba游戏a(这里指dota2)有129个英雄,我们用read_csv读取抓取处理好的csv,有n条比赛数据(一共有(比赛id,选人序号,胜负方,平均分,时长这几个需要使用的数据特征),然后进行筛选,比如4000mmr以上和20分钟以上的比赛,然后建立一个129*129的numpy矩阵,对每一场出现的22对抗组合和22协作组合进行统计出场胜率.保存在2个129*129的numpy特征矩阵里
		2.对每场比赛建一个向量,然后一起组成一个矩阵,里面包含胜率和选人,然后进行数据整理
		3.使用sklearn,keras进行生成模型并预测
## 待做
		1.第二步抓取特定比赛的录像文件批量保存,使用(dota-clarity([]())或manta([]()))进行录像数据解析
		2.每场有效比赛大概有大于150000条选人胜负段位时长数据,需要根据游戏本身过程清洗出有利于预测分析的数据
		3.结合选人数据,选手数据,具体游戏内数据进行数据分析机器学习
#### 获取实时比赛的数据,并传入参数进已经训练好的模型进行相关(比如胜负预测)
    1.测试模型的准确性
    2.给出实时预测并确认结果
#### 使用matplotlib等工具绘图(绘制,直观胜率,学习曲线)
#### 安装包要求参考 requirement.txt文件
