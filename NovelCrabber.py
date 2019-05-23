import Crabber
import Novel
from database import CFDatabaseController as dbc

novel_name = Crabber.get_novel_name()

#TODO 做全部章節
iterator = 1 #章節計數器
chapter_name, chapter_text = Crabber.get_chapter_content()
novel = Novel.Novel(novel_name, iterator, chapter_name , chapter_text)
dbc.CF_Set(novel)