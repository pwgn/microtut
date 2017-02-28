import time

class Comments():

    def __init__(self):
        self.threads = {}

    def add(self, thread_id, data):
        message_id = str(time.time()).replace('.', '')
        message = {
            'id': message_id,
            'message': data['message']
        }

        if self.threads.haskey(thread_id):
            self.threads[thread_id].append(message)
        else:
            self.threads[thread_id] = [message]

        return message

    def get(self, article_id):
        pass

    def list(self):
        pass
