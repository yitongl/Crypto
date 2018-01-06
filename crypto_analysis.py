from coinmarketcap import Market
import pandas as pd
from time import sleep

# Show all columns on one line when printing
pd.set_option('display.width', 1000)
coinmarketcap = Market()

while True:
    all_currencies = coinmarketcap.ticker()

    df = pd.DataFrame(all_currencies)
    df = df.convert_objects(convert_numeric=True)

    sorted_1h = df.sort_values(by = ['percent_change_1h'], ascending=False)

    
    print('------------------------------------------------------------------------------------')
    print('Most increase in value during the last hour')
    print(sorted_1h.head(10)[['symbol', 'price_usd', 'percent_change_1h', 'percent_change_24h', 'percent_change_7d']])
    print('------------------------------------------------------------------------------------')
    print('Most decrease in value during the last hour')
    print(sorted_1h.tail(10)[['symbol', 'price_usd', 'percent_change_1h', 'percent_change_24h', 'percent_change_7d']])
    print('------------------------------------------------------------------------------------')
    sleep(300)
