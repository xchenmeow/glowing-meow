
r = float(raw_input('rate?'))
n = int(raw_input('number of pmt?'))
pmt = float(raw_input('pmt?'))
fv = float(raw_input('fv?'))
cpmt = pmt / (1+r) * (1 - 1 / (1+r)**n) / (1 - 1/(1+r))
pv = cpmt + fv / (1+r)**n
print pv