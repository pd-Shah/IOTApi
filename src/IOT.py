import requests
import json

class Api():

    # def __new__(cls, *args):
    #     if not hasattr(cls, "_instance"):
    #         cls._instance=object.__new__(cls)
    #     return cls._instance

    def __init__(self,  username=None, password=None, host="http://172.16.100.243/api/v1/"):
        self.username = username
        self.password = password
        self.host = host
        self.login()

    def _api_request(self, endpoint, verb='get', body=None, headers=None, data=None):
        response = getattr(requests, verb)(self.host + endpoint, json=body, headers=headers, data= data)
        print('{} {}'.format(response.status_code, response.reason))
        data = response.json()
        print(data)
        if isinstance(data, dict):
            messages = data.pop("messages", None)
            if messages:
                print(json.dumps(messages, indent=4))
        try:
            response.raise_for_status()
        except Exception as e:
            print(e)
            return None
        else:
            return data

    def login(self, endpoint="user/login", verb="post"):
        data={"username": self.username, "password": self.password}
        self.access_token=self._api_request(endpoint, verb, data=data)["result"]["accessToken"]
        self.headers={"Authorization":"Bearer " + self.access_token}
        return self.access_token, self.headers

    def signup(self, endpoint="user/signup", verb="post"):
        data={"username": self.username, "password": self.password}
        self.signup_state=self._api_request(endpoint, verb, data=data)
        return self.signup_state

    def renew(self, endpoint="user/renew"):
        self.renew_state=self._api_request(endpoint, headers=self.headers)
        return self.renew_state

class Person(object):

    def __init__(self, username, password):
        self.projects=[]
        self.api=Api(username, password)

    def get_projects(self, page_number, page_size, endpoint="project/list"):
        data={"pageNumber":page_number, "pageSize":page_size}
        self.projects.extend([Project(proj) for proj in self.api._api_request(endpoint, headers=self.api.headers, data=data)])
        return self.projects

    def make_new_project(self, project_name, project_description, endpoint="project/new", verb="post"):
        data={"name": project_name, "description":project_description}
        self.projects.append(Project(self.api._api_request(endpoint, verb=verb, data=data, headers=self.api.headers)))
        return self.projects[-1]

class Permission():
    def __init__(self, connection):
        self.headers=connection.headers

    def get_permission_list(self, page_number, page_size, endpoint="permission/list"):
        data={"pageNumber": page_number, "pageSize":page_size}
        self.permission_list=api._api_request(endpoint, headers=self.headers, data=data)
        return self.permission_list_state

    def grant_permission(self, project_id, user_id, permission_id, endpoint="permission/grant", verb="post"):
        data={"projectId": project_id, "userId":user_id, "permissionId":permission_id}
        self.grant_permission_state=api._api_request(endpoint, verb=verb, data=data, headers=self.headers)
        return self.grant_permission_state

    def deny_permission(self, project_id, user_id, permission_id, endpoint="permission/deny", verb="post"):
        data={"projectId": project_id, "userId":user_id, "permissionId":permission_id}
        self.deny_permission_state=api._api_request(endpoint, verb=verb, data=data, headers=self.headers)
        return self.deny_permission_state

    def get_permission(self, project_id, user_id, endpoint="query/{0}/{1}"):
        endpoint=endpoint.format(project_id, user_id)
        data={"projectId":project_id, "userId":user_id}
        self.get_permission_state=api._api_request(endpoint, data=data, headers=self.headers)
        return self.get_permission_state

class ProjectCaptcha():

    def captcha_generate_deletion(self, api, endpoint="captcha/generate/project/deletion"):
        data={"projectId":self.project_obj["id"]}
        self.captcha_generate_deletion_state=api._api_request(endpoint, headers=api.headers, data=data)
        return self.captcha_generate_deletion_state

    def captcha_generate_modification(self, api, endpoint="captcha/generate/project/modification"):
        data={"projectId":self.project_obj["id"]}
        self.captcha_generate_modification_state=api._api_request(endpoint, headers=api.headers, data=data)
        return self.captcha_generate_modification_state

class Project(ProjectCaptcha):

    def __init__(self, project_obj):
        self.project_obj=project_obj
        self.things=[]

    def get_project_info(self, api, endpoint="project/{0}/info"):
        endpoint=endpoint.format(self.project_obj["id"])
        self.info=api._api_request(endpoint, headers=api.headers)
        return self.info_state

    def update_project_info(self, new_name, new_description, api, endpoint="project/{0}/info", verb="put"):
        endpoint=endpoint.format(self.project_obj["id"])
        data={"name": new_name, "description": new_description}
        self.project_info_update_state=api._api_request(endpoint, headers=api.headers, verb=verb, data=data)
        return self.project_info_update_state

    def get_things(self, page_number, page_size, api, endpoint="project/{0}/things"):
        endpoint=endpoint.format(self.project_obj["id"])
        data={"pageNumber":page_number, "pageSize":page_size, projectId: self.project_obj["id"]}
        self.things.extend([Thing(thing) for thing in  api._api_request(endpoint, headers=api.headers, data=data)])
        return self.things

    def delete_project(self, api, endpoint="project/{0}", verb="delete"):
        endpoint=endpoint.format(self.project_obj["id"])
        self.delete_state=api._api_request(endpoint, headers=api.headers, verb=verb)
        return self.delete_state

    def update_project(self, new_name, new_description, api, endpoint="project/{0}", verb="put"):
        endpoint=endpoint.format(self.project_obj["id"])
        data={"name": new_name, "description":new_description}
        self.project_update_state=api._api_request(endpoint, headers=api.headers, verb=verb, data=data)
        return self.project_update_state

    def get_permission(self, api, endpoint="project/{0}/permission"):
        endpoint=endpoint.format(self.project_obj["id"])
        self.permission= api._api_request(endpoint, headers=api.headers)
        return self.permission_state

    # def delete_permission(self, api, endpoint="project/{0}/permission", verb="delete"):
    #     endpoint=endpoint.format(self.project_obj["id"])
    #     self.delete_permission_state=api._api_request(endpoint, headers=api.headers, verb=verb)
    #     return self.delete_permission_state

    # def update_permission(self, api, endpoint="project/{0}/permission", verb="put"):
    #     endpoint=endpoint.format(self.project_obj["id"])
    #     self.update_permission_state=api._api_request(endpoint, headers=api.headers, verb=verb)
    #     return self.delete_permission_state

    def get_project_users(self, page_number, page_size, api, endpoint="project/{0}/users"):
        endpoint=endpoint.format(self.project_obj["id"])
        data={"projectId": self.project_obj["id"], "pageNumber":page_number, "pageSize":page_size}
        self.project_users_state=api._api_request(endpoint, headers=api.headers, data=data)
        return self.project_users_state

    def make_new_thing(self, thing_name, description, api, endpoint="thing/new", verb="post"):
        data={"projectId": self.project_obj["id"], "name":thing_name, "description":description}
        self.things.append(Thing(api._api_request(endpoint, headers=api.headers, data=data)))
        return self.things[-1]

class Interface():

    def get_lora(self, api, endpoint="interface/{0}/lora/enable"):
        endpoint=endpoint.format(self.thing_obj["id"])
        self.lora=api._api_request(endpoint, headers=api.headers)
        return self.lora_state

    def update_lora(self, enable, api, endpoint="interface/{0}/lora/enable", verb="put"):
        endpoint=endpoint.format(self.thing_obj["id"])
        data={"enable":enable}
        self.update_lora_state=api._api_request(endpoint, headers=api.headers, data= data, verb=verb)
        return self.update_lora_state

    def get_lora_otaa(self, api, endpoint="interface/{0}/lora/otaa"):
        endpoint=endpoint.format(self.thing_obj["id"])
        self.lora_otaa_state=api._api_request(endpoint, headers=api.headers)
        return self.lora_otaa_state

    def update_lora_otaa(self, app_key, app_EUI, dev_EUI, api, endpoint="interface/{0}/lora/otaa", verb="put"):
        endpoint=endpoint.format(self.thing_obj["id"])
        data={"thingId":self.thing_obj["id"], "appkey":app_key, "appEUI":app_EUI, "devEUI":dev_EUI}
        self.update_lora_otaa_state=api._api_request(endpoint, headers=api.headers, data=data, verb=verb)
        return self.update_lora_otaa_state

    def get_lora_abp(self,api, endpoint="interface/{0}/lora/abp"):
        endpoint=endpoint.format(self.thing_obj["id"])
        self.lora_abp_state=api._api_request(endpoint, headers=api.headers)
        return self.lora_abp_state

    def update_lora_abp(self, app_skey, nwk_skey, dev_addr, api, endpoint="interface/{0}/lora/abp", verb="put"):
        data={"thingId":self.thing_obj["id"], "appSkey":app_skey, "nwkSkey":nwk_skey, "devAddr":dev_addr}
        endpoint=endpoint.format(self.thing_obj["id"])
        self.update_lora_abp_state=api._api_request(endpoint, headers=api.headers, data=data, verb=verb)
        return self.update_lora_abp_state

    def lora_operation_mode(self, mode, api, endpoint="interface/{0}/lora/operationmode"):
        data={"thingId":self.thing_obj["id"], "mode": mode}
        endpoint=endpoint.format(self.thing_obj["id"])
        self.lora_operation_mode_state=api._api_request(endpoint, headers=api.headers, data=data)
        return self.lora_operation_mode_state

    def update_lora_operation_mode(self, mode, api, endpoint="interface/{0}/lora/operationmode", verb="put"):
        data={"thingId":self.thing_obj["id"], "mode": mode}
        endpoint=endpoint.format(self.thing_obj["id"])
        self.update_lora_operation_mode_state=api._api_request(endpoint, headers=api.headers, data=data, verb=verb)
        return self.update_lora_operation_mode_state

    def check_mqtt(self, api, endpoint="interface/{0}/mqtt/enable"):
        endpoint=endpoint.format(self.thing_obj["id"])
        self.mqtt=api._api_request(endpoint, headers=api.headers)
        return self.mqtt_state

    def update_mqtt(self, enable, api, endpoint="interface/{0}/mqtt/enable", verb="put"):
        endpoint=endpoint.format(self.thing_obj["id"])
        data={"enable": enable, "thingId": self.thing_obj["id"]}
        self.update_mqtt_state=api._api_request(endpoint, headers=api.headers, data=data, verb=verb)
        return self.update_mqtt_state

    def get_mqtt_sub(self, api, endpoint="interface/{0}/mqtt/sub"):
        endpoint=endpoint.format(self.thing_obj["id"])
        self.get_mqtt_sub_state=api._api_request(endpoint, headers=api.headers)
        return self.get_mqtt_sub_state

    def update_mqtt_sub(self, enable, api, endpoint="interface/{0}/mqtt/sub", verb="put"):
        endpoint=endpoint.format(self.thing_obj["id"])
        data={"enable":enable, "thingId": self.thing_obj["id"]}
        self.update_mqtt_sub_state=api._api_request(endpoint, headers=api.headers, verb=verb, data=data)
        return self.update_mqtt_sub_state

    def get_mqtt_pub(self, api, endpoint="interface/{0}/mqtt/pub"):
        endpoint=endpoint.format(self.thing_obj["id"])
        self.mqtt_pub_state=api._api_request(endpoint, headers=api.headers)
        return self.mqtt_pub_state

    def update_mqtt_pub(self, enable, api, endpoint="interface/{0}/mqtt/pub", verb="put"):
        data={"thingId":self.thing_obj["id"], "enable":enable}
        endpoint=endpoint.format(self.thing_obj["id"])
        self.update_mqtt_pub_state=api._api_request(endpoint, headers=api.headers, verb=verb, data=data)
        return self.update_mqtt_pub_state

    def check_jwt(self, api, endpoint="interface/{0}/jwt/enable"):
        endpoint=endpoint.format(self.thing_obj["id"])
        self.jwt=api._api_request(endpoint, headers=api.headers)
        return self.jwt_state

    def update_jwt(self, enable, api, endpoint="interface/{0}/jwt/enable", verb="put"):
        endpoint=endpoint.format(self.thing_obj["id"])
        data={"thingId":self.thing_obj["id"], "enable":enable}
        self.update_jwt_state=api._api_request(endpoint, headers=api.headers, verb=verb, data=data)
        return self.update_jwt_state

    def get_jwt_settings(self, api, endpoint="interface/{0}/jwt/settings"):
        endpoint=endpoint.format(self.thing_obj["id"])
        self.get_jwt_settings_state=api._api_request(endpoint, headers=api.headers)
        return get_jwt_settings_state

    def update_jwt_settings(self, key, audience, issuer, description, api, endpoint="interface/{0}/jwt/settings", verb="put"):
        endpoint=endpoint.format(self.thing_obj["id"])
        data={"thingId":self.thing_obj["id"], "key":key, "audience":audience, "issuer":issuer, "description":description}
        self.update_jwt_settings_state=api._api_request(endpoint, headers=api.headers, verb=verb, data=data)
        return update_jwt_settings_state

    def get_jwt_generate(self, seconds, endpoint="interface/{0}/jwt/generate"):
        endpoint=endpoint.format(self.thing_obj["id"])
        data={"seconds": seconds, "thingId":self.thing_obj["id"]}
        self.get_jwt_generate_state=api._api_request(endpoint, headers=api.headers, data=data)
        return self.get_jwt_generate_state

class ThingCaptcha():

    def captcha_generate_modification(self, api, endpoint="captcha/generate/thing/modification"):
        data={"thingId":self.thing_obj["id"], }
        self.captcha_generate_modification_state=api._api_request(endpoint, headers=api.headers, data=data)
        return self.captcha_generate_modification_state

    def captcha_generate_deletion(self, api, endpoint="captcha/generate/thing/deletion"):
        data={"thingId":self.thing_obj["id"], }
        self.captcha_generate_deletion_state=api._api_request(endpoint, headers=api.headers, data=data)
        return self.captcha_generate_deletion_state

class Thing(Interface, ThingCaptcha):

    def __init__(self, thing_obj):
        self.thing_obj=thing_obj
        self.sensors=[]

    def get_sensors(self, page_number, page_size, api, endpoint="thing/{0}/sensors"):
        endpoint=endpoint.format(self.thing_obj["id"])
        data={"thingId":self.thing_obj["id"], "pageNumber":page_number, "pageSize":page_size }
        self.sensors.extend([Sensor(sensor) for sensor in api._api_request(endpoint, headers=api.headers, data=data)])
        return self.sensors_state

    def delete_thing(self, api, endpoint="thing/{0}", verb="delete"):
        endpoint=endpoint.format(self.thing_obj["id"])
        self.delete_thing_sate= api._api_request(endpoint, headers=api.headers, verb=verb)
        return delete_thing_state

    def get_raw_data(self, page_number, page_size, api, endpoint="thing/{0}/data/raw"):
        endpoint=endpoint.format(self.thing_obj["id"])
        data={"pageNumber": page_number,"thingId":endpoint.format(self.thing_obj["id"]), "pageSize": page_size}
        self.raw_data=api._api_request(endpoint, headers=api.headers, data=data)
        return self.raw_data_state

    def get_thing_interfaces(self, api, endpoint="thing/{0}/interfaces"):
        endpoint=endpoint.format(self.thing_obj["id"])
        data={"thingId":endpoint.format(self.thing_obj["id"])}
        self.thing_interfaces=api._api_request(endpoint, headers=api.headers, data=data)
        return self.thing_interfaces_state

    def get_location(self, api, endpoint="thing/{0}/location"):
        endpoint=endpoint.format(self.thing_obj["id"])
        data={"thingId":endpoint.format(self.thing_obj["id"])}
        self.location=api._api_request(endpoint, headers=api.headers, data=data)
        return self.location_state

    def update_location(self, latitude, longitude, api, endpoint="thing/{0}/data/raw", verb="put"):
        endpoint=endpoint.format(self.thing_obj["id"])
        data={"latitude": latitude,"thingId":endpoint.format(self.thing_obj["id"]), "longitude": longitude}
        self.update_location_state=api._api_request(endpoint, headers=api.headers, data=data, verb=verb)
        return self.update_location_state

    def get_data_sensor_by_type(self, _type, page_number, page_size, api, endpoint="thing/{0}/data/sensor/{1}"):
        endpoint=endpoint.format(self.thing_obj["id"], _type)
        data={"thingId": self.thing_obj["id"] ,"type":_type, "pageNumber":page_number, "pageSize":page_size}
        self.data_sensor_by_type_state= api._api_request(endpoint, headers=api.headers, data=data)
        return self.data_sensor_by_type_state

    def get_script(self, api, endpoint="thing/{0}/script"):
        endpoint=endpoint.format(self.thing_obj["id"])
        self.script_state= api._api_request(endpoint, headers=api.headers)
        return self.script_state

    def update_scrip(self, script, api, endpoint="thing/{0}/script"):
        endpoint=endpoint.format(self.thing_obj["id"])
        data={"thingId":self.thing_obj["id"], "script":script,}
        self.update_scrip_state=api._api_request(endpoint, headers=api.headers, data=data)
        return self.update_scrip_state

class Sensor():

    def __init__(self, sensor_obj):
        self.sensor_obj=sensor_obj

class Script():
    def get_script_validation(self, param, code, api, endpoint="script/validate"):
        data={"param":param, "code":code}
        self.script_validation_state=api._api_request(endpoint, headers=api.headers, data=data)
        return script_validation_state

class Data():

    def make_anonymous_raw(self, base64, api, endpoint="data/anonymous/raw", verb="post"):
        data={"base64":base64}
        self.anonymous_raw_state=api._api_request(endpoint, headers=api.headers, data=data, verb=verb)
        return self.anonymous_raw_state

    def make_raw_noscript(self, base64, api, endpoint="data/raw/noscript", verb="post"):
        data={"base64":base64}
        self.raw_noscript_state=api._api_request(endpoint, headers=api.headers, data=data, verb=verb)
        return self.raw_noscript_state

    def make_anonymous_cbor(self, base64, api, endpoint="data/anonymous/cbor", verb="post"):
        data={"base64":base64}
        self.anonymous_cbor_state=api._api_request(endpoint, headers=api.headers, data=data, verb=verb)
        return self.anonymous_cbor_state

    def make_anonymous_cbor_noscript(self, base64, api, endpoint="data/anonymous/cbor/noscript", verb="post"):
        data={"base64":base64}
        self.anonymous_cbor_noscript_state=api._api_request(endpoint, headers=api.headers, data=data, verb=verb)
        return self.anonymous_cbor_noscript_state

    def make_anonymous_json(self, json, api, endpoint="data/anonymous/json", verb="post"):
        data={"json":json}
        self.anonymous_json_state=api._api_request(endpoint, headers=api.headers, data=data, verb=verb )
        return self.anonymous_json_state

    def make_anonymous_json_noscript(self, json, api, endpoint="data/anonymous/json/noscript", verb="post"):
        data={"json": json}
        self.anonymous_json_noscript_state= api._api_request(endpoint, headers= api.headers, data=data, verb=verb)
        return self.anonymous_json_noscript_state

if __name__=="__main__":

    pd=Person("pd", "123456")
    connection=pd.api
    print(pd.api.headers)
    print(pd.api.access_token)
    print(pd.api.host)

    # pd.make_new_project("new", "new")
    # pd.get_projects(page_size=10, page_number=0)
    # print(pd.projects)
    # print(pd.projects[0])
    #
    # pd.projects[0].update_project_info("new name", "new description", connection)
    # print(pd.projects[0].project_info_update_state)
    #
    # pd.projects[0].update_project("new name", "new description", connection)
    # print(pd.projects[0].project_update_state)
    # print(pd.projects[0].things)
    # print(pd.projects[0].project_obj)
    # print(pd.projects[0].project_obj["id"])
    #
    # pd.projects[0].get_project_info(connection)
    # print(pd.projects[0].info)
    #
    # pd.projects[0].get_permission(connection)
    # print(pd.projects[0].permission)

    # pd.projects[0].delete_permission(connection)
    # print(pd.projects[0].delete_permission_state)
    #
    # pd.projects[0].update_permission(connection)
    # print(pd.projects[0].update_permission_state)
    #
    # pd.projects[0].delete_project(connection)
    # print(pd.projects[0].delete_state)
    #
    # pd.projects[0].get_things(connection)
    # print(pd.projects[0].things)
    # print(pd.projects[0].things[0])
    # print(pd.projects[0].things[0].thing_obj)
    # print(pd.projects[0].things[0].thing_obj["id"])
    # print(pd.projects[0].things[0].sensors)
    #
    # pd.projects[0].things[0].delete_thing(connection)
    # print(pd.projects[0].things[0].delete_thing_state)
    #
    # pd.projects[0].things[0].get_sensors(connection)
    # print(pd.projects[0].things[0].sensors)
    # print(pd.projects[0].things[0].sensors[0].sensor_obj)
