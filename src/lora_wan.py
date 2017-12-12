class LoRaWAN():

    def get_lorawan(self, api, endpoint="interface/lorawan/{0}"):
        endpoint=endpoint.format(self.thing_obj["id"])
        data={'thingId':self.thing_obj["id"], }
        self._get_lorawan=api._api_request(endpoint, headers=api.headers, data=data)
        return self._get_lorawan

    def set_lorawan(self, is_enable, is_otaa, dev_EUI, appSKey, nwkSKey, dev_addr, app_key, app_EUI, description, api, endpoint="interface/lorawan/{0}", verb="put"):
        endpoint=endpoint.format(self.thing_obj["id"])
        print(endpoint)
        json={'isEnable': is_enable,
        'isOtaa': is_otaa,
        'devEUI': dev_EUI,
        'abp': {'appSKey': appSKey, 'nwkSKey': nwkSKey, 'devAddr':dev_addr},
        'ota': {'appKey':  app_key, 'appEUI': app_EUI},
        'description': description }
        self._set_lorawan= api._api_request(endpoint, headers=api.headers, json=json, verb=verb)
        return self._set_lorawan

    def get_lorawan_enable(self, api, endpoint='interface/lorawan/{0}/enable'):
        endpoint=endpoint.format(self.thing_obj["id"])
        data={'thingId':self.thing_obj["id"], }
        self._get_lorawan_enable=api._api_request(endpoint, headers=api.headers, data= data)
        return self._get_lorawan_enable

    def set_lorawan_enable(self, enable, api, endpoint="interface/lorawan/{0}/enable", verb='put'):
        endpoint=endpoint.format(self.thing_obj["id"])
        data={'thingId':self.thing_obj["id"], 'enable':enable}
        self._set_lorawan_enable=api._api_request(endpoint, headers=api.headers, data=data, verb=verb)
        return self._set_lorawan_enable

    def get_lorawan_otaa(self, api, endpoint="interface/lorawan/{0}/otaa"):
        endpoint=endpoint.format(self.thing_obj["id"])
        data={'thingId':self.thing_obj["id"], }
        self._get_lorawan_otaa=api._api_request(endpoint, headers=api.headers, data=data)
        return self._get_lorawan_otaa

    def set_lorawan_otaa(self, app_key, app_EUI, api, endpoint="interface/lorawan/{0}/otaa", verb="put"):
        endpoint=endpoint.format(self.thing_obj["id"])
        data={"thingId":self.thing_obj["id"], "appkey":app_key, "appEUI":app_EUI, }
        self._set_lorawan_otaa=api._api_request(endpoint, headers=api.headers, data=data, verb=verb)
        return self._set_lorawan_otaa

    def get_lorawan_abp(self,api, endpoint="interface/lorawan/{0}/abp"):
        endpoint=endpoint.format(self.thing_obj["id"])
        data={"thingId":self.thing_obj["id"],}
        self._get_lorawan_abp=api._api_request(endpoint, headers=api.headers, data=data)
        return self._get_lorawan_abp

    def set_lora_abp(self, app_skey, nwk_skey, dev_addr, api, endpoint="interface/lorawan/{0}/abp", verb="put"):
        data={"thingId":self.thing_obj["id"], "appSkey":app_skey, "nwkSkey":nwk_skey, "devAddr":dev_addr}
        endpoint=endpoint.format(self.thing_obj["id"])
        self._set_lora_abp=api._api_request(endpoint, headers=api.headers, data=data, verb=verb)
        return self._set_lora_abp

    def get_lorawan_deveui(self, api, endpoint='interface/lorawan/{0}/deveui'):
        endpoint=endpoint.format(self.thing_obj["id"])
        data={"thingId":self.thing_obj["id"],}
        self._get_lorawan_deveui=api._api_request(endpoint, headers=api.headers, data=data)
        return self._get_lorawan_deveui

    def set_lorawan_deveui(self, dev_EUI, api, endpoint='interface/lorawan/{0}/deveui', verb='put'):
        endpoint=endpoint.format(self.thing_obj["id"])
        data={"thingId":self.thing_obj["id"], 'devEUI':dev_EUI, }
        self._set_lorawan_deveui=api._api_request(endpoint, headers=api.headers, data=data, verb=verb)
        return self._set_lorawan_deveui

    def get_lorawan_mode(self, api, endpoint='interface/lorawan/{0}/mode'):
        endpoint=endpoint.format(self.thing_obj["id"])
        data={"thingId":self.thing_obj["id"], }
        self._get_lorawan_mode= api._api_request(endpoint, headers=api.headers, data=data)
        return self._get_lorawan_mode

    def set_lorawan_mode(self, mode, api, endpoint='interface/lorawan/{0}/mode', verb='put'):
        endpoint=endpoint.format(self.thing_obj["id"])
        data={"thingId":self.thing_obj["id"], 'mode':mode}
        self._set_lorawan_mode= api._api_request(endpoint, headers=api.headers, data=data, verb=verb)
        return self._set_lorawan_mode

    # def lora_operation_mode(self, mode, api, endpoint="interface/{0}/lora/operationmode"):
    #     data={"thingId":self.thing_obj['result']["id"], "mode": mode}
    #     endpoint=endpoint.format(self.thing_obj['result']["id"])
    #     self.lora_operation_mode_state=api._api_request(endpoint, headers=api.headers, data=data)
    #     return self.lora_operation_mode_state

    # def update_lora_operation_mode(self, mode, api, endpoint="interface/{0}/lora/operationmode", verb="put"):
    #     data={"thingId":self.thing_obj['result']["id"], "mode": mode}
    #     endpoint=endpoint.format(self.thing_obj['result']["id"])
    #     self.update_lora_operation_mode_state=api._api_request(endpoint, headers=api.headers, data=data, verb=verb)
    #     return self.update_lora_operation_mode_state
