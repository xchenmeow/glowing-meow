import pandas as pd
import math

roll_file = '^GSPC_roll.csv'
attr_name = 'Sigma'

# read from ugarchroll result file
roll_df = pd.DataFrame.from_csv(roll_file)

# time series of given attribute
ts = roll_df[attr_name]

# ts_file = '^GSPC_sigma.csv'
# ts.to_csv(ts_file, header=True, index_label='Date')

vol_15_weight = make_simple_weight(0.15 / math.sqrt(252))
vol_10_weight = make_simple_weight(0.10 / math.sqrt(252))

# weights = roll_df['Sigma'].map(vol_10_weight)
roll_df['weights'] = roll_df['Sigma'].map(vol_10_weight)

roll_df["Strategy"] = roll_df['weights'] * roll_df['Realized']

strat_level_ts = timeseries_return_to_level(roll_df['Strategy'])
unprot_level_ts = timeseries_return_to_level(roll_df['Realized'])
ts_comp = pd.concat([strat_level_ts, unprot_level_ts], axis=1)
