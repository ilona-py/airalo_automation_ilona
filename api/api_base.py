import requests
from source_shop import ApiLinks


class ApiManager(object):
    headers = {'Content-Type': 'application/json'}
    token = ''

    @staticmethod
    def get_oauth2_token():
        response = requests.post(url=ApiLinks.token_url, data={
            "grant_type": "client_credentials",
            "client_id": ApiLinks.client_id,
            "client_secret": ApiLinks.client_secret
        })
        assert response.ok
        token_info = response.json()
        return token_info['data']['access_token']

    def login(self):
        self.token = self.get_oauth2_token()
        ApiManager.headers['Authorization'] = f'Bearer {self.token}'
        return self.token

    @staticmethod
    def post(url, body=None, header=None, data=None):
        if header is None:
            header = ApiManager.headers
        result = requests.post(url,
                               json=body,
                               headers=header,
                               data=data)
        return result

    @staticmethod
    def get(url):
        result = requests.get(url,
                              headers=ApiManager.headers
                              )
        return result
