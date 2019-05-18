import  requests
import threading
from bs4 import BeautifulSoup
import re
import os
import time

#模擬瀏覽器
req_header={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"
}

req_url_base='http://www.qu.la/book/'           #小說主地址
req_url=req_url_base + "3137/"                       #單獨一本小說地址
txt_section='10542714.html'                       #某一章頁面地址
#請求當前章節頁面  params為請求引數
r=requests.get(req_url + txt_section,params=req_header) 
#soup轉換
soup=BeautifulSoup(r.text,"html.parser")
#獲取章節名稱                                    
section_name=soup.select('#wrapper .content_read .box_con .bookname h1')[0]
pattern = re.compile(r'<(/*)h1>') #移除<h1> & </h1>
section_name=re.sub(pattern,"", str(section_name))
print(section_name)
#獲取章節內容
section_text = soup.select('#wrapper .content_read .box_con #content')[0]
#刪去內容不必要的東西
section_text = re.sub(r'<br/>','\n\n', str(section_text))
section_text = re.sub(r'<(/*)div>','', str(section_text))
print(str(section_text))






