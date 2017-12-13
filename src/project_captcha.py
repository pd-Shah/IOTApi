class ProjectCaptcha():

    def captcha_generate_deletation(self, api, endpoint="captcha/generate/project/deletion"):
        params={"projectId":self.project_obj["id"]}
        self._captcha_generate_deletation=api._api_request(endpoint, headers=api.headers, params=params)
        return self._captcha_generate_deletation

    def captcha_generate_modification(self, api, endpoint="captcha/generate/project/modification"):
        params={"projectId":self.project_obj["id"]}
        self._captcha_generate_modification=api._api_request(endpoint, headers=api.headers, params=params)
        return self._captcha_generate_modification
