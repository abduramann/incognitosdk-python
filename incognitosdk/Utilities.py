PRV_ID = "0000000000000000000000000000000000000000000000000000000000000004"

BURNING_ADDRESS = "12RxahVABnAVCGP3LGwCn8jkQxgw7z1x14wztHzn455TTVpi1wBq9YGwkRMQg3J4e657AbAnCvYCJSdA9czBUNuCKwGSRQt55Xwz8WA"


def coin(amount, decimals, nano=True):
    if nano:
        return amount * (10 ** decimals)
    else:
        return amount / (10 ** decimals)


def calculateBuyAmount(sellAmount, sellPoolAmount, buyPoolAmount):
    return buyPoolAmount - (buyPoolAmount * sellPoolAmount) / (sellPoolAmount + sellAmount)


def fp(value, precision):
    formattedValue = f'{value:.{precision}f}'.rstrip('0').rstrip('.')
    if formattedValue == "0":
        formattedValue = f'{"" if value > 0 else "-"}0.{"0" * (precision - 1)}1'
    return formattedValue


def c(value):
    return fp(value, 9)


def p(value):
    return fp(value, 2)
