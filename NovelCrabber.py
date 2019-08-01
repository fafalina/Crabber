import Crabber
import Novel
from database import CFDatabaseController as dbc

novel_name = Crabber.get_novel_name()
author_name = Crabber.get_novel_author()
chapter_num = Crabber.get_chapter_num()

for iterator in range(chapter_num):
    chapter_name, chapter_text = Crabber.get_chapter_content(iterator)
    novel = Novel.Novel(novel_name, author_name, chapter_name, iterator , chapter_text)
    dbc.CF_set_content(novel) #新增章節ID和章節內容
    print('第' + str(iterator) + '章新增成功')
    
dbc.CF_set_information(novel) #最後新增一些資訊


'''
#Get method
docs = dbc.CF_get_content(novel)
print('{}'.format(docs.to_dict()['content']))
'''