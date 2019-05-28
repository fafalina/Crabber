class Novel:
    data = {
        "chapter_id" : None,
        "content" : ""
    }
    def __init__(self, novel_name, chapter_name, chapter_id, content):
        self.novel_name = novel_name
        self.chapter_name = chapter_name
        self.chapter_id = chapter_id
        self.content = chapter_name + '\n' + content

    def data_to_dict(self):
        self.data = {
            "chapter_id" : self.chapter_id,
            "content" : self.content
        }
        return self
        
    def get_data(self):
        return self.data
