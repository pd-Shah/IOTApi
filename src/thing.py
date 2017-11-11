from thing_captcha import ThingCaptcha
from data import Data
from jwt import JWT
from lora_wan import LoRaWAN
from sensor import Sensor

class Thing(ThingCaptcha, Data, JWT, LoRaWAN):

    def __init__(self, thing_obj):
        self.thing_obj=thing_obj
        self.sensors=[]

    def get_info(self, api, endpoint="thing/{0}/info"):
        endpoint=endpoint.format(self.thing_obj["id"])
        data={"thingId":self.thing_obj["id"], }
        self._get_info=api._api_request(endpoint, headers=api.headers, data=data)
        return self._get_info

    def set_info(self, name, description, api, endpoint="thing/{0}/info", verb="put"):
        endpoint=endpoint.format(self.thing_obj["id"])
        data={"thingId":self.thing_obj["id"], "name":name, "description":description, }
        self._set_info=api._api_request(endpoint, headers=api.headers, data=data, verb=verb)
        return self._set_info

    def get_location(self, api, endpoint="thing/{0}/location"):
        endpoint=endpoint.format(self.thing_obj["id"])
        self._get_location=api._api_request(endpoint, headers=api.headers, )
        return self._get_location

    def set_location(self, latitude, longitude, api, endpoint="thing/{0}/location", verb='put'):
        endpoint=endpoint.format(self.thing_obj["id"])
        data={"latitude": latitude, "longitude":longitude, "thingId":self.thing_obj["id"], }
        self._set_location=api._api_request(endpoint, headers=api.headers, data=data, verb=verb)
        return self._set_location

    def get_program(self, api, endpoint='thing/{0}/program'):
        endpoint=endpoint.format(self.thing_obj["id"])
        self._get_program=api._api_request(endpoint, headers=api.headers, )
        return self._get_program

    def set_program(self, program_id, api, endpoint='thing/{0}/program', verb='put'):
        endpoint=endpoint.format(self.thing_obj["id"])
        data={'programId':program_id, 'thingId':self.thing_obj["id"]}
        self._set_program=api._api_request(endpoint, headers=api.headers, verb=verb, data=data)
        return self._set_program

    #
    # def delete_thing(self, api, endpoint="thing/{0}", verb="delete"):
    #     endpoint=endpoint.format(self.thing_obj['result']["id"])
    #     self.delete_thing_state= api._api_request(endpoint, headers=api.headers, verb=verb)
    #     return self.delete_thing_state
    #
    # def get_raw_data(self, page_number, page_size, api, endpoint="thing/{0}/data/raw"):
    #     endpoint=endpoint.format(self.thing_obj['result']["id"])
    #     data={"pageNumber": page_number,"thingId":endpoint.format(self.thing_obj['result']["id"]), "pageSize": page_size}
    #     self.raw_data=api._api_request(endpoint, headers=api.headers, data=data)
    #     return self.raw_data_state
    #
    # def get_thing_interfaces(self, api, endpoint="thing/{0}/interfaces"):
    #     endpoint=endpoint.format(self.thing_obj['result']["id"])
    #     data={"thingId":endpoint.format(self.thing_obj['result']["id"])}
    #     self.thing_interfaces=api._api_request(endpoint, headers=api.headers, data=data)
    #     return self.thing_interfaces_state

    # def get_data_sensor_by_type(self, _type, page_number, page_size, api, endpoint="thing/{0}/data/sensor/{1}"):
    #     endpoint=endpoint.format(self.thing_obj['result']["id"], _type)
    #     data={"thingId": self.thing_obj['result']["id"] ,"type":_type, "pageNumber":page_number, "pageSize":page_size}
    #     self.data_sensor_by_type_state= api._api_request(endpoint, headers=api.headers, data=data)
    #     return self.data_sensor_by_type_state
    #
    # def get_script(self, api, endpoint="thing/{0}/script"):
    #     endpoint=endpoint.format(self.thing_obj['result']["id"])
    #     self.script_state= api._api_request(endpoint, headers=api.headers)
    #     return self.script_state
    #
    # def update_scrip(self, script, api, endpoint="thing/{0}/script"):
    #     endpoint=endpoint.format(self.thing_obj['result']["id"])
    #     data={"thingId":self.thing_obj['result']["id"], "script":script,}
    #     self.update_scrip_state=api._api_request(endpoint, headers=api.headers, data=data)
    #     return self.update_scrip_state
