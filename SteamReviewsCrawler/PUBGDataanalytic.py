# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 19:26:08 2018

@author: Haosong
"""
import re
file=r'steam.txt'
data=[]
comment_date=[]
funny_scores=[]
comments=[]
with open(file,'r',encoding='UTF-8') as f:
    lines=f.readlines()
    #cleanerlines=lines.split('\n')
    #print(lines)
    for i in range(len(lines)):
        if(i%3==0):
            data.append(lines[i])
        elif(i%3==1):
            comment_date.append(lines[i])
        else:
            comments.append(lines[i])
            
            
        
        
#        if(re.search('[a-zA-Z]', line)):
##            print(line)
#            
##            if(line.find('Posted')!=-1):
##                print('------raw line below--------------')
##                print(line)
#            if(line.find('\t')==0):
#                comments.append(line.strip('\t'))
#            #print(line)
#            data=line.split('\t')
#
#            if(len(data)>1 and data[0].find('Posted')!=-1):
#                #print('----data below------')
#                #print(data)
#                funny_scores.append(data[1])

        '''
        data=line.split('\t')
        try:
            print(data)
            #print(data[1])
        except IndexError:
            pass
        '''

        #data=line.split(',')
        #print(data)
f.close()
#print(len(comments))
##print(comments[0])
##print(comments)
#print(len(funny_scores))
##print(funny_scores[0])
#print(funny_scores)

comments.append("No comments available")
print(len(data))
print(len(comment_date))
print(len(comments))
for info in data:
    print(info)
    #mixture=info.split('\t')
    #print(mixture)
#print(data[0].split('\t'))