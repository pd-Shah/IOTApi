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
        self.headers={"Authorization":"Bearer " + self.access_token}
        return self.access_token

    def get_projects(self, endpoint="project/my"):
        self.projects=self._api_request(endpoint, headers=self.headers)
        return self.projects

    def get_things(self, project_id, endpoint="project/get/project/{0}/things"):
        endpoint=endpoint.format(project_id)
        self.things= self._api_request(endpoint, headers=self.headers)
        return self.things

    def get_sensors(self, thing_id, endpoint="project/get/thing/{0}/sensors"):
        endpoint=endpoint.format(thing_id)
        self.sensors=self._api_request(endpoint, headers=self.headers)
        return self.sensors

if __name__=="__main__":

    ali=Api("ali@parto.com", "1qaz@WSX", )

    ali.login()
    print(ali.access_token)

    ali.get_projects()
    print(ali.projects)

    ali.get_things(ali.projects[0]["id"])
    print(ali.things)

    ali.get_sensors(ali.things[1]["id"])
    print(ali.sensors)
