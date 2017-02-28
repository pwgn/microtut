import time

class Articles():

    def __init__(self):
        self.articles = {}

    def add(self, article_data):
        article_id = str(time.time()).replace('.', '')
        article = {
            'id': article_id,
            'title': article_data['title'],
            'content': article_data['content']
        }
        self.articles[article_id] = article
        return article

    def get(self, article_id):
        return self.articles[article_id]

    def list(self):
        def exclude_content(d):
            return {key: value for key, value in d.items() if key != 'content'}
        return {k: exclude_content(v) for k, v in self.articles.items()}
