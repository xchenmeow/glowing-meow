from scipy.optimize import fsolve
import math

def FutureValue(arg):
  r = arg[0]
	n = arg[1]
	pmt = arg[2]
	if len(arg) < 4:
		pv = 0
	else:
		pv = arg[3]
	cpmt = pmt * (1+r) * (1 - (1+r)**n) / (1 - (1+r))
	fv = cpmt + pv * (1+r)**n
	return fv
fvPara = [0.05, 5, 100, 100]
# rate, nper, pmt, pv(optional)
 
fv = FutureValue(fvPara)
print fv


def PresentValue(arg):
	r = arg[0]
	n = arg[1]
	pmt = arg[2]
	if len(arg) < 4:
		fv = 0
	else:
		fv = arg[3]
	cpmt = pmt / (1+r) * (1 - 1 / (1+r)**n) / (1 - 1/(1+r))
	pv = cpmt + fv / (1+r)**n
	return pv
pvPara = [0.05, 5, 100, 100]
# rate, nper, pmt, fv(optional)

pv = PresentValue(pvPara)
print pv



def funcPV(r, n, pmt, pv, fv):
	cpmt = pmt / (1+r) * (1 - 1/(1+r)**n) / (1 - 1/(1+r))
	presentv = cpmt + fv / (1+r)**n
	return presentv - pv

def Rate(arg):
	nper = arg[0]
	pmt = -arg[1]
	pv = arg[2]
	if len(arg) == 4:
		fv = arg[3]
	else:
		fv = 0
	rate = fsolve(funcPV, 0.01, args = (nper, pmt, pv, fv))
	return rate[0]

ratePara = [48, -200, 8000]
# nper, pmt, pv, fv(optional)


rate =  Rate(ratePara)
print rate


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
