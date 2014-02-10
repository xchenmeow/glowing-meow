import csv

resource = 'screener_results.csv'



with open(resource, 'rb') as csvfile, open('symbols.csv', 'wb') as symbol_file:
	 symbols_reader = csv.reader(csvfile)
	 # help here.
	 symbols_writer = csv.writer(symbol_file)
	 for row in symbols_reader:
	 	symbols_writer.writerow([row[1]])
