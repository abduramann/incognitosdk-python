import json
import requests
from websocket import create_connection
from .Response import Response
import threading


class Rpc:
    def __init__(self, url):
        self._headers = {'Content-Type': 'application/json'}
        self._id = 1
        self._json_rpc = "1.0"
        self._base_url = url
        self._params = None
        self._method = None

    def with_params(self, params):
        self._params = params
        return self

    def with_method(self, method):
        self._method = method
        return self

    def execute(self):
        data = {"jsonrpc": self._json_rpc,
                "id": self._id,
                "method": self._method}
        if self._params is not None:
            data["params"] = self._params

        response = requests.post(self._base_url, data=json.dumps(data), headers=self._headers)

        return Response(response, f'From: {self._base_url}')


class WebSocket:
    def __init__(self, url, timeout=180):
        self._timeout = timeout
        self._url = url
        self._ws_conn = None
        self._type = 0
        self._json_rpc = "1.0"
        self._id = 1

        self._dictSubscription = {}
        self._threadSubscription = None

    def open(self):
        if self._ws_conn is None:
            self._ws_conn = create_connection(self._url, self._timeout)
            return

        if not self.is_alive():
            self._ws_conn = create_connection(self._url, self._timeout)

    def close(self):
        self._ws_conn.close()

    def is_alive(self):
        return self._ws_conn.connected

    def subscribe(self, subscriptionType, params, handler):
        uniqueSubscriptionId = subscriptionType + " " + str(params)
        if uniqueSubscriptionId not in self._dictSubscription:
            self._dictSubscription[uniqueSubscriptionId] = [handler]
            data = {"request": {"jsonrpc": self._json_rpc, "method": subscriptionType, "params": params,
                                "id": self._id},
                    "subcription": uniqueSubscriptionId, "type": self._type}
            self.open()
            self._ws_conn.send(json.dumps(data))

            # self.send(subscriptionType, params)
        else:
            self._dictSubscription[uniqueSubscriptionId].append(handler)

        if self._threadSubscription is None:
            self._threadSubscription = threading.Thread(target=self._watchSubcriptions)
            self._threadSubscription.start()

    def _watchSubcriptions(self):
        while True:
            response = Response(self._ws_conn.recv())
            uniqueSubscriptionId = response.get_subscription_type()
            handlers = self._dictSubscription[uniqueSubscriptionId]
            for handler in handlers:
                handler(uniqueSubscriptionId.split()[0], response)