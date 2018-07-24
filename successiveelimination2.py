import random
import math

mr = [0.12, 0.23, 0.34, 0.45, 0.56, 0.67, 0.78, 0.87, 0.89, 0.51]  # Mean reward of each arm during exploration
N = 10
ar = []
U = []
L = []
for x in range(N):
    ar.append(1)
    U.append(0.0)
    L.append(0.0)
flag = N
T = 0
a = 0
op = 0
while flag > 1:
    a = 0
    for a in range(N):
        if ar[a] == 0:
            continue
        T = T + 1
        u = random.normalvariate(mr[a], 0.1)
        r = math.sqrt((2 * math.log(T)) / T)
        U[a] = u + r
        L[a] = u - r
    for z in range(N):
        if ar[z] == 0:
            continue
        for y in range(N):
            if ar[y] == 0 or z == y:
                continue
            if U[z] < L[y] and ar[z] != 0 and ar[y] != 0:
                print("Arm No.", z + 1, " inactive")
                ar[z] = 0
                U[z] = 0.0
                L[z] = 0.0
                flag -= 1
                op = y
            y += 1
        z += 1
print("Final state of arms ", ar)
print("UCB of best arm is ", U[op])
print("LCB of best arm is ", L[op])
print("Best arm is Arm No.", op + 1)
