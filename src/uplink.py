
class Uplink():

    def post_anonymous_raw(self, base64, api, token, endpoint='data/uplink/anonymous/raw', verb='post'):
        data={'base64':base64, }
        api.headers['Authorization']='Bearer ' + token
        self._post_anonymous_raw=api._api_request(endpoint, headers=api.headers, data=data, verb=verb)
        return self._post_anonymous_raw

    def post_anonymous_cbor(self, base64, api, token, endpoint='data/uplink/anonymous/cbor', verb='post'):
        data={'base64':base64, }
        api.headers['Authorization']='Bearer ' + token
        self._post_anonymous_cbor=api._api_request(endpoint, headers=api.headers, data=data, verb=verb)
        return self._post_anonymous_cbor

    def post_anonymous_json(self, json, api, token, endpoint='data/uplink/anonymous/json', verb='post'):
        json={'json':json, }
        api.headers['Authorization']='Bearer ' + token
        self._post_anonymous_json=api._api_request(endpoint, headers=api.headers, json=json, verb=verb)
        return self._post_anonymous_json
