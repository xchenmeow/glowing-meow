# this function calculates all the combination of weights
# n is the number of stocks
# [w1,w2,...,wn] is the weight vector of stocks
# 0 <= wi < 1 and the sum of wi is 1
# this function will print the number of combination on console

import csv
def CalWeightList(n):
	number = pow(10,n)
	a = []
	weightlist = []
	for item in range(0,number):
		temp = item
		while True:		
			if temp < 10:
				a.append(temp)
				templist = a
				a = []
				break
			a.append(temp%10)
			temp /= 10		
		if sum(templist) == 10:
			weightlist.append(templist)
	print len(weightlist)
	f = open('weightlist2.csv','w')
	for item in weightlist:
		if len(item)<n:
			b = item + [0]*(n-len(item))
		else:
			b = item
		c = [i/10.0 for i in b]
		foo = csv.writer(f,delimiter = ',')
		foo.writerow(c)
	f.close()

CalWeightList(4)