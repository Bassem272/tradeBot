import json
import os
import binance_connect
import strategy

import_path = "settings.json"
output_path = "output.json"

# import settings
def get_settings(import_path):
    # ensure the path exists
    if os.path.exists(import_path):
        file = open(import_path, "r")
        project_settings = json.load(file)
        file.close()
        return project_settings
    else:
        return ImportError
    

if __name__ == "__main__":
    project_settings = get_settings(import_path)
    api_key = project_settings['Binance_keys']['api_key']
    secret_key = project_settings['Binance_keys']['secret_key']

    account = binance_connect.query_account(api_key, secret_key)
    # print(account)
    if os.path.exists(output_path):
        with open(output_path, "w") as file:
            json.dump(account, file)

    candleData = binance_connect.get_candleSticks_data('ETHBTC','1h',5)
    # print(candleData)

    symbol_list = binance_connect.get_symbol_list("BTC")
    print(symbol_list)
    # status = binance_connect.query_binance_status()
    # print(status)

    # testnet = binance_connect.query_testnet()
    # print(testnet)
