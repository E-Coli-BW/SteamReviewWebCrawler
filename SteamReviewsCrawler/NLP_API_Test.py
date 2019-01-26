# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 13:58:27 2018

@author: Haosong
"""

import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt
from nltk.classify import NaiveBayesClassifier
data=pd.read_csv('Sleep_is_Good_PUBGSteamReview.csv')
#print(data.columns.values)
#print(data.head())
df=pd.DataFrame(data=data)
print(df.head())
comments=df['comment']
attitudes=df['attitude']
'''preprocess comments data'''
'''need to split everyword and store it as a dictionary'''
def preprocess(text):
    return {word:True for word in text.lower().split()}
#print(comments[1])
'''split the data'''
print(len(comments))
comment_training=comments[:len(comments)//5]
comment_testing=comments[len(comments)//5:]



attitude_training=attitudes[:len(attitudes)//5]
attitude_testing=attitudes[len(attitudes)//5:]

'''preprocess attitude_training'''
'''
for attitude in attitude_training:
    if(attitude=='Recommended'):
        attitude='pos'
    else:
        attitude='neg'
'''        
processed_training_comment=[preprocess(text) for text in comment_training]
training_data=[list(l) for l in zip(processed_training_comment,attitude_training)]

'''feed training data to model'''
model=NaiveBayesClassifier.train(training_data)
processed_testing_comment=[preprocess(text) for text in comment_testing]
res=[model.classify(item) for item in processed_testing_comment]
print('predicted overall attitude:')
from collections import Counter
word_count=Counter(res)
print(word_count.most_common(1))

print('model accuracy:')
count=0
for predict,real in zip(res,attitude_testing):
    if (predict==real):
        count+=1
print(count/len(res))