
class Script():
    def script_validation(self, param, code, api, endpoint="script/validate"):
        params={"param":param, "code":code}
        self._script_validation=api._api_request(endpoint, headers=api.headers, params=params)
        return self._script_validation

    def make_new_script(self, name, description, script, api, endpoint='script/new', verb='post'):
        data={'projectId': self.project_obj["id"], 'name':name, 'description':description, 'script':script}
        self._make_new_script=api._api_request(endpoint, headers=api.headers, data=data, verb=verb)
        return self._make_new_script
