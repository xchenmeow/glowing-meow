def ChairsSurvival(N):
    chairs = []
    for i in range(0, N):
        chairs.append(1)
    flag = True
    while True:
        for i in range(0, N):
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

# print ChairsSurvival(1000000)

import time
elapseTime = []

for i in range(10000, 10001):
    # print i
    bgnTime = time.clock()
    print ChairsSurvival(i)
    endTime = time.clock()
    elapseTime.append(endTime - bgnTime)


print elapseTime