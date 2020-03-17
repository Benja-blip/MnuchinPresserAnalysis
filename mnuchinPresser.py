import mysql.connector
from mysql.connector import Error as err


def mnuchinPresser():

    cnx = mysql.connector.connect(user='user', password='password', host='127.0.0.1', database='StockPipeline')
    cnx.connect()
    cursor = cnx.cursor()

    print('')
    print('***************************The weak***************************')
    print('')

    cursor.execute(
        "SELECT * FROM `1pmStocks` t1 WHERE NOT EXISTS (SELECT t2.symbol FROM `11amStocks` t2 WHERE t1.symbol = t2.symbol)")
    the_weak_sql = cursor.fetchall()
    the_weak_list = []
    for row in the_weak_sql:
        the_weak_list.append(row[0])

    print(the_weak_list)

    print('')
    print('***************************The strong***************************')
    print('')

    cursor.execute("SELECT * FROM 11amStocks JOIN 1pmStocks ON 11amStocks.symbol = 1pmStocks.symbol")
    the_strong_sql = cursor.fetchall()
    the_strong_list = []
    for row in the_strong_sql:
        the_strong_list.append(row[0])

    print(the_strong_list)

    print('')
    print('***************************The strange***************************')
    print('')

    cursor.execute(
        "SELECT * FROM `11amStocks` t1 WHERE NOT EXISTS (SELECT t2.symbol FROM `1pmStocks` t2 WHERE t1.symbol = t2.symbol)")
    the_strange_sql = cursor.fetchall()
    the_strange_list = []
    for row in the_strange_sql:
        the_strange_list.append(row[0])

    print(the_strange_list)


mnuchinPresser()
