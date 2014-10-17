import pandas as pd
import pandas.io.data as web
import datetime


def backtest_series(positions, historic):
    '''
    both inputs are pandas Series.
    returns account value Series
    '''
    return positions * historic


if __name__ == '__main__':
    # start date and end time
    start_date = datetime.datetime(2014, 10, 1)
    end_date = datetime.datetime(2014, 10, 17)

    # prepare position data and historic data
    positions_date_range = pd.date_range('2014-10-01', '2014-10-17')
    positions = pd.Series(100, index=positions_date_range)

    yahoo_data = web.DataReader('SPY', 'yahoo', start_date, end_date)
    historic_close = yahoo_data.Close

    result = backtest_series(positions, historic_close)