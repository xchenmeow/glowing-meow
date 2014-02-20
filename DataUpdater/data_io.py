import pandas as pd


def from_ymdv_csv(path):
	return pd.DataFrame.from_csv(path, header=0, index_col=[0, 1, 2], parse_dates=False)


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