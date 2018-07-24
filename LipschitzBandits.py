import math
import random
import matplotlib.pyplot as plt

mr = [0.12, 0.23, 0.34, 0.45, 0.56, 0.67, 0.78, 0.87, 0.89, 0.51]  # Mean reward of each arm during exploration
T = 2000
K = 10  # Number of arms
maxindex = 0.0
rew = 0.0
a = b = o = 0
st = []
index = []
u = []
rt = []
n = []
time = []
play = []

for x in range(K):
    st.append(0)
    u.append(0.0)
    n.append(0)
    rt.append(2 * math.log(T) / (n[x] + 1))
    index.append(2 * rt[x])

for x in range(T):
    time.append(x + 1)
    for a in range(K):
        if x is 0:
            o = random.randint(0, 9)
            print("Arm number ", o + 1, "activated.")
            maxindex = 2 * rt[o]
            st[o] = 1
            break
        if st[a] == 0:
            continue
        for b in range(K):
            if st[b] == 1:
                continue
            if rt[a] <= (math.fabs(mr[a] - mr[b])):
                st[b] = 1
                print("Arm number ", b + 1, "activated.")
                break
        if st[b] == 1:
            break

    for y in range(K):
        if st[y] == 0:
            continue
        if maxindex < index[y]:
            maxindex = index[y]
            o = y
    print("Arm number ", o + 1, "played.")
    v = random.normalvariate(mr[o], 0.01)
    play.append(v)
    rew += v
    u[o] = (u[o] * T + v) / (T + 1)
    n[o] += 1
    rt[o] = 2 * math.log(T) / (n[o] + 1)
    index[o] = u[o] + 2 * rt[o]
    maxindex = index[o]

print("Total Reward =", rew)

plt.plot(time, play)

# naming the x axis
plt.xlabel('Time')
# naming the y axis
plt.ylabel('Reward')

# giving a title to my graph
plt.title('Lipschitz Bandit')

# function to show the plot
plt.show()
