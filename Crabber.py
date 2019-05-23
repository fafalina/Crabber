import inlp.convert.chinese as cv
import  requests
from bs4 import BeautifulSoup
import re
import os
import time

def get_novel_name():
    #請求當前章節頁面  params為請求引數
    r = requests.get(req_url, params=req_header) 
    #soup轉換
    soup=BeautifulSoup(r.text, "html.parser")
    #以selcetor獲取章節名稱 
    novel_name = soup.select('#info h1')[0]
    #刪去不必要的東西
    pattern = re.compile(r'<(/*)h1>') #移除<h1> & </h1>
    novel_name = re.sub(pattern, "", str(novel_name))
    #簡中轉繁中
    novel_name = cv.s2t(novel_name)

    return novel_name

def get_chapter_content():
    #請求當前章節頁面  params為請求引數
    r = requests.get(req_url + txt_chapter, params=req_header) 
    #soup轉換
    soup=BeautifulSoup(r.text, "html.parser")
    #以selcetor獲取章節名稱                                    
    chapter_name = soup.select('#wrapper .content_read .box_con .bookname h1')[0]
    pattern = re.compile(r'<(/*)h1>') #移除<h1> & </h1>
    chapter_name = re.sub(pattern, "", str(chapter_name))
    #獲取章節內容
    chapter_text = soup.select('#wrapper .content_read .box_con #content')[0]
    #刪去內容不必要的東西
    chapter_text = re.sub(r'<br/>', '\n\n', str(chapter_text)) #移除html的換行符號<br/>
    chapter_text = re.sub(r'<div id="content">', '', str(chapter_text)) #移除此段<div id="content">
    chapter_text = re.sub(r'<(/*)div>', '', str(chapter_text)) #移除<div> & </div>
    #簡中轉繁中
    chapter_name = cv.s2t(chapter_name)
    chapter_text = cv.s2t(chapter_text)

    return chapter_name, chapter_text

#模擬瀏覽器
req_header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"
}

#TODO 自動取得頁面網址
req_url_base = 'http://www.qu.la/book/'             #小說主地址
req_url = req_url_base + "3137/"                    #單獨一本小說地址
txt_chapter = '10542714.html'                       #某一章頁面地址 #list > dl > dd:nth-child(17) > a

