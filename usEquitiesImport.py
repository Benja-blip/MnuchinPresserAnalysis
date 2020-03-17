import alpaca_trade_api as tradeapi
import mysql.connector
from mysql.connector import Error as err


chosen_ones = []

def get_tickers():

    base_url = 'https://paper-api.alpaca.markets'
    api_key_id = 'API_KEY'
    api_secret = 'SECRET_KEY'

    api = tradeapi.REST(
        base_url=base_url,
        key_id=api_key_id,
        secret_key=api_secret
    )

    min_share_price = 5
    max_share_price = 15

    print('Getting current ticker data...')
    tickers = api.polygon.all_tickers()
    print('Success.')
    assets = api.list_assets()
    symbols = [asset.symbol for asset in assets if asset.tradable]
    for ticker in tickers:
        if (ticker.ticker in symbols and
            ticker.lastTrade['p'] >= min_share_price and
            ticker.lastTrade['p'] <= max_share_price and
            ticker.todaysChangePerc >= 1.0
            ):
            chosen_ones.append(ticker)
        else:
            pass

    database_insert()


def database_insert():

    cnx = mysql.connector.connect(user='user', password='password', host='127.0.0.1', database='StockPipeline')
    cnx.connect()
    cursor = cnx.cursor()

    try:
        cursor.execute("CREATE TABLE 1pmStocks (symbol CHAR(5) NOT NULL, prevDayClose DECIMAL(6,4) NOT NULL, prevDayHigh DECIMAL(6,4) NOT NULL, prevDayLow DECIMAL(6,4) NOT NULL, lastTrade DECIMAL(6,4) NOT NULL, todaysChangePerc DECIMAL(6,4) NOT NULL);")
        print("created")
    except err:
        print("err")

    print(chosen_ones)
    print(len(chosen_ones))

    for ticker in chosen_ones:
        print(ticker.ticker)
        print(ticker.prevDay['c'])
        value = (ticker.ticker, ticker.prevDay['c'], ticker.prevDay['h'], ticker.prevDay['l'], ticker.lastTrade['p'],
                ticker.todaysChangePerc)
        query = 'INSERT INTO 1pmStocks (symbol, prevDayClose, prevDayHigh, prevDayLow, lastTrade, todaysChangePerc) VALUES (%s, %s, %s, %s, %s, %s)'
        try:
            cursor.execute(query, value)
            print("db appended")
            print(value)
        except ValueError:
            print(value)
            print("Value error")

    cnx.commit()


get_tickers()
