import decimal
import sys

from binance.client import Client

from Initialize_API import InitializeAPI

from check import Check

client = InitializeAPI()

class Calculations:

    def __init__(self,client):
        self.client = client

    def ConvertToQuantityBaseOnMarket(self,exchange,amountBalance,amountPercentage):
        amountUsed = amountBalance*float(amountPercentage)
        marketPrice = Check.CheckMarketPriceOfCoin(client,exchange)
        quantity = amountUsed/marketPrice
        return quantity

    def ReduceDecimalPlaces(self,quantity):

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