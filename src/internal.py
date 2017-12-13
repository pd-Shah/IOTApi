class Internal():

    def lora_find_deveui(self, q, api, endpoint='internal/lora/find/deveui'):
        params={"q": q, }
        self._lora_find_deveui=api._api_request(endpoint, headers=api.headers, params=params)
        return self._lora_find_deveui

    def lora_find_devaddr(self, q, api, endpoint='internal/lora/find/devaddr'):
        params={'q':q, }
        self._lora_find_devaddr=api._api_request(endpoint, headers=api.headers, params=params)
        return self._lora_find_devaddr
