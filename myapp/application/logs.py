# coding:utf-8

import os
import glob
import csv
import MeCab
import array
import numpy as np
import pickle
import cgi

# login: ログイン時
# tweet in window: 画面内にある投稿
# 

# ログ内容をファイルに記録
def regist_log(time,user_id,about,data1,data2):
    data = [time,user_id,about,data1,data2]
    with open(os.getcwd()+'/myapp/application/'+user_id+'_logs.csv','a') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(data)