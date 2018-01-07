from coinmarketcap import Market
import pandas as pd
from time import sleep
import subprocess

# Show all columns on one line when printing
pd.set_option('display.width', 1000)
coinmarketcap = Market()

has_pinged = []

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
    
    
    increase_10pct = sorted_1h[sorted_1h['percent_change_1h'] > 10.0]['symbol'].values
    
    for value in increase_10pct:
        if value not in has_pinged:
            subprocess.call(['afplay', '/System/Library/Sounds/Ping.aiff'])            
            print (value)
    
    has_pinged.extend(increase_10pct)

    sleep(300)