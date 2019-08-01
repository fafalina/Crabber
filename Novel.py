class Novel:
    chapter = {
        "chapter_id" : None,
        "content" : ""
    }

    information = {
        "athor_name" : ""
    }

    def __init__(self, novel_name, author_name, chapter_name, chapter_id, content):
        self.novel_name = novel_name
        self.author_name = author_name
        self.chapter_name = chapter_name
        self.chapter_id = chapter_id
        self.content = chapter_name + '\n' + content

    def chapter_to_dict(self):
        self.chapter = {
            "chapter_id" : self.chapter_id,
            "content" : self.content
        }
        return self

    def information_to_dict(self):    
        self.information = {
            "athor_name" : self.author_name
        }
        return self
    
    def get_chapter(self):
        return self.chapter

    def get_information(self):
        return self.information
