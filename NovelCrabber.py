import Crabber
import Novel
from database import CFDatabaseController as dbc

novel_name = Crabber.get_novel_name()
chapter_num = Crabber.get_chapter_num()

for iterator in range(chapter_num):
    chapter_name, chapter_text = Crabber.get_chapter_content(iterator)
    novel = Novel.Novel(novel_name, chapter_name, iterator , chapter_text)
    dbc.CF_Set(novel) #新增內容
    print('第' + str(iterator) + '章新增成功')
    


'''
#Get method
docs = dbc.CF_Get(novel)
print('{}'.format(docs.to_dict()['content']))
'''