class MQTT():
    pass
    # def check_mqtt(self, api, endpoint="interface/{0}/mqtt/enable"):
    #     endpoint=endpoint.format(self.thing_obj['result']["id"])
    #     self.mqtt=api._api_request(endpoint, headers=api.headers)
    #     return self.mqtt_state
    #
    # def update_mqtt(self, enable, api, endpoint="interface/{0}/mqtt/enable", verb="put"):
    #     endpoint=endpoint.format(self.thing_obj['result']["id"])
    #     data={"enable": enable, "thingId": self.thing_obj['result']["id"]}
    #     self.update_mqtt_state=api._api_request(endpoint, headers=api.headers, data=data, verb=verb)
    #     return self.update_mqtt_state
    #
    # def get_mqtt_sub(self, api, endpoint="interface/{0}/mqtt/sub"):
    #     endpoint=endpoint.format(self.thing_obj['result']["id"])
    #     self.get_mqtt_sub_state=api._api_request(endpoint, headers=api.headers)
    #     return self.get_mqtt_sub_state
    #
    # def update_mqtt_sub(self, enable, api, endpoint="interface/{0}/mqtt/sub", verb="put"):
    #     endpoint=endpoint.format(self.thing_obj['result']["id"])
    #     data={"enable":enable, "thingId": self.thing_obj['result']["id"]}
    #     self.update_mqtt_sub_state=api._api_request(endpoint, headers=api.headers, verb=verb, data=data)
    #     return self.update_mqtt_sub_state
    #
    # def get_mqtt_pub(self, api, endpoint="interface/{0}/mqtt/pub"):
    #     endpoint=endpoint.format(self.thing_obj['result']["id"])
    #     self.mqtt_pub_state=api._api_request(endpoint, headers=api.headers)
    #     return self.mqtt_pub_state
    #
    # def update_mqtt_pub(self, enable, api, endpoint="interface/{0}/mqtt/pub", verb="put"):
    #     data={"thingId":self.thing_obj['result']["id"], "enable":enable}
    #     endpoint=endpoint.format(self.thing_obj['result']["id"])
    #     self.update_mqtt_pub_state=api._api_request(endpoint, headers=api.headers, verb=verb, data=data)
    #     return self.update_mqtt_pub_state
