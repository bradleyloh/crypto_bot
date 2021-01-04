from binance.client import Client
from binance.exceptions import BinanceAPIException
import sys
import decimal


## To Configure
## Only Works for BTC

api_key = ""

api_secret = ""

# To initialize API
client = Client(api_key, api_secret)

# Check individual price of coin
def checkMarketPriceOfCoin(exchange):
    prices = client.get_all_tickers()

    for value in prices:
        if value['symbol'] == exchange:
            return (float(value["price"]))
    print("Invalid Exchange")
    return sys.exit()

# Check the amount of quantity
def convertToQuantity(exchange,amountBalance,amountPercentage):
    amountUsed = amountBalance*amountPercentage
    marketPrice = checkMarketPriceOfCoin(exchange)
    quantity = amountUsed/marketPrice
    return quantity


def reduceDecimalPlaces(quantity):

    # Check no. of decimal places
    decimalPlaces = abs(decimal.Decimal(str(quantity)).as_tuple().exponent)
    
    # Decreasing decimal value
    if decimalPlaces > 10:
        decimalPlaces = 9
    if decimalPlaces == 1:
        quantity = float(int(quantity))
        return quantity

    # multiply by 10^x so that it can reduce by 1 decimal place
    reducedSizeBy = str(1/(10**(int(decimalPlaces) - 1)))
    newValue = decimal.Decimal(quantity).quantize(decimal.Decimal(reducedSizeBy),rounding=decimal.ROUND_DOWN)
    return float(newValue)

def main(amountPercentage,altCoin):

    # Check BTC Balance
    balance = client.get_asset_balance(asset='BTC')
    free_balance = float(balance["free"])

    # SUPPORT BTC ONLY
    exchange = altCoin + "BTC"
    # Need to convert to count the no. of quantity to BUY since its required for the API
    quantity = convertToQuantity(exchange,free_balance,float(amountPercentage))

    # Place a test market buy order, to place an actual order use the create_order function
    # Try to buy coin, if there is an error, repeat till you get no error by reducing decimal place
    while True:
        try:
            order = client.create_test_order(
                symbol=exchange,
                side=Client.SIDE_BUY,
                type=Client.ORDER_TYPE_MARKET,
                quantity=quantity)
            print(quantity)
            print("Done")
            break

        except BinanceAPIException as e:

            print(e.message)
            quantity = reduceDecimalPlaces(quantity)
            print(quantity)


if __name__ == "__main__":

    # Ask user for input
    amountPercentage = input("Percentage (enter 0.0-1.00): ")
    altCoin = input("Enter alt-coin eg. IDEX: ")

    main(amountPercentage,altCoin)




