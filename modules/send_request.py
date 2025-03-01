import requests

def send_request(method, url, headers):
    try:
        res = requests.request(method, url, headers=headers)
        if res.status_code == 200:
            response = res.json()
            if 'message' in response:
                if response['message'] == 'Not Found':
                    raise ValueError(f'Wrong response from {url} - Status: {response['status']} - Message: {response['message']}')
            else:
                return response
    except ValueError as e:
        raise e