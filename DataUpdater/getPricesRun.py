import pandasDataAccess
import sys
from datetime import datetime
from writer import csv2db
# todo: http://docs.python.org/2/library/argparse.html

# Interface now: start (2014-01-01), end, symbols file

if len(sys.argv) != 4:
	raise NotImplementedError

start_str = sys.argv[1]
start = datetime.strptime(start_str, '%Y-%m-%d')

end_str = sys.argv[2]
end = datetime.strptime(end_str, '%Y-%m-%d')

symbol_file = sys.argv[3]
symbol_list = []

with open(symbol_file, 'rb') as f:
	for line in f:
		symbol_list.append(line.rstrip())


if __name__ == '__main__':
	pandasDataAccess.get_all_prices(symbol_list, start, end)
	for i in xrange(len(symbol_list)):
		try:
			csv2db(symbol_list[i]+'.csv', symbol_list[i])
		except sqlite3.IntegrityError:
			print 'The primary key exists.'