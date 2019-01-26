# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 12:12:28 2018

@author: Haosong
"""

'''
This script is for testing whether I can create a table, write data, and query the oracle sql db 
to get the data out 
'''
import spark
import pymysql.cursors

#connect to database
dbServerName = "127.0.0.1"
dbUser = "root"
dbPassword = "L314h15926s"
dbName = "django_blog"
connection = pymysql.connect(host=dbServerName,
                            user=dbUser,
                            password=dbPassword,
                            db=dbName,
                            charset='utf8',
                            port=3306
                            )
try:
    with connection.cursor() as cursor:
        #create a new record
        #sql="INSERT INTO h1n1_reviews VALUES (%s,%s,'%s','%s',%s,%s,%s,%s);"
        data=(2,2,1,20,1,2,0,0)
        insert_data="INSERT INTO h1n1_reviews(ID,Lan,Comments,Hours,Attitude,NumProdOwn,Funny,Helpful) VALUES ({0},{1},{2},{3},{4},{5},{6},{7})".format(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7])
        
        cursor.execute(insert_data)
        
    #commmit changes
    connection.commit()
    
    with connection.cursor() as cursor:
        #Read a single record
        sql= "SELECT * FROM 'h1n1_reviews' WHERE 'ID'=%d"
        cursor.execute(sql,(2,))
        result=cursor.fetchone()
        print(result)
finally:
    connection.close()
