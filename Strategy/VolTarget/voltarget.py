# import math from parent directory
import pandas as pd


symbols = ['^GSPC', 'AGG']
roll_files = [s + '_roll.csv' for s in symbols]
# print roll_files
vol_target = 0.12


roll_dfs = [pd.DataFrame.from_csv(f) for f in roll_files]
# print roll_dfs[0][['Sigma', 'Realized']]
sigma_realized_dfs = [df[['Sigma', 'Realized']] for df in roll_dfs]
# print sigma_realized_dfs[0]

sigma_df = pd.concat([roll_dfs[0]['Sigma'], roll_dfs[1]['Sigma']], axis=1)
returns_df = pd.concat([roll_dfs[0]['Realized'], roll_dfs[1]['Realized']], axis=1)
vol_x_weight = make_two_independent_weights(vol_target / math.sqrt(252))
weight1_ts = sigma_df.apply(vol_x_weight, axis=1)
weight1_ts = weight1_ts.fillna(value=0)
weight2_ts = weight1_ts.apply(lambda x: (1 - x) if (x > 0) else 0)

portfolio_return_ts = returns_df.ix[:, 0] * weight1_ts + returns_df.ix[:, 0] * weight2_ts

portfolio_return_ts = portfolio_return_ts.fillna(method='bfill')

strat_level_ts = timeseries_return_to_level(portfolio_return_ts)
unprot_level_ts = timeseries_return_to_level(returns_df.ix[:, 0])

ts_comp = pd.concat([strat_level_ts, unprot_level_ts], axis=1)


symbols = ['^GSPC']
roll_files = [s + '_roll.csv' for s in symbols]
# print roll_files
vol_target = 0.12

roll_dfs = [pd.DataFrame.from_csv(f) for f in roll_files]
# print roll_dfs[0][['Sigma', 'Realized']]
sigma_realized_dfs = [df[['Sigma', 'Realized']] for df in roll_dfs]
# print sigma_realized_dfs[0]

sigma_df = pd.concat([roll_dfs[0]['Sigma']], axis=1)
returns_df = pd.concat([roll_dfs[0]['Realized']], axis=1)
vol_x_weight = make_simple_weight(vol_target / math.sqrt(252))
weight1_ts = sigma_df.applymap(vol_x_weight)
weight1_ts = weight1_ts.fillna(value=0)
# weight2_ts = weight1_ts.apply(lambda x: (1 - x) if (x > 0) else 0)

portfolio_return_ts = returns_df.ix[:, 0] * weight1_ts# + returns_df.ix[:, 0] * weight2_ts

portfolio_return_ts = portfolio_return_ts.fillna(method='bfill')

strat_level_ts = timeseries_return_to_level(portfolio_return_ts)
unprot_level_ts = timeseries_return_to_level(returns_df.ix[:, 0])

# ts_comp = pd.concat([strat_level_ts, unprot_level_ts], axis=1)
