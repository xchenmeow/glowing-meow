__author__ = 'benqing.shen'

import csv
import sqlite3
import datetime


def csv2db(csvfile, conn, symbol, header=True, table_name='stocks', inputformat='yahoo'):
    if inputformat != 'yahoo':
        raise NotImplementedError

    time_series = []

    with open(csvfile) as csvfile:
        datareader = csv.reader(csvfile)

        if header:
            next(datareader)

        for row in datareader:
            time_series.append((symbol, row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

    c = conn.cursor()

    time_series.reverse()
    num_of_records = len(time_series)

    c.execute("""
        CREATE TABLE if not exists %s (
            symbol text,
            date text,
            open real,
            high real,
            low real,
            close real,
            volume real,
            price real,
            PRIMARY KEY (symbol, date))
        """ %table_name)

    c.executemany('INSERT INTO ' + table_name + ' VALUES (?,?,?,?,?,?,?,?)',
                  time_series[0: num_of_records])
    

def update_db_with_csv(csvfile, symbol, start_date='2014-01-13', header=True, sqlite_file='data.db',
                       table_name='stocks', inputformat='yahoo'):
    if inputformat != 'yahoo':
        raise NotImplementedError

    d = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    # print type(d)
    # print d

    time_series = []

    with open(csvfile) as csvfile:
        datareader = csv.reader(csvfile)

        if header:
            # skip the header
            next(datareader)

        for row in datareader:
            date_str = row[0]
            this_date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
            if this_date >= d:
                time_series.append((symbol, row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

    # print time_series
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    time_series.reverse()
    num_of_records = len(time_series)
    c.executemany('INSERT INTO ' + table_name + ' VALUES (?,?,?,?,?,?,?,?)',
                  time_series[0: num_of_records])

    conn.commit()
    conn.close()


if __name__ == '__main__':
    # csv2db('table.csv', 'spx')

    try:
        #update_db_with_csv('table.csv', 'spx', start_date='2000-01-01')
        # *** todo: change the call params ***
        # csv2db('HYG.csv', 'HYG')
    except sqlite3.IntegrityError:
        print 'The primary key exists.'