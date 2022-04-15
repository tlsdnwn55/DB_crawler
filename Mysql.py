#_*_ coding: utf-8 _*_

import csv
import pymysql
from random import randint



# MySQL Connection 연결
def db_insert():
    try:
        conn = pymysql.connect(host='localhost', user='root', password='root' , db='media_db', charset='UTF8')
        curs = conn.cursor() # connection 으로부터 cursor 생성
        f = open('banzz.csv', 'r')
        media = csv.reader(f)
        sql = "insert into media(video_title,video_time,video_hit,like_number,upload_time,video_link) values(%s,%s,%s,%s,%s,%s)"
        for te in media:
            title = te[0]
            time = te[1]
            hit = te[2].replace(',','')
            like = te[3].replace(',','')
            upload = te[4]
            link = te[5]
            curs.execute(sql,(title,time,hit,like,upload,link))
        #rows = curs.fetchall()
        conn.commit()
    finally:
        conn.close()

def db_insert2():
    try:
        conn = pymysql.connect(host='localhost', user='root', password='root' , db='media_db', charset='UTF8')
        curs = conn.cursor() # connection 으로부터 cursor 생성
        f = open('ad_list.csv','r')
        ad = csv.reader(f)
        sql = "insert into advertise(ad_brand,ad_name,ad_second,second_profit) values(%s,%s,%s,%s)"
        for i in ad:
            brand = i[0]
            name = i[1]
            second = i[2]
            profit = i[3]
            #print(brand,name,int(second),float(profit) )
            curs.execute(sql,(brand,name,int(second),float(profit)))
        conn.commit()
    finally:
        conn.close()

def db_update():
    try:
        conn = pymysql.connect(host='localhost', user='root', password='root' , db='media_db', charset='UTF8')
        curs = conn.cursor()
        sql = "update media set ad_id = %s where no = %s"
        for i in range(220):
            r = randint(1,49)
            print(r)
            curs.execute(sql,(r,i+2))
        conn.commit()
    finally:
        conn.close()

db_update()