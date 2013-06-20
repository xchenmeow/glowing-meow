import math


def NPer(arg):
  r = arg[0]
	pmt = -arg[1]
	pv = arg[2]
	if len(arg) < 4:
		fv = 0
	else:
		fv = arg[3]
	n = math.log((pmt/r - fv) / (pmt/r -pv)) / math.log(1+r)
	return n
NperPara = [0.0525, -200, 1500]
# rate, nper, pmt, pv(optional)
 
nper = NPer(NperPara)
print nper
