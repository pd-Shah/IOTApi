import requests
import json

class Api(object):

    def __init__(self, username, password, host="http://172.16.100.243/api/v1/"):
        self.host = host
        self.username = username
        self.password = password

    def _api_request(self, endpoint, verb='get', body=None, headers=None, data=None):
        response = getattr(requests, verb)(self.host + endpoint, json=body, headers=headers, data= data)
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
        self.access_token=self._api_request(endpoint, verb, data=data)["accessToken"]
        return self.access_token

    def get_projects(self, endpoint="project/my"):
        headers={"Authorization":"Bearer " + self.access_token}
        self.projects=self._api_request(endpoint, headers=headers)
        return self.projects

    def get_things(self, project_id, endpoint="project/get/project/{0}/things"):
        endpoint=endpoint.format(project_id)
        headers={"Authorization":"Bearer " + self.access_token}
        self.things= self._api_request(endpoint, headers=headers)
        return self.things




if __name__=="__main__":

    ali=Api("ali@parto.com", "1qaz@WSX", )

    ali.login()
    print(ali.access_token)

    ali.get_projects()
    print(ali.projects)

    ali.get_things(ali.projects[0]["id"])
    print(ali.things)
