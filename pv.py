# I recommend this:
import sys
sys.argv
# A useful terminology here is called "unpack"

r = float(raw_input('rate?'))
n = int(raw_input('number of pmt?'))
pmt = float(raw_input('pmt?'))
fv = float(raw_input('fv?'))
cpmt = pmt / (1+r) * (1 - 1 / (1+r)**n) / (1 - 1/(1+r))
pv = cpmt + fv / (1+r)**n
print pv

# define a function
# http://docs.python.org/2.7/tutorial/controlflow.html#defining-functions
def PresentValue(rate, nper, pmt, fv=0):
  # Your logic here
	pv = 0
	return pv

# Then run the function
pv = PresentValue(r, n, pmt, fv)
