import pandas as pd


def read_ymdv_csv(path):
	'''
	read <data>.csv in the format of:
	year, month, day, value
	return a DataFrame
	'''
	date_spec = {'date' : [0, 1, 2]}
	# todo: DataFrame or DataFrame? Which is better?
	return pd.DataFrame.from_csv(path, header=0, parse_dates=date_spec)

# todo: CD to working directory.
equity_indices = ['spx', 'rty', 'mxef', 'mxea', 'mid']
bond_indices = ['lbustruu', 'mm']
# Note: bond index and mm index miss some data
# To avoid problem, intersect the equity indices first
# then fill the bond indices.
def merge_equity_indices(indices, currency='usd', join='inner'):
	index_df_list = [read_ymdv_csv(f) for f in 
		['_'.join([currency, ind]) + '.csv' for ind in indices]]
	return pd.concat(index_df_list, axis=1, join=join)

idx_df = merge_equity_indices(equity_indices)
bond_df_list = [read_ymdv_csv(f) for f in 
		['_'.join(['usd', ind]) + '.csv' for ind in bond_indices]]
all_idx_df = idx_df.join(bond_df_list[0]).join(bond_df_list[1])
all_idx_df = all_idx_df.interpolate(method='time')


fund_codes = ['101', '102', '103', '104', '105', '106', '107', '150', '151', '152', '153']
def merge_funds(fund_codes, join='inner'):
	fund_df_list = [read_ymdv_csv(f) for f in 
		['_'.join(['fund', code]) + '.csv' for code in fund_codes]]
	return pd.concat(fund_df_list, axis=1, join=join)

funds_df = merge_funds(fund_codes)


fund_map_file = 'C:\\bshen\\Indices\\fundMap.csv'
def read_fund_map(map_file):
	date_spec = {'date' : [0, 1, 2]}
	# todo: DataFrame or DataFrame? Which is better?
	return pd.DataFrame.from_csv(map_file, header=0,
		parse_dates=date_spec, index_col=['date', 'Fund Code'])

fund_map_df = read_fund_map(fund_map_file)

def get_one_latest_map(df, code):
	'''
	input:
	map data frame
	code is INTEGER
	return:
	map for this fund in DataFrame
	'''
	return df.swaplevel(0, 1).ix[code].tail(1)


code = '101'
latest_map = get_one_latest_map(fund_map_df, int(code))

orig_fund_levels = read_ymdv_csv('_'.join(['fund', code]) + '.csv')
sliced = orig_fund_levels.loc[all_idx_df.index].dropna()
first_date = sliced.index[0]
first_value = sliced.values[0, 0]

bfill_idx_df = all_idx_df[:first_date]

bfill_index = bfill_idx_df.index
bfill_map_df = pd.DataFrame(data=map(list, latest_map.values), index=bfill_index)
bfill_map_df.columns = all_idx_df.columns

bfill_idx_returns = bfill_idx_df.pct_change()
bfill_fund_returns = (bfill_idx_returns * bfill_map_df).sum(axis=1)
bfill_fund_levels = timeseries_return_to_level_bfill(
	bfill_fund_returns, first_date, first_value)
# todo: column name ad hoc
bfill_fund_levels_df = bfill_fund_levels.to_frame(code + 'Level')

df = pd.concat([bfill_fund_levels_df, sliced[1:]])


def backfill_one_fund(code, fund_map_df, all_idx_df):
	'''
	code: string
	fund_map_df: DataFrame of fund map history
	all_idx_df: DataFrame of all indices
	'''
	latest_map = get_one_latest_map(fund_map_df, int(code))

	orig_fund_levels = read_ymdv_csv('_'.join(['fund', code]) + '.csv')
	sliced = orig_fund_levels.loc[all_idx_df.index].dropna()
	first_date = sliced.index[0]
	first_value = sliced.values[0, 0]

	bfill_idx_df = all_idx_df[:first_date]

	bfill_index = bfill_idx_df.index
	bfill_map_df = pd.DataFrame(data=map(list, latest_map.values), index=bfill_index)
	bfill_map_df.columns = all_idx_df.columns

	bfill_idx_returns = bfill_idx_df.pct_change()
	bfill_fund_returns = (bfill_idx_returns * bfill_map_df).sum(axis=1)
	bfill_fund_levels = timeseries_return_to_level_bfill(
		bfill_fund_returns, first_date, first_value)
	# todo: column name ad hoc
	bfill_fund_levels_df = bfill_fund_levels.to_frame(code + ' Level')

	df = pd.concat([bfill_fund_levels_df, sliced[1:]])
	return df


def ymdv_2_monthly_return(df, months, return_type='simple'):
	if return_type != 'simple':
		raise NotImplemented

	# Convert to capitalized
	df.index.names = [s.capitalize() for s in df.index.names]

	gdf = df.groupby(level=['Year', 'Month'])
	ymv = gdf.last()
	month_end_levels = ymv.tail(months + 1)
	monthly_returns = month_end_levels.pct_change()
	return monthly_returns[1:]