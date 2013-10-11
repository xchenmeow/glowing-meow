from scipy.optimize import fsolve
from sys import argv

def funcPV(r, n, pmt, pv, fv):
	cpmt = pmt / (1+r) * (1 - 1/(1+r)**n) / (1 - 1/(1+r))
	presentv = cpmt + fv / (1+r)**n
	return presentv - pv

n = int(argv[1])
pmt = float(argv[2])
pv = float(argv[3])
fv = float(argv[4])
rate = fsolve(funcPV, 0.01, args = (n, pmt, pv, fv))
print rate

