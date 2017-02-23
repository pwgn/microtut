
class Registry():

    def __init__(self):
        self.services = {}

    def get_service(self, service_id):
        return self.services[service_id]

    def list_services(self):
        return self.services

    def register_service(self, service_id, service):
        self.services[service_id] = service

    def deregister_service(self, service_id):
        self.services.pop(service_id)
