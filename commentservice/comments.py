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

        if thread_id in self.threads:
            self.threads[thread_id].append(message)
        else:
            self.threads[thread_id] = [message]

        return message

    def get_thread(self, thread_id):
        thread = []
        if thread_id in self.threads:
            thread = self.threads[thread_id]

        return thread
