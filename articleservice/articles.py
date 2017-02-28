import time

class Articles():

    def __init__(self):
        self.articles = {}

    def add(self, title, content):
        article_id = str(time.time())
        self.articles[article_id] = {
            'id': article_id,
            'title': title,
            'content': content
        }

    def get(self, article_id):
        return self.articles[article_id]

    def list(self):
        def exclude_content(d):
            return {key: value for key, value in d.items() if key != 'content'}
        return {k: exclude_content(v) for k, v in self.articles.items()}
