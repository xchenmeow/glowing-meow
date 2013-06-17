# I recommend this:
import sys
sys.argv
# A useful terminology here is called "unpack"

# define a function
# http://docs.python.org/2.7/tutorial/controlflow.html#defining-functions
def PresentValue(r, n, pmt, fv):
	cpmt = pmt / (1+r) * (1 - 1 / (1+r)**n) / (1 - 1/(1+r))
	pv = cpmt + fv / (1+r)**n
	return pv

rate = float(sys.argv[1])
nper = int(sys.argv[2])
pmt = float(sys.argv[3])
fv = float(sys.argv[4])
# Then run the function
pv = PresentValue(rate, nper, pmt, fv)
print pv
