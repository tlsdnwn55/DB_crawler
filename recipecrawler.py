#_*_ coding: utf-8 _*_

from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
from urllib.error import HTTPError
import re
import time
import csv




temp_list = []
def Crawling(target_page):
    r = requests.get(target_page)
    soup2 = BeautifulSoup(r.text,"html.parser")
    try:
        h3 = soup2.find('h3').get_text()
    except AttributeError:
        h3 = "삭제요망"
    try:
        info1 = soup2.find('span',{'class' : 'view2_summary_info1'}).get_text().strip('\n').strip(' ')
    except AttributeError:
        info1 = "재량"
    try:
        info2 = soup2.find('span', {'class': 'view2_summary_info2'}).get_text().strip('이내').strip('\n').strip(' ')
    except AttributeError:
        info2 = "재량"
    try:
        info3 = soup2.find('span', {'class': 'view2_summary_info3'}).get_text().strip('\n').strip(' ')
    except AttributeError:
        info3 = "재량"
    #ingre = soup2.find('div',{'class':'ready_ingre3'}).find_all('li')[0].get_text().strip('\n')
    #print(h3,info1,info2,info3,target_page)
    n = 0
    ingre_str = []
    for i in range(1,10):
        try:
            ingre = soup2.find('div', {'class': 'ready_ingre3'}).find_all('ul')[0].find_all('li')[n].get_text().replace("\n","").replace(" ","")
            ingre_str.append(ingre)
            ingre2 = soup2.find('div', {'class': 'ready_ingre3'}).find_all('ul')[1].find_all('li')[n].get_text().replace("\n","").replace(" ","")
            ingre_str.append(ingre2)
            n += 1
        except AttributeError:
            continue
        except IndexError:
            break
    ingredient = " ".join(ingre_str)
    temp_list.append([h3,info1,info2,info3,ingredient,target_page])
    print(temp_list)







def Call_Crawler():
    year = 2010
    page = 1
    while True:
        if page < 10:
            print(str(year) + "년" + str(page) + "월\n")
            url = 'http://www.10000recipe.com/ranking/list.html?type=best&year='+str(year)+'&month=0'+str(page)
            page += 1
        elif page < 13:
            print(str(year) + "년" + str(page) + "월\n")
            url = 'http://www.10000recipe.com/ranking/list.html?type=best&year=' + str(year) + '&month=' + str(page)
            page += 1
        else :
            page = 1
            year += 1
            continue
        if year > 2018:
            with open('test.csv', 'a', newline='', encoding="utf8") as f:
                writer = csv.writer(f)
                #writer.writerow(["Title", "For_person", "Cooking_time", "Difficulty", "Ingredient", "Link"])
                for row in temp_list:
                    writer.writerow(row)
            break
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        row = soup.find_all('div',{'class':'media-body'})

        for li in row:
            try:
                target_page = 'http://www.10000recipe.com'+ li.find('a',{'href' :True})['href']
                Crawling(target_page)
                #writer.writerow(list)
            except TypeError:
                print("링크없음\n")



Call_Crawler()
#title = soup.find('h3').get_text()
#ingredient = soup.find_all('')

