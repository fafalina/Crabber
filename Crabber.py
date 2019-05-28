import inlp.convert.chinese as cv
import  requests
from bs4 import BeautifulSoup
import re
import os
import time

#取得小說名稱
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

#取得小說某章節內容
def get_chapter_content(sub_chapter):
    #請求當前章節頁面  params為請求引數
    r = requests.get(req_url + chapter_url[sub_chapter], params=req_header) 
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

#取得小說所有章節的網址檔案名稱
def get_all_chapter_url():
    all_chapter_url = []
    #請求當前章節頁面  params為請求引數
    r = requests.get(req_url, params=req_header)
    #soup轉換
    soup=BeautifulSoup(r.text, "html.parser")
    #找到此小說的所有章節網址
    sub_page = soup.find_all(href=re.compile("/book/" + req_url_page))
    for tag in sub_page:
        sub_url = re.split(r'/', tag.get('href'))
        all_chapter_url.append(sub_url[3])
        
    return all_chapter_url

def get_chapter_num():
    return len(chapter_url)

#模擬瀏覽器
req_header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"
}

req_url_base = 'http://www.qu.la/book/'             #小說網站
req_url_page = "3137/"                              #小說位址
req_url = req_url_base + req_url_page               #單獨一本小說地址
chapter_url = get_all_chapter_url()                 #小說所有頁面地址
