import pandas as pd
import pandas.io.data as web
import numpy as np
import datetime


def backtest_series(positions, historic):
    '''
    both inputs are pandas Series.
    returns account value Series
    '''
    return positions * historic


def backtest_dataframe(positions, historic):
    '''
    both inputs are pandas DataFrame.
    returns account value DataFrame
    '''
    return positions * historic


def backtest(positions):
    '''
    takes positions
    automatically prepare data
    returns value DataFrame
    '''
    investments = [name for name in positions.columns]
    start_date = positions.index[0]
    end_date = positions.index[-1]
    yahoo_data = web.DataReader(investments, 'yahoo', start_date, end_date)
    historic_close = yahoo_data['Adj Close']

    return positions * historic_close


def validate_positions(positions):
    '''
    positions should be a pandas DataFrame
    positions should be indexed by datetime
    positions should have columns which are investments
    positions should have positive values???
    '''
    pass

def random_postion(date_range, min_postion=0, max_postion=100):
    '''
    take a date range and returns randome positions
    '''
    date_range_length = date_range.size
    return pd.Series(np.random.randint(min_postion, max_postion, size=date_range_length), index=date_range)


def buy_and_hold_postion(date_range, investments, init_account=10000.0, weighting=None):
    '''
    On start_date
    returns positions
    '''

    # Be careful. investments have to be list and sorted.
    investments.sort()

    start_date = date_range[0]
    end_date = date_range[-1]
    yahoo_data = web.DataReader(investments, 'yahoo', start_date, end_date)
    historic_close = yahoo_data['Adj Close']
    if weighting == None:
        init_allocation = [init_account / len(investments) for i in investments]
        init_position = init_allocation / historic_close.ix[0, ].values
        series_list = [pd.Series(pos, index=date_range) for pos in init_position]
        # return (init_position, pd.DataFrame(init_position, index=date_range))
        df = pd.concat(series_list, axis = 1)
        df.columns = investments
        return df
    else:
        # weighting list must add to 1
        pass


def constant_weighting_position(date_range, investments, init_account=10000.0, weighting=None):
    '''
    60-40
    adjust everyday.
    '''
    # todo: sort with weighting.
    investments.sort()

    start_date = date_range[0]
    end_date = date_range[-1]
    yahoo_data = web.DataReader(investments, 'yahoo', start_date, end_date)
    historic_close = yahoo_data['Adj Close']
    if weighting == None:
        init_allocation = [init_account / len(investments) for i in investments]
        init_position = init_allocation / historic_close.ix[0, ].values
        # todo
        series_list = [pd.Series(pos, index=date_range) for pos in init_position]
        # return (init_position, pd.DataFrame(init_position, index=date_range))
        df = pd.concat(series_list, axis = 1)
        df.columns = investments
        return df
    else:
        constant_allocation = [init_account * w for w in weighting]
        # return constant_allocation
        positions = constant_allocation / historic_close
        return positions



if __name__ == '__main__':
    # start date and end time
    start_date = datetime.datetime(2004, 1, 2)
    end_date = datetime.datetime(2014, 10, 17)

    # prepare position data and historic data
    positions_date_range = pd.date_range(start_date, end_date)
    positions = pd.Series(100, index=positions_date_range)
    
    # A future warning here.
    positions_frame = pd.DataFrame(50, index=positions_date_range, columns=['SPY', 'IVV'])


    yahoo_data = web.DataReader('SPY', 'yahoo', start_date, end_date)
    historic_close = yahoo_data.Close

    # A Panel.
    yahoo_data2 = web.DataReader(['SPY', 'IVV'], 'yahoo', start_date, end_date)
    # A DataFrame
    historic_close2 = yahoo_data2.Close

    result = backtest_series(positions, historic_close)
    result2 = backtest_dataframe(positions_frame, historic_close2)