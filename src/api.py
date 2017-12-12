import requests

class Api():

    # def __new__(cls, *args):
    #     if not hasattr(cls, "_instance"):
    #         cls._instance=object.__new__(cls)
    #     return cls._instance

    def __init__(self,  username=None, password=None, host="http://172.16.100.243/api/v1/"):
        self.username = username
        self.password = password
        self.host = host

    def _api_request(self, endpoint, verb='get', json=None, headers=None, data=None):
        response = getattr(requests, verb)(self.host + endpoint, json=json, headers=headers, data= data)
        print('{} {}'.format(response.status_code, response.reason))
        data = response.json()
        print(data)
        if isinstance(data, dict):
            messages = data.pop("messages", None)
            if messages:
                print(json.dumps(messages, indent=4))
        try:
            response.raise_for_status()
        except Exception as e:
            print(e)
            return None
        else:
            return data

    def login(self, endpoint="user/login", verb="post"):
        data={"username": self.username, "password": self.password}
        self.access_token=self._api_request(endpoint, data=data, verb=verb)["result"]["accessToken"]
        self.headers={"Authorization":"Bearer " + self.access_token}
        return self.access_token, self.headers

    def signup(self, endpoint="user/signup", verb="post"):
        data={"username": self.username, "password": self.password}
        self._signup=self._api_request(endpoint, data=data, verb=verb)
        return self._signup

    def renew(self, endpoint="user/renew"):
        self._renew=self._api_request(endpoint, headers=self.headers)
        return self._renew
