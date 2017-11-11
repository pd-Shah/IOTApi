
class Uplink():

    def post_anonymous_raw(self, base64, api, endpoint='data/uplink/anonymous/raw', verb='post'):
        data={'base64':base64, }
        self._post_anonymous_raw=api._api_request(endpoint, headers=api.headers, data=data)
        return self._post_anonymous_raw

    def post_anonymous_cbor(self, base64, api, endpoint='data/uplink/anonymous/cbor', verb='post'):
        data={'base64':base64, }
        self._post_anonymous_cbor=api._api_request(endpoint, headers=api.headers, data=data)
        return self._post_anonymous_cbor

    def post_anonymous_json(self, json, api, endpoint='data/uplink/anonymous/json', verb='post'):
        data={'json':json, }
        self._post_anonymous_json=api._api_request(endpoint, headers=api.headers, data=data)
        return self._post_anonymous_json
