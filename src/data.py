
class Data():

    def get_sensors(self, api, endpoint="data/{0}/sensors"):
        endpoint=endpoint.format(self.thing_obj["id"])
        data={"thingId":self.thing_obj["id"], }
        self.sensors.extend([Sensor(sensor) for sensor in api._api_request(endpoint, headers=api.headers, data=data)['result']])
        return self.sensors

    def get_sensor(self, type, api, endpoint='data/{0}/sensor'):
        endpoint=endpoint.format(self.thing_obj["id"])
        data={"thingId":self.thing_obj["id"], 'type':type}
        self._get_sensor=api._api_request(endpoint, headers=api.headers, data=data)
        return self._get_sensor

    # def make_anonymous_raw(self, base64, api, endpoint="data/anonymous/raw", verb="post"):
    #     data={"base64":base64}
    #     self.anonymous_raw_state=api._api_request(endpoint, headers=api.headers, data=data, verb=verb)
    #     return self.anonymous_raw_state
    #
    # def make_raw_noscript(self, base64, api, endpoint="data/raw/noscript", verb="post"):
    #     data={"base64":base64}
    #     self.raw_noscript_state=api._api_request(endpoint, headers=api.headers, data=data, verb=verb)
    #     return self.raw_noscript_state
    #
    # def make_anonymous_cbor(self, base64, api, endpoint="data/anonymous/cbor", verb="post"):
    #     data={"base64":base64}
    #     self.anonymous_cbor_state=api._api_request(endpoint, headers=api.headers, data=data, verb=verb)
    #     return self.anonymous_cbor_state
    #
    # def make_anonymous_cbor_noscript(self, base64, api, endpoint="data/anonymous/cbor/noscript", verb="post"):
    #     data={"base64":base64}
    #     self.anonymous_cbor_noscript_state=api._api_request(endpoint, headers=api.headers, data=data, verb=verb)
    #     return self.anonymous_cbor_noscript_state
    #
    # def make_anonymous_json(self, json, api, endpoint="data/anonymous/json", verb="post"):
    #     data={"json":json}
    #     self.anonymous_json_state=api._api_request(endpoint, headers=api.headers, data=data, verb=verb )
    #     return self.anonymous_json_state
    #
    # def make_anonymous_json_noscript(self, json, api, endpoint="data/anonymous/json/noscript", verb="post"):
    #     data={"json": json}
    #     self.anonymous_json_noscript_state= api._api_request(endpoint, headers= api.headers, data=data, verb=verb)
    #     return self.anonymous_json_noscript_state
