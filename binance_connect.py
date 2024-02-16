# binance.py
from binance.spot import Spot  # Import Spot locally

import pandas

# Function to get the status
def query_binance_status():
    status = Spot().system_status()
    if status["status"] == 0:
        return True
    else:
        raise ConnectionError

# Function query account
def query_account(api_key, secret_key):
    return Spot(
        api_key=api_key,
        api_secret=secret_key,
        base_url="https://testnet.binance.vision",
    ).account()

# query testnet
def query_testnet():
    client = Spot(base_url="https://testnet.binance.vision")
    print(client.time())

# query candle data
def get_candleSticks_data(symbol, timeFrame, qty):
    data = Spot().klines(symbol=symbol, interval=timeFrame, limit=qty)
    df = pandas.DataFrame(data)
    converted_data = []
    for candle in data:
        converted_candle = {
            "time": candle[0],
            "open": float(candle[1]),
            "high": float(candle[2]),
            "low": float(candle[3]),
            "close": float(candle[4]),
            "volume": float(candle[5]),
            "close_time": candle[6],
            "quote_asset_volume": float(candle[7]),
            "number_of_trades": int(candle[8]),
            "taker_buy_base_asset_volume": float(candle[9]),
            "taker_buy_quote_asset_volume": float(candle[10]),
        }  
        converted_data.append(converted_candle)
        return converted_data
# get list of available assets for trading 
def get_symbol_list(symbol): 
    symbol_dict = Spot().exchange_info()
    symbol_dataFrame = pandas.DataFrame(symbol_dict["symbols"])
    symbol_dataFrame = symbol_dataFrame.loc[
        (symbol_dataFrame["quoteAsset"] == symbol) & (symbol_dataFrame["status"] == "TRADING")
    ] 
    return symbol_dataFrame

# trade with params
def trade_with_params(params,project_settings):
    apiKey = project_settings["Binance_Keys"]["api_key"]
    secretKey = project_settings["Binance_Keys"]["secret_key"]
    client = Spot(
        api_key=apiKey,
        secret_key=secretKey,
        base_url="https://testnet.binance.vision",
    )

    try:
        response = client.new_order(**params)
        return response
    except ConnectionRefusedError as error:
        print(f"Error : {error}")    

# get open trades
def get_trades( project_settings):
    apiKey = project_settings["Binance_Keys"]["api_key"]
    secretKey = project_settings["Binance_Keys"]["secret_key"]
    client = Spot(
        api_key=apiKey,
        secret_key=secretKey,
        base_url="https://testnet.binance.vision",
    ) 
    #get trades open orders
    try:
        response = client.get_open_orders()
        return response
    except ConnectionRefusedError as error:
        print(f"Error : {error}")

# cancel a trade 
def cancel_trade_with_symbol(symbol, project_settings):
    apiKey = project_settings["Binance_Keys"]["api_key"]
    secretKey = project_settings["Binance_Keys"]["secret_key"]
    client = Spot(
        api_key=apiKey,
        secret_key=secretKey,
        base_url="https://testnet.binance.vision",
    )
# cancel trade 
    try: 
        response = client.cancel_order(symbol=symbol)
        return response
    except ConnectionRefusedError as error:
        print(f"Error : {error}")

# function to place a limit for symbol
def place_limit_order(symbol,side,quantity,price,project_settings):
    apiKey = project_settings["Binance_Keys"]["api_key"]
    secretKey = project_settings["Binance_Keys"]["secret_key"]
    client = Spot(
        api_key=apiKey,
        secret_key=secretKey,
        base_url="https://testnet.binance.vision",
    )

# place a a limit order for symbol
    try:
        response = client.new_order(
            symbol=symbol,
            side=side,
            type='LIMIT',
            timeInForce='GTC',
            quantity=quantity,
            price=price
        )
        return response
    except ConnectionRefusedError as error:
        print(f"Error : {error}")

# function to place stop loss 
def place_stop_loss_order(symbol,side,quantity,stop_price,limit_price,project_settings):
    apiKey = project_settings["Binance_Keys"]["api_key"]
    secretKey = project_settings["Binance_Keys"]["secret_key"]
    client = Spot(
        api_key=apiKey,
        secret_key=secretKey,
        base_url="https://testnet.binance.vision",
    )
# place a stop loss order
    try:
        response = client.new_order(
            symbol=symbol,
            side=side,
            type='STOP_LOSS_LIMIT',
            timeInForce='GTC',
            quantity=quantity,
            stopPrice=stop_price,
            price=limit_price
        )
        return response
    except ConnectionRefusedError as error:
        print(f"Error : {error}")        

# PLACE  take profit order 
def place_take_profit(
        symbol,side,quantity,stop_price,limit_price,project_settings
        ):
    apiKey = project_settings["Binance_Keys"]["api_key"]
    secretKey = project_settings["Binance_Keys"]["secret_key"]
    client = Spot(
        api_key=apiKey,
        secret_key=secretKey,
        base_url="https://testnet.binance.vision",
    )
# place a take profit order
    try:
        response = client.new_order(
            symbol=symbol,
            side=side, # side is buying or selling
            type='TAKE_PROFIT_LIMIT',
            timeInForce='GTC',
            quantity=quantity,
            stopPrice=stop_price,
            price=limit_price
        )
        return response
    except ConnectionRefusedError as error:
        print(f"Error : {error}")                     