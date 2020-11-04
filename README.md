# Python API for Incognito SDK

To use this library in your applications, just run the command below in the root directory (which contains setup.py file):

```
pip3 install .
```

As of now, the library is incomplete. As time goes by, we'll try to evolve it. The current version supports:

- Subscription methods (require a full node with websocket support): ```subcribenewshardblock```, ```subcribenewbeaconblock```, ```subcribependingtransaction```
- Public RPC methods: ```extractpdeinstsfrombeaconblock```, ```getpdestate```, ```getblockchaininfo```, ```getblocks```, ```getmempoolinfo```, ```getpdetradestatus```, ```gettransactionbyhash```
- Private RPC methods: ```createandsendprivacycustomtokentransaction```, ```createandsendtxwithptokencrosspooltradereq```
