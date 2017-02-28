import requests

def get_service_url(discovery_url, service_id, path):
    # Get the service from the service registry
    discoveryservice_url = 'http://' + '/'.join([discovery_url, service_id])
    discoveryservice_response = requests.get(discoveryservice_url)

    # Build the service url
    service = discoveryservice_response.json()
    service_url = service['host'] + ':' + str(service['port'])
    service_request_url = 'http://' + '/'.join([service_url, service_id, path])

    return service_request_url
