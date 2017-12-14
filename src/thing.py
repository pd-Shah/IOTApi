from .thing_captcha import ThingCaptcha
from .data import Data
from .jwt import JWT
from .lora_wan import LoRaWAN
from .sensor import Sensor

class Thing(ThingCaptcha, Data, JWT, LoRaWAN):

    def __init__(self, thing_obj):
        self.thing_obj=thing_obj
        self.sensors=[]

    def get_info(self, api, endpoint="thing/{0}/info"):
        endpoint=endpoint.format(self.thing_obj["id"])
        self._get_info=api._api_request(endpoint, headers=api.headers,)
        return self._get_info

    def set_info(self, name, description, api, endpoint="thing/{0}/info", verb="put"):
        endpoint=endpoint.format(self.thing_obj["id"])
        data={"name":name, "description":description, }
        self._set_info=api._api_request(endpoint, headers=api.headers, data=data, verb=verb)
        return self._set_info

    def get_location(self, api, endpoint="thing/{0}/location"):
        endpoint=endpoint.format(self.thing_obj["id"])
        self._get_location=api._api_request(endpoint, headers=api.headers, )
        return self._get_location

    def set_location(self, latitude, longitude, api, endpoint="thing/{0}/location", verb='put'):
        endpoint=endpoint.format(self.thing_obj["id"])
        data={"latitude": latitude, "longitude":longitude, }
        self._set_location=api._api_request(endpoint, headers=api.headers, data=data, verb=verb)
        return self._set_location

    def get_program(self, api, endpoint='thing/{0}/program'):
        endpoint=endpoint.format(self.thing_obj["id"])
        self._get_program=api._api_request(endpoint, headers=api.headers, )
        return self._get_program

    def set_program(self, program_id, api, endpoint='thing/{0}/program', verb='put'):
        endpoint=endpoint.format(self.thing_obj["id"])
        data={'programId':program_id, }
        self._set_program=api._api_request(endpoint, headers=api.headers, verb=verb, data=data)
        return self._set_program
