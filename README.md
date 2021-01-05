# Overview

This bot helps you to buy and sell cryptocurrencies on binance

## Quick Start

Prequisite

- [Python 3.7.8](https://www.python.org/downloads/release/python-378/)

1. Ensure dependencies are installed

```sh
$ pip install python-binance
```

2. Clone this repository or simply just download it

3. Create file name ``api_key.txt`` and input your API

```
#firstline = API Key
#secondline = API Secret
```

```
QWDOKQWOMDQOEMASSELAMATMWOEGFMOWMEGR
QWERGOWRGRONALDKOHZHENXIANWROEGMNOWEM
```

4. Navigate to folder directory using CMD and type

```sh
$ python bot.py
```

# Instructions

## IMPORTANT NOTE

- Ensure that you change ``trade.py`` to ``create_test_order`` instead of ``create_order`` to test beforehand

## Steps

- This script will ask you for 4 inputs
1. Percentage of BTC you wanna trade
2. Percentage of Profit you earn before bot helps you to sell
3. Percentage of Loss you made before bot helps you to sell
4. Enter Alternative Coin (eg. if ADABTC is what you want, enter ADA)
