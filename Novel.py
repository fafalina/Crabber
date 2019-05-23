class Novel:
    data = {
        "chapter_name" : "",
        "content" : ""
    }
    def __init__(self, novel_name, chapter_id, chapter_name = "", content = ""):
        self.novel_name = novel_name
        self.chapter_id = chapter_id
        self.chapter_name = chapter_name
        self.content = content

    def data_to_dict(self):
        self.data = {
            "chapter_name" : self.chapter_name,
            "content" : self.content
        }
        return self
        
    def get_data(self):
        return self.data
