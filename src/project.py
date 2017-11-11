
from project_captcha import ProjectCaptcha
from script import Script
from thing import Thing

class Project(ProjectCaptcha, Script):

    def __init__(self, project_obj):
        self.project_obj=project_obj
        self.things=[]

    def get_info(self, api, endpoint="project/{0}/info"):
        endpoint=endpoint.format(self.project_obj["id"])
        self._get_info=api._api_request(endpoint, headers=api.headers)
        return self._get_info

    def update_info(self, new_name, new_description, api, endpoint="project/{0}/info", verb="put"):
        endpoint=endpoint.format(self.project_obj["id"])
        data={"name": new_name, "description": new_description}
        self._update_info=api._api_request(endpoint, headers=api.headers, verb=verb, data=data)
        return self._update_info

    def get_things(self, page_number, page_size, api, endpoint="project/{0}/things"):
        endpoint=endpoint.format(self.project_obj["id"])
        data={"pageNumber":page_number, "pageSize":page_size, "projectId": self.project_obj["id"]}
        self.things.extend([Thing(thing) for thing in  api._api_request(endpoint, headers=api.headers, data=data)["result"]])
        return self.things

    # def delete(self, api, endpoint="project/{0}", verb="delete"):
    #     endpoint=endpoint.format(self.project_obj["id"])
    #     self._delete=api._api_request(endpoint, headers=api.headers, verb=verb)
    #     return self._delete

    # def update_project(self, new_name, new_description, api, endpoint="project/{0}", verb="put"):
    #     endpoint=endpoint.format(self.project_obj["id"])
    #     data={"name": new_name, "description":new_description}
    #     self.project_update_state=api._api_request(endpoint, headers=api.headers, verb=verb, data=data)
    #     return self.project_update_state

    # def get_permission(self, api, endpoint="project/{0}/permission"):
    #     endpoint=endpoint.format(self.project_obj["id"])
    #     self._get_permission= api._api_request(endpoint, headers=api.headers)
    #     return self._get_permission

    # def delete_permission(self, api, endpoint="project/{0}/permission", verb="delete"):
    #     endpoint=endpoint.format(self.project_obj["id"])
    #     self.delete_permission_state=api._api_request(endpoint, headers=api.headers, verb=verb)
    #     return self.delete_permission_state

    # def update_permission(self, api, endpoint="project/{0}/permission", verb="put"):
    #     endpoint=endpoint.format(self.project_obj["id"])
    #     self.update_permission_state=api._api_request(endpoint, headers=api.headers, verb=verb)
    #     return self.delete_permission_state

    # def get_users(self, page_number, page_size, api, endpoint="project/{0}/users"):
    #     endpoint=endpoint.format(self.project_obj["id"])
    #     data={"projectId": self.project_obj["id"], "pageNumber":page_number, "pageSize":page_size}
    #     self._get_users=api._api_request(endpoint, headers=api.headers, data=data)
    #     return self._get_users

    def make_new_thing(self, thing_name, description, api, endpoint="thing/new", verb="post"):
        data={"projectId": self.project_obj["id"], "name":thing_name, "description":description}
        self.things.append(Thing(api._api_request(endpoint, headers=api.headers, data=data, verb=verb)))
        return self.things[-1]

    def get_rule(self, api, endpoint="project/{0}/rule"):
        endpoint=endpoint.format(self.project_obj["id"])
        data={"projectId": self.project_obj["id"]}
        self._get_rule= api._api_request(endpoint, headers=api.headers, data=data)
        return self._get_rule

    def new_rule(self, is_enabled, interval, trigger, script, api, endpoint="project/{0}/rule", verb="put"):
        endpoint=endpoint.format(self.project_obj["id"])
        data={"isEnabled":is_enabled, "interval":interval, "trigger":trigger, "script":script}
        self._new_rule= api._api_request(endpoint, headers=api.headers, data=data, verb=verb)
        return self._new_rule

    def set_rule_enable(self, value, api, endpoint="project/{0}/rule/enable", verb="put"):
        endpoint=endpoint.format(self.project_obj["id"])
        data={"value":value, "projectId": self.project_obj["id"]}
        self._set_rule_enable= api._api_request(endpoint, headers=api.headers, data=data, verb=verb)
        return self._set_rule_enable

    def set_rule_interval(self, value, api, endpoint="project/{0}/rule/interval", verb="put"):
        endpoint=endpoint.format(self.project_obj["id"])
        data={"projectId": self.project_obj["id"], "value":value}
        self._set_rule_interval= api._api_request(endpoint, headers=api.headers, data=data, verb=verb)
        return self._set_rule_interval

    def set_rule_trigger(self, value, api, endpoint="project/{0}/rule/trigger", verb="put"):
        endpoint=endpoint.format(self.project_obj["id"])
        data={"projectId": self.project_obj["id"], "value":value}
        self._set_rule_trigger= api._api_request(endpoint, headers=api.headers, data=data, verb=verb)
        return self._set_rule_trigger

    def set_rule_script(self, value, api, endpoint="project/{0}/rule/script", verb="put"):
        endpoint=endpoint.format(self.project_obj["id"])
        data={"projectId": self.project_obj["id"], "value":value}
        self._set_rule_script=api._api_request(endpoint, headers=api.headers, data=data, verb=verb)
        return self._set_rule_script