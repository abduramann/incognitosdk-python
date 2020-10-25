from .Connections import *


class Incognito:
    def __init__(self, config=None):
        self._config = Incognito.Config() if config is None else config
        self._websocket = WebSocket(self._config.WsUrl)
        self._websocket.open()
        self._rpc = Rpc(url=self._config.RpcUrl)

        self.Public = Incognito.Public(self)

    def destroy(self):
        self._websocket.close()

    class Config:
        def __init__(self):
            self.RpcUrl = "https://mainnet.incognito.org/fullnode"
            self.WsUrl = "ws://fullnode.incognito.best:19334"
            self.TokenListUrl = "https://api.incognito.org/ptoken/list"

    class Public:
        def __init__(self, incognito_instance):
            self._ii = incognito_instance
            self._rpc = self._ii._rpc
            self._websocket = self._ii._websocket
            self._config = self._ii._config

        def get_pde_inst(self, beacon_height):
            return self._rpc. \
                with_method("extractpdeinstsfrombeaconblock"). \
                with_params([{"BeaconHeight": beacon_height}]). \
                execute()

        def get_pde_state(self, beacon_height):
            return self._rpc. \
                with_method("getpdestate"). \
                with_params([{"BeaconHeight": beacon_height}]). \
                execute()

        def get_token_list(self):
            return requests.get(self._config.TokenListUrl)

        def subscribe(self, subscriptionType, params, handler):
            return self._websocket.subscribe(subscriptionType, params, handler)

    class Private:
        def getbalance(self, incognito_instance):
            self._ii = incognito_instance
            self._rpc = self._ii._rpc
            self._websocket = self._ii._websocket
            self._config = self._ii._config
