def ChairsSurvival(N):
	chairs = []
	for i in range(0,N):
		chairs.append(1)
	flag = True
	while True:
		for i in range(0,100):
			if flag and chairs[i] == 1:
				chairs[i] = 0
				flag = False
				continue
			elif (not flag) and chairs[i] == 1:
				flag = True
			else:
				continue
		if chairs.count(1) == 1:
			break
	return chairs.index(1)

print ChairsSurvival(100)
