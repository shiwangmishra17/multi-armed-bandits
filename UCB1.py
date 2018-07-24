import random
import math
import matplotlib.pyplot as plt

mr = [0.12, 0.23, 0.34, 0.45, 0.56, 0.67, 0.78, 0.87, 0.89, 0.51]  # Mean reward of each arm during exploration
N = 10
T = 100
u = []
U = []
t = 0
ta = []
rew = 0.0
umax = 0
x = 0
o = 0
x1 = []
y1 = []
for x in range(N):
    u.append(0.0)
    U.append(0.0)
    ta.append(0)
    t += 1
    x1.append(t)
    ta[x] += 1
    u[x] = random.normalvariate(mr[x], 0.1)
    rew += u[x]
    r = math.sqrt((2 * math.log(t)) / (ta[x] + 1))
    U[x] = u[x] + r
    y1.append(U[x])
    if x is 0:
        o = 0
        umax = U[x]
    if U[x] > umax:
        o = x
        umax = U[x]
while t != T:
    t += 1
    x1.append(t)
    print("Arm no. ", o + 1, " repeated.")
    r = random.normalvariate(mr[x], 0.1)
    rew += r
    u[o] = ((u[o] * ta[o]) + r) / (ta[o] + 1)
    ta[o] += 1
    r = math.sqrt((2 * math.log(t)) / ta[o])
    U[o] = u[o] + r
    y1.append(U[o])
    o = 0
    umax = U[0]
    for x in range(N - 1):
        if U[x + 1] > umax:
            o = x + 1
            umax = U[x + 1]
print("Total Reward = ", rew)
print(U)

plt.plot(x1, y1)

# naming the x axis
plt.xlabel('Time')
# naming the y axis
plt.ylabel('UCB(Max)')

# giving a title to my graph
plt.title('Trend in UCB1')

# function to show the plot
plt.show()