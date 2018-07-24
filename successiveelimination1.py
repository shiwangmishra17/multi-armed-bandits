import random
import math

mr = [0.55, 0.62]  # Mean reward of each arm during exploration
T = 0
u1 = 0.0
u2 = 0.0
while 1:
    for x in range(2):
        u1 = (u1 * T + random.normalvariate(mr[0], 0.2)) / (T + 1)
        u2 = (u2 * T + random.normalvariate(mr[1], 0.2)) / (T + 1)
        T += 1
    r = math.sqrt((2 * math.log(T)) / T)
    U1 = u1 + r
    L1 = u1 - r
    U2 = u2 + r
    L2 = u2 - r
    print(U1, L2)
    print(U2, L1)
    if U1 < L2 and U2 >= L1:
        print("Arm 2 is better.")
        break
    elif U2 < L1 and U1 >= L2:
        print("Arm 1 is better.")
        break
