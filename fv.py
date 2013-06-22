import sys
sys.argv
# A useful terminology here is called "unpack"

# define a function
# http://docs.python.org/2.7/tutorial/controlflow.html#defining-functions
def FutureValue(r, n, pmt, fv):
	cpmt = pmt * (1+r) * (1 - (1+r)**n) / (1 - (1+r))
	fv = cpmt + pv * (1+r)**n
	return fv

rate = float(sys.argv[1])
nper = int(sys.argv[2])
pmt = float(sys.argv[3])
pv = float(sys.argv[4])
# Then run the function
fv = FutureValue(rate, nper, pmt, pv)
print fv
