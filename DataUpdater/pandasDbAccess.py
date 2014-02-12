import sqlite3
from pandas.io import sql


def pd_read_sql(db_path, indexes=None):
	conn = sqlite3.connect(db_path)

	df = sql.read_sql("SELECT * FROM stocks", conn, index_col=indexes)
	# df.set_index(indexes, inplace=True)
	conn.close()

	return df


if __name__ == '__main__':
	db_path = "..\\Database\\data.db"
	indexes = ['symbol', 'date']

	df = pd_read_sql(db_path, indexes)
	print df.head()
	print df.ix['ixic'].tail()