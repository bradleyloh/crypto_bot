from binance.client import Client

from binance.exceptions import BinanceAPIException

from calculations import Calculations as Cal

from check import Check

from Initialize_API import InitializeAPI

client = InitializeAPI()

class Trade:
    
    
    def __init__(self,client):
        self.client = client

    def MarketBuy(self,exchange,quantity):
        timeBefore = client.get_server_time()
        while True:
            try:
                order = client.create_test_order(
                    symbol=exchange,
                    side=Client.SIDE_BUY,
                    type=Client.ORDER_TYPE_MARKET,
                    quantity=quantity)

                print("Done with Market Buy")

                trades = client.get_my_trades(symbol=exchange)
                timeAfter = client.get_server_time()

                boughtPrice = 0

                for subtrade in trades:
                    if timeBefore['serverTime'] <= subtrade["time"] <= timeAfter['serverTime'] and subtrade['isBuyer'] == True:
                        boughtPrice = float(subtrade['price'])
                        print("Market Buy Price: " ,subtrade['price'])
                        return quantity, boughtPrice
                            
                boughtPrice = Check.CheckMarketPriceOfCoin(client,exchange)

                return quantity , boughtPrice

            except BinanceAPIException as e:

                print(e.message)
                quantity = Cal(client).ReduceDecimalPlaces(quantity)
                print(quantity)

    # x amount
    def ZemusMethod(self,exchange,buyPrice,profitPercent,lossPercent,quantity):
        profitPrice = float((1+(float(profitPercent)/100))*float(buyPrice))
        lossPrice = float((1-(float(lossPercent)/100))*float(buyPrice))

        while True:

            marketPrice = Check.CheckMarketPriceOfCoin(client,exchange)
            #print(marketPrice)
            percentagedifference = (((float(buyPrice) - marketPrice)/float(buyPrice))*100)*-1
            print(marketPrice,percentagedifference,"%")

            # lossPrice <= marketPrice <= profitPrice
            if marketPrice <= lossPrice or marketPrice >= profitPrice:
                try:
                    order = client.create_test_order(
                        symbol=exchange,
                        side=Client.SIDE_SELL,
                        type=Client.ORDER_TYPE_MARKET,
                        quantity=quantity)

                    print("Zemus Trading Completed!")
                    break

                except BinanceAPIException as e:
                    print(e.message)