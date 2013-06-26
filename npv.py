from math import pow

def NPV(arg):
	r = arg[0]
	arg.remove(arg[0])
	value = arg
	pv = 0
	for i in range(len(value)):
		pv = pv + value[i] / pow(1+r,i+1)
	return pv

arg = [0.05, 100, 100, 100]
pv = NPV(arg)
print pv