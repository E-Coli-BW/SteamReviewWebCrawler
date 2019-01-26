# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 22:50:59 2018

@author: Haosong
"""

import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

data=pd.read_csv('Sleep_is_Good_PUBGSteamReview.csv')
#print(data.columns.values)
#print(data.head())
df=pd.DataFrame(data=data)


'''Let's get some info out of this bunch of data!'''
'''average hours played'''
hours=df['hour']
hours=hours.str.replace(',','')
hours=hours.astype(float)
#print(df.head())
#hours_data=df
print('average hours played by the reviewers of PUBG:')

print(hours.mean())

'''overall attitude towards PUBG'''
attitude=df['attitude']
attitude=attitude.str.replace('Not Recommended','-1')
attitude=attitude.str.replace('Recommended','1')
attitude=attitude.astype(float)
print('Overall attitude towards PUBG: -1 as really negative,1 as really positive')
print(attitude.mean())

'''For those who have more than 50 products what's their attitude?'''
print("Total number of player:")
print(len(df.index))
numProdOwn=df['numProdOwn'].str.replace(',','').astype(float)
crazyPlayers=numProdOwn[numProdOwn>50]
print("Number of reviewers who has more than 50 products in accout")
print(len(crazyPlayers.index))
print("percentage:")
print('{} %'.format(len(df.index)/len(crazyPlayers.index)))
print('For these players. overall attitude towards PUBG is :')
crazy_player_attitude=df[df['numProdOwn'].str.replace(',','').astype(float)>50]['attitude']
crazy_player_attitude=crazy_player_attitude.str.replace('Not Recommended','-1')
crazy_player_attitude=crazy_player_attitude.str.replace('Recommended','1')
crazy_player_attitude=crazy_player_attitude.astype(float)
print(crazy_player_attitude.mean())
