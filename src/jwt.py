class JWT():

    def jwt(self, api, endpoint='interface/jwt/{0}'):
        endpoint=endpoint.format(self.thing_obj['result']["id"])
        self._jwt=api._api_request(endpoint, headers=api.headers, )
        return self._jwt

    def get_jwt_enable(self, api, endpoint="interface/jwt/{0}/enable"):
        endpoint=endpoint.format(self.thing_obj['result']["id"])
        self._get_jwt_enable=api._api_request(endpoint, headers=api.headers, )
        return self._get_jwt_enable

    def set_jwt_enable(self, enable, api, endpoint="interface/jwt/{0}/enable", verb="put"):
        endpoint=endpoint.format(self.thing_obj['result']["id"])
        data={"enable":enable}
        self._set_jwt_enable=api._api_request(endpoint, headers=api.headers, verb=verb, data=data)
        return self._set_jwt_enable

    def get_jwt_settings(self, api, endpoint="interface/jwt/{0}/settings"):
        endpoint=endpoint.format(self.thing_obj['result']["id"])
        self._get_jwt_settings=api._api_request(endpoint, headers=api.headers)
        return self._get_jwt_settings

    def set_jwt_settings(self, key, audience, issuer, description, api, endpoint="interface/jwt/{0}/settings", verb="put"):
        endpoint=endpoint.format(self.thing_obj['result']["id"])
        data={"key":key, "audience":audience, "issuer":issuer, "description":description}
        self._set_jwt_settings=api._api_request(endpoint, headers=api.headers, verb=verb, data=data)
        return self._set_jwt_settings

    def get_jwt_generate(self, seconds, api, endpoint='interface/jwt/{0}/generate'):
        endpoint=endpoint.format(self.thing_obj['result']["id"])
        params={"seconds": 10000, }
        self._get_jwt_generate=api._api_request(endpoint, headers=api.headers, params=params)
        return self._get_jwt_generate
