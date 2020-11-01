class SubscriptionType:
    """
    Enumeration of Websocket subscriptions
    """
    NewShardBlock = "subcribenewshardblock"
    PendingTransaction = "subcribependingtransaction"
    NewBeaconBlock = "subcribenewbeaconblock"


class TransactionType:
    Shielding = 25
    Erc20Shielding = 81
    Trade = 206


class TradeStatus:
    Accepted = "xPoolTradeAccepted"
