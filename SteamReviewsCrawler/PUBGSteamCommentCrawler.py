# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 02:51:47 2018
This crawler is for crawling down steam reviews 
As of Dec 22 2018, you can use it as a genral purpose crawler
I originally wrote it for crawling down PUBG comment, however
as long as you know the appid of a particular game
you can just change the number in the url section 
then it is totally good to use on a new steam game
However, currently it seems that the crawler canot get the nickname of the reviewer
For instance, the appid of H1N1is 433850, the appid of PUBG is 5780080 so you can just change the 
id in url to crawl down info of a different game as long as you know the appid of it

Also, you can crawl down Chinese and English version of the comments(The Chinese Steam is locked so 
it has a different link to the review section)

The for i in range(1,100) section is to set how many pages of comments you wish to crawl done
You can modify it to while(True) break statements if you wish to crawl down all the comments of a 
particular game

@author: Haosong
"""
import itertools
import re
import requests
from bs4 import BeautifulSoup
from time import sleep


def getFunnyHelpfulLevel(review):
    funny_helpful = review.find('div', {'class': 'found_helpful'}).text
    #print(funny_helpful)
    raw_num=re.findall(r'\d+',funny_helpful)
    helpful=-1
    funny=-1
    if(not raw_num):
        helpful=-1
        funny=-1
    #print(raw_num)
    for item in raw_num:
        if(len(raw_num)==0):
            helpful=0
            funny=0
        elif(len(raw_num)==1):
            helpful=raw_num[0]
            funny=0
        elif(len(raw_num)==2):
            helpful=int(raw_num[0])
            funny=int(raw_num[1])
        else:
            helpful=int(raw_num[0]+raw_num[1])
            if(len(raw_num)==3):
                funny=int(raw_num[-1])
            else:
                funny=int(raw_num[-2]+raw_num[-1])
    return [helpful,funny]
'''Lists to store catagorical data'''
funny_List=[]
helpful_List=[]
numProdOwn_List=[]
attitude_List=[]
hour_List=[]
comment_List=[]

#url='https://steamcommunity.com/app/578080/reviews/?browsefilter=toprated&snr=1_5_100010_'
#url='https://steamcommunity.com/app/578080/homecontent/?userreviewsoffset=30&p=4&workshopitemspage=4&readytouseitemspage=4&mtxitemspage=4&itemspage=4&screenshotspage=4&videospage=4&artpage=4&allguidepage=4&webguidepage=4&integratedguidepage=4&discussionspage=4&numperpage=10&browsefilter=toprated&browsefilter=toprated&appid=578080&appHubSubSection=10&appHubSubSection=10&l=english&filterLanguage=default&searchText=&forceanon=1'
'''Uncomment this if you wish to write the results to file'''

file = open('PUBGSteamReview.csv', 'w+', encoding='utf-8')

headers = {'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'}
'''
Write file into CSV, I originally plan to write to db but pymysql is full of fucking dam bugs
'''
import csv
#big_list=zip(funny_List,helpful_List,numProdOwn_List,attitude_List,hour_List,comment_List)
csvData=[['funny','helpful','numProdOwn','attitude','hour','comment']]
#for item in big_list:
#    csvData.append(item)
# =============================================================================
# with open('PUBGSteamReview.csv','w+',encoding='utf-8') as f:
#     writer=csv.writer(f)
#     writer.writerows(csvData)
# f.close()
# =============================================================================
writer=csv.writer(file)
writer.writerows(csvData)
for i in range(1,10000):
    '''
    English Version Comment url
    '''
    '''
    The following url info is gained by preserving log and scrolling down, then see what's the requests 
    look like in
    ''' 
    '''
    XHR(Cross-domain requests)  
    '''
    '''
    section!!!
    '''
    url='http://steamcommunity.com/app/433850/homecontent/?userreviewsoffset='\
    + str(10 * (i - 1)) + '&p=' + str(i) + '&workshopitemspage=' + str(i)\
    + '&readytouseitemspage=' + str(i) + '&mtxitemspage=' + str(i) + '&itemspage=' + str(i)\
    + '&screenshotspage=' + str(i) + '&videospage=' + str(i) + '&artpage=' + str(i)\
    + '&allguidepage=' + str(i) + '&webguidepage=' + str(i) + '&integratedguidepage=' + str(i)\
    + '&discussionspage=' + str(i)\
    + '&numperpage=10&browsefilter=toprated&browsefilter=toprated&appid=433850&appHubSubSection=10&l=english&filterLanguage=default&searchText=&forceanon=1'
    
    '''
    Chinese Versiion Comment url
    '''
    '''
    url='http://steamcommunity.com/app/433850/homecontent/?userreviewsoffset='\
    + str(10 * (i - 1)) + '&p=' + str(i) + '&workshopitemspage=' + str(i)\
    + '&readytouseitemspage=' + str(i) + '&mtxitemspage=' + str(i) + '&itemspage=' + str(i)\
    + '&screenshotspage=' + str(i) + '&videospage=' + str(i) + '&artpage=' + str(i)\
    + '&allguidepage=' + str(i) + '&webguidepage=' + str(i) + '&integratedguidepage=' + str(i)\
    + '&discussionspage=' + str(i) + '&numperpage=10&browsefilter=toprated&browsefilter=toprated&appid=433850&appHubSubSection=10&l=schinese&filterLanguage=default&searchText=&forceanon=1'
    '''
    try:
        htmlObj=requests.get(url,headers=headers)
        sleep(1)
    except requests.exceptions.ConnectionError:
        pass
    html = requests.get(url,headers=headers).text
    #print(html)
    if(htmlObj.status_code == 404):
        break
    soup = BeautifulSoup(html, 'lxml')
    reviews = soup.find_all('div', {'class': 'apphub_UserReviewCardContent'})
    
    '''
    use headers to mimic browser so that we can get all of the reviews
    '''
    #print(reviews)        
    for review in reviews:
        '''
        First get the helpful and useful score
        '''
        funny_helpful=getFunnyHelpfulLevel(review)
        funny=funny_helpful[1]
        helpful=funny_helpful[0]
        '''
        Then Get the user id and review content
        '''
        nick = review.find('div', {'class': 'apphub_CardContentAuthorName'})
        numProdOwn=soup.find('div',{'class':'apphub_CardContentMoreLink ellipsis'}).text.split(" ")[0]
        attitude=review.find('div', {'class': 'title'}).text
        hour = review.find('div', {'class': 'hours'}).text.split(' ')[0]
        #link = nick.find('a').attrs['href']
        date_posted=soup.find('div',{'class':'date_posted'}).text
        comment = review.find('div', {'class': 'apphub_CardTextContent'}).text
        '''
        write to csv file
        '''
        #'funny','helpful','numProdOwn','attitude','hour','comment'
        writer.writerows([[funny,helpful,numProdOwn,attitude,hour,comment]])
file.close()
# =============================================================================
#         '''data analytic preparation'''
#         funny_List.append(funny)
#         helpful_List.append(helpful)
#         numProdOwn_List.append(numProdOwn)
#         attitude_List.append(0 if attitude=='Not Recommended' else 1)
#         hour_List.append(hour)
#         comment_List.append(comment)
#         '''data analytic preparation ends'''
# =============================================================================
# =============================================================================
#         
#         '''Uncomment this if you wish to write the results to file''' 
#         '''
#         file.write(
#                 str(date_posted) +'\t' + str(funny) +'\t' + str(helpful) +'\t' +str(nick) +'\t' + str(numProdOwn) +'\t' + str(hour) +'\t' + str(attitude) +'\t' + str(comment).strip('\t') +'\n'
#                 )
#         '''
# '''Uncomment this if you wish to write the results to file'''
# '''
# file.close()
# '''
# =============================================================================
# =============================================================================
# print(len(funny_List),len(helpful_List),len(numProdOwn_List),len(attitude_List),len(hour_List),len(comment_List))
# 
# 
# =============================================================================


# =============================================================================
# 
# '''
# build a dictionary from funny score and comments to extract funniest comments in H1Z1
# comment as key
# funny as value
# '''
# rank_dict=dict(zip(comment_List,funny_List))
# '''write a helper function to extract top-n funniest comments from rank_dict'''
# def order_dict(dicts, n):
#     result = []
#     result1 = []
#     p = sorted([(k, v) for k, v in dicts.items()], reverse=True)
#     s = set()
#     for i in p:
#         s.add(i[1])
#     for i in sorted(s, reverse=True)[:n]:
#         for j in p:
#             if j[1] == i:
#                 result.append(j)
#     for r in result:
#         result1.append(r[0])
#     return result1
# 
# top10=order_dict(rank_dict,10)
# for comment in top10:
#     print(comment)
#     print('===funny score==')
#     print(rank_dict[comment])
# =============================================================================
'''
        funny_helpful = review.find('div', {'class': 'found_helpful'}).text
        raw_num=re.findall(r'\d+',funny_helpful)
        for item in raw_num:
            if(len(raw_num)==2):
                helpful=int(raw_num[0])
                funny=int(raw_num[1])
            else:
                helpful=int(raw_num[0]+raw_num[1])
                if(len(raw_num)==3):
                    funny=int(raw_num[-1])
                else:
                    funny=int(raw_num[-2]+raw_num[-1])
        #print("helpful:{}, funny:{}".format(helpful,funny))
        
'''
'''
'''
    #Get the user id and review content
'''
    for review in reviews:
        #nick=soup.find('div',{'class':"apphub_CardContentAuthorName in-game ellipsis"}).text
        nick = review.find('div', {'class': 'apphub_CardContentAuthorName'})
        numProdOwn=soup.find('div',{'class':'apphub_CardContentMoreLink ellipsis'}).text.split(" ")[0]
        attitude=review.find('div', {'class': 'title'}).text
        hour = review.find('div', {'class': 'hours'}).text.split(' ')[0]
        #link = nick.find('a').attrs['href']
        date_posted=soup.find('div',{'class':'date_posted'}).text
        comment = review.find('div', {'class': 'apphub_CardTextContent'}).text
        print(nick,numProdOwn,attitude,hour,date_posted,comment)
        
    
    
        #title = review.find('div', {'class': 'title'}).text
        #hour = review.find('div', {'class': 'hours'}).text.split(' ')[0]
        #link = nick.find('a').attrs['href']
        #comment = review.find('div', {'class': 'apphub_CardTextContent'}).text
        #print(nick.text, title, hour, link, )
        #print(comment.split('\n')[3].strip('\t'))
'''