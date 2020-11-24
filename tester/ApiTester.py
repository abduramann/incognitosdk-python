import sys
from cmd import Cmd
from incognitosdk.Incognito import *

config = Incognito.Config()
config.WsUrl = None  # Do not open websocket connection
incognitoApi = Incognito(config)


class testShell(Cmd):
    prompt = 'Please enter the command: '
    command = None

    # for commands just requiring its parameters in a list
    def do_run(self, arg):
        params = str(arg).split()
        res = incognitoApi._rpc._run(params[0],
                                     [int(x) if x.isdigit() else x for x in params[1:]] if len(params) > 1 else [])
        print(res)
        with open(f'result.json', 'w') as outfile:
            json.dump(res.data(), outfile);

    def do_retb(self, arg):
        params = str(arg).split()
        print(incognitoApi._rpc._run("retrieveblock", [params[0], '1']))

    def do_retbbh(self, arg):
        params = str(arg).split()
        print(incognitoApi._rpc._run("retrieveblockbyheight", [int(params[0]), int(params[1]), '1']))

    def do_bretb(self, arg):
        params = str(arg).split()
        print(incognitoApi._rpc._run("retrievebeaconblock", [params[0], '1']))

    def do_bretbbh(self, arg):
        params = str(arg).split()
        print(incognitoApi._rpc._run("retrievebeaconblockbyheight", [int(params[0]), '1']))

    def do_blockchain(self, arg):
        print(incognitoApi.Public.get_blockchain_info())

    def do_trade(self, arg):
        params = str(arg).split()
        print(incognitoApi.Private.trade_token_cross(params[0], params[1], params[2], float(params[3]), params[4],
                                                     float(params[5])))

    def do_sendprv(self, arg):
        params = str(arg).split()
        print(incognitoApi.Private.send_prv(params[0], params[1], float(params[2])))

    def do_sendtoken(self, arg):
        params = str(arg).split()
        print(incognitoApi.Private.send_token(params[0], params[1], params[2], float(params[3]),
                                              float(params[4]) if len(params) > 4 else 0))

    def do_exit(self, arg):
        sys.exit()

    def emptyline(self):
        pass


shell = testShell()

while True:
    try:
        shell.cmdloop()
    except (SystemExit, KeyboardInterrupt):
        raise
    except:
        raise
