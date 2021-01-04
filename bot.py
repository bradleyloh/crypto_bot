from binance.client import Client
from binance.exceptions import BinanceAPIException

import sys
import decimal

from Initialize_API import InitializeAPI

from check import Check
from calculations import Calculations
from trade import Trade
import time

## To Configureclient
## Only Works for BTC


# To initialize API
client = InitializeAPI()

# Set Classes
Trade = Trade(client)
Cal = Calculations(client)
Check = Check(client)

def main(amountPercentage,altCoin,profitPercent,lossPercent):

    # SUPPORT BTC ONLY
    defaultCoin = "BTC"

    # Check BTC Balance
    balance = Check.CheckBalance(defaultCoin)

    exchange = altCoin + defaultCoin
    
    # Need to convert to count the no. of quantity to BUY since its required for the API
    estimatedquantity = Cal.ConvertToQuantityBaseOnMarket(exchange,balance,amountPercentage)

    quantity,boughtPrice = Trade.MarketBuy(exchange,estimatedquantity)

    Trade.ZemusMethod(exchange,boughtPrice,profitPercent,lossPercent,quantity)



if __name__ == "__main__":

    # Ask user for input
    amountPercentage = input("Percentage (enter 0.0-1.00): ")
    altCoin = input("Enter alt-coin eg. IDEX: ")
    profitPercent = input("Enter percentage profit 5,10: ")
    lossPercent = input("Enter percentage 5,10: ")

    main(amountPercentage,altCoin,profitPercent,lossPercent)




