import time

class Articles():

    def __init__(self):
        self.articles = {}

    def addArticle(self, title, content):
        article_id = str(time.time())
        self.articles[article_id] = {
            'id': article_id,
            'title': title,
            'content': content
        }

    def getArticle(self, article_id):
        return self.articles[article_id]

    def listArticles(self):
        return {}
