from .sensor import Sensor

class Data():

    def get_sensors(self, api, endpoint="data/{0}/sensors"):
        endpoint=endpoint.format(self.thing_obj["id"])
        self.sensors.extend([Sensor(sensor) for sensor in api._api_request(endpoint, headers=api.headers,)['result']])
        return self.sensors

    def get_sensor(self, type, api, endpoint='data/{0}/sensor'):
        endpoint=endpoint.format(self.thing_obj["id"])
        params={'type':type, }
        self._get_sensor=api._api_request(endpoint, headers=api.headers, params=params)
        return self._get_sensor

    def get_commands(self, api, endpoint='data/{0}/commands'):
        endpoint=endpoint.format(self.thing_obj["id"])
        self._get_commands= api._api_request(endpoint, headers=api.headers)
        return self._get_commands

    def execute_command(self, command_id, api, endpoint='data/{0}/execute'):
        endpoint= endpoint.format(self.thing_obj["id"])
        params={'commandId': command_id}
        self._execute_command= api._api_request(endpoint, headers=api.headers, params=params)
        return self._execute_command
