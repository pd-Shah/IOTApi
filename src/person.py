from api import Api
from project import Project

class Person():

    def __init__(self, username, password):
        self.projects=[]
        self.api=Api(username, password)

    def get_projects(self, page_number, page_size, endpoint="project/list"):
        params={"pageNumber":page_number, "pageSize":page_size}
        self.projects.extend([Project(proj) for proj in self.api._api_request(endpoint, headers=self.api.headers, params=params)['result']])
        return self.projects

    def make_new_project(self, project_name, project_description, endpoint="project/new", verb="post"):
        data={"name": project_name, "description":project_description}
        self.projects.append(Project(self.api._api_request(endpoint, verb=verb, data=data, headers=self.api.headers)))
        return self.projects[-1]
