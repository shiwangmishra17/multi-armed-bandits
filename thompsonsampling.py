import random
import math
import matplotlib.pyplot as plt

mr = [0.12, 0.23, 0.34, 0.45, 0.56, 0.67, 0.78, 0.87, 0.89, 0.51]  # Mean reward of each arm during exploration
N = 10
u = []
S = []
F = []
z = []
v = []
rew = 0.0
C = math.pow(2.7128, 83)
T = 1000

for x in range(N):
    u.append(0.0)
    S.append(0)
    F.append(0)
    u[x] = C * math.pow(mr[x], S[x]) * math.pow(1 - mr[x], F[x])

o = random.randint(0, 9)
print("Arm number", o + 1, "being played.")
# u[0] = (S[0]+1)/(S[0]+F[0]+2)
umax = u[o]
r = random.normalvariate(mr[o], 0.001)
z.append(r)
v.append(1)
rew += r
c = random.random()
if r >= mr[o]:
    S[o] += 1
else:
    F[o] += 1
u[o] = C * math.pow(mr[o], S[o]) * math.pow(1 - mr[o], F[o])

for x in range(T - 1):
    for y in range(N):
        if u[y] >= umax:
            umax = u[y]
            o = y
        print("Arm number", o + 1, "being played.")
    r = random.normalvariate(mr[o], 0.001)
    z.append(r)
    v.append(x + 1)
    rew += r
    c = random.random()
    if r >= mr[o]:
        S[o] += 1
    else:
        F[o] += 1
    u[o] = C * math.pow(mr[o], S[o]) * math.pow(1 - mr[o], F[o])
    umax = u[o]

print("Total Reward =", rew)
print(u)
print("Success of arms =", S)
print("Failure of arms =", F)

plt.plot(v, z)

# naming the x axis
plt.xlabel('Time')
# naming the y axis
plt.ylabel('Reward')

# giving a title to my graph
plt.title('Thompson Sampling')

# function to show the plot
plt.show()
