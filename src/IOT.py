import requests
import json

class Api():

    def __new__(cls, *args):
        if not hasattr(cls, "_instance"):
            cls._instance=object.__new__(cls)
        return cls._instance

    def __init__(self,  username=None, password=None, host="http://172.16.100.243//api/v1/"):
        self.username = username
        self.password = password
        self.host = host
        self.login()

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
        return self.access_token, self.headers

class Person(object):

    def __init__(self, username, password):
        self.projects=[]
        self.api=Api(username, password)

    def get_projects(self, endpoint="project/list"):
        self.projects.extend([Project(proj) for proj in self.api._api_request(endpoint, headers=self.api.headers)])
        return self.projects

class Project():
    def __init__(self, project_obj):
        self.project_obj=project_obj
        self.things=[]

    def get_project_info(self, api, endpoint="project/{0}/info"):
        endpoint=endpoint.format(self.project_obj["id"])
        self.info=api._api_request(endpoint, headers=api.headers)
        return self.info

    def get_things(self, api, endpoint="project/{0}/things"):
        endpoint=endpoint.format(self.project_obj["id"])
        self.things.extend([Thing(thing) for thing in  api._api_request(endpoint, headers=api.headers)])
        return self.things

    def get_permission(self, api, endpoint="project/{0}/permission"):
        endpoint=endpoint.format(self.project_obj["id"])
        self.permission= api._api_request(endpoint, headers=api.headers)
        return self.permission

class Thing():
    def __init__(self, thing_obj):
        self.thing_obj=thing_obj
        self.sensors=[]

    def get_sensors(self, api, endpoint="thing/{0}/sensors"):
        endpoint=endpoint.format(self.thing_obj["id"])
        self.sensors.extend([Sensor(sensor) for sensor in api._api_request(endpoint, headers=api.headers)])
        return self.sensors

class Sensor():
    def __init__(self, sensor_obj):
        self.sensor_obj=sensor_obj


if __name__=="__main__":

    ali=Person("ali@parto.com", "1qaz@WSX")
    connection=ali.api

    print(ali.api.headers)
    print(ali.api.access_token)
    print(ali.api.host)

    ali.get_projects()
    print(ali.projects)
    print(ali.projects[0])
    print(ali.projects[0].things)
    print(ali.projects[0].project_obj)
    print(ali.projects[0].project_obj["id"])

    ali.projects[0].get_project_info(connection)
    print(ali.projects[0].info)

    ali.projects[0].get_permission(connection)
    print(ali.projects[0].permission)

    ali.projects[0].get_things(connection)
    print(ali.projects[0].things)
    print(ali.projects[0].things[0])
    print(ali.projects[0].things[0].thing_obj)
    print(ali.projects[0].things[0].thing_obj["id"])
    print(ali.projects[0].things[0].sensors)

    ali.projects[0].things[0].get_sensors(connection)
    print(ali.projects[0].things[0].sensors)
    print(ali.projects[0].things[0].sensors[0].sensor_obj)
