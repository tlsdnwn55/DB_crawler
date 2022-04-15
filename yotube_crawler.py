#_*_ coding: utf-8 _*_



from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

def get_playlist_info(playlist_link,playlist_title):
    link_list = []
    temp_list = []
    response = requests.get(playlist_link)
    soup = BeautifulSoup(response.text, "lxml")
    lis = soup.find_all('tr', {'class': 'pl-video yt-uix-tile'})
    cnt = 1
    for li in lis:
        try:
            video_link = 'https://www.youtube.com' + li.find('a', {'href': True})['href'].replace("\n","").replace(" ","")
            cnt += 1
            link_list.append(video_link)
            if cnt > 10 :
                for link in link_list:
                    temp_list.append(get_video_info(playlist_title, link))
                break
        except AttributeError:
            return ['삭제','삭제','삭제','삭제','삭제','삭제','삭제']
    if cnt < 5:
        return
    return temp_list


def get_video_info(playlist_title,link):
    response = requests.get(link)
    soup2 = BeautifulSoup(response.text, "html.parser")
    try:
        video_title = soup2.find('h1', {'class': 'watch-title-container'}).get_text().replace("\n","")
    except AttributeError:
        return ['삭제','삭제','삭제','삭제','삭제','삭제','삭제']
    hit = soup2.find('div', {'class': 'watch-view-count'}).get_text().strip('조회수').strip('회')
    video_time = soup2.find('span',{'class':'video-time'}).get_text()
    number_of_like = soup2.find_all('span', {'class': 'yt-uix-button-content'})[18].get_text()
    upload_time = soup2.find_all('strong')[3].get_text().strip('게시일:').strip(' ')
    temp = [playlist_title,video_title,video_time,hit,number_of_like,upload_time,link]
    return temp


def get_playlist():
    driver = webdriver.Chrome('C:/chromedriver_win32/chromedriver.exe')
    driver.get('https://www.youtube.com/channel/UC5W3wHMAkp6b_8HrhReP5aQ/playlists')
    time.sleep(1.5)

    body = driver.find_element_by_tag_name("body")
    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")
    find = soup.find_all('ytd-grid-playlist-renderer')
    # csv 파일 쓰기 준비
    with open('test.csv', 'w', newline='', encoding="utf8") as f:
        writer = csv.writer(f)
        writer.writerow(["playList_title"])
        for li in find:
            playlist_title = li.find('h3', {'class': True}).get_text().replace(" ", "").replace("\n", "")

def crawler_start():
    driver = webdriver.Chrome('C:/chromedriver_win32/chromedriver.exe')
    driver.get('https://www.youtube.com/channel/UC5W3wHMAkp6b_8HrhReP5aQ/playlists')
    time.sleep(1.5)

    body = driver.find_element_by_tag_name("body")
    html = driver.page_source
    soup = BeautifulSoup(html,"lxml")
    find = soup.find_all('ytd-grid-playlist-renderer')

    # csv 파일 쓰기 준비
    with open('test.csv', 'w', newline='', encoding="utf8") as f:
        writer = csv.writer(f)
        writer.writerow(["PlayList_Title", "Video_Title", "Video_Time", "Video_Hit", "Number_Of_Like", "Upload_Time","Video_Link"])
        for li in find:
            playlist_title = li.find('h3', {'class': True}).get_text().replace(" ","").replace("\n","")
            playlist_link = 'https://www.youtube.com' + li.find('a', {'class' : 'yt-simple-endpoint style-scope yt-formatted-string'})['href']
            temp = get_playlist_info(playlist_link,playlist_title)
            print(temp)
            try:
                for row in temp:
                    writer.writerow(row)
            except TypeError:
                continue

    driver.close()

crawler_start()