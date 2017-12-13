class ThingCaptcha():

    def captcha_generate_modification(self, api, endpoint="captcha/generate/thing/modification"):
        params={"thingId":self.thing_obj["id"], }
        self._captcha_generate_modification=api._api_request(endpoint, headers=api.headers, params=params)
        return self._captcha_generate_modification

    def captcha_generate_deletation(self, api, endpoint="captcha/generate/thing/deletion"):
        params={"thingId":self.thing_obj["id"], }
        self._captcha_generate_deletation=api._api_request(endpoint, headers=api.headers, params=params)
        return self._captcha_generate_deletation
