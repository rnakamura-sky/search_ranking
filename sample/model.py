class Keyword:
    def __init__(self):
        self.id = None
        self.text = ''
        self.delete = 0
    
    def __str__(self):
        return f'Keyword({self.id}, {self.text}, {self.delete})'

class Statistics:
    def __init__(self, keyword):
        self.date = None
        self.keyword = keyword
        self.rank = -1
        self.page = -1
        self.rank_in_page = -1
    
    def __str__(self):
        return f'Statistics({self.date},)'