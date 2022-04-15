#_*_ coding: utf-8 _*_

from bs4 import BeautifulSoup
import requests
import csv


def get_ad_list():
    url = 'https://www.thinkwithgoogle.com/intl/ko-kr/advertising-channels/video/youtube-leaderboard-q2-2018/'
    res = requests.get(url)
    soup = BeautifulSoup(res.text,"lxml")
    adlist = []
    lis = soup.find_all('div',{'class':'card__body'})
    for li in lis:
        try:
            title = li.find('span',{'class':'cjk-title-wrap-ko-kr'}).get_text()
            brand = li.find('span',{'class':'card__meta-value'}).get_text()
        except AttributeError:
            continue
        adlist.append([brand,title])
    return adlist



if __name__ == '__main__':
    list = []
    list = get_ad_list()
    with open('ad_list.csv','a',encoding='utf-8') as f:
        writer = csv.writer(f)
        #writer.writerow(["brand","ad_name"])
        for row in list:
            writer.writerow(row)