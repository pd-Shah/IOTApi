class ThingCaptcha():

    def captcha_generate_modification(self, api, endpoint="captcha/generate/thing/modification"):
        data={"thingId":self.thing_obj["id"], }
        self._captcha_generate_modification=api._api_request(endpoint, headers=api.headers, data=data)
        return self._captcha_generate_modification

    def captcha_generate_deletation(self, api, endpoint="captcha/generate/thing/deletion"):
        data={"thingId":self.thing_obj["id"], }
        self._captcha_generate_deletation=api._api_request(endpoint, headers=api.headers, data=data)
        return self._captcha_generate_deletation
