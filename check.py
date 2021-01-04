from binance.client import Client

from Initialize_API import InitializeAPI

client = InitializeAPI()


class Check:
    def __init__(self,client):
        self.client = client

    def CheckMarketPriceOfCoin(self,exchange):
        
        prices = client.get_symbol_ticker(symbol=exchange)
        return float(prices["price"])
        
        # asset = 'BTC','ETH'
    def CheckBalance(self,asset):
        availableBalance = client.get_asset_balance(asset=asset)
        freeBalance = float(availableBalance["free"])
        return freeBalance