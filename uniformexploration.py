import random
import matplotlib.pyplot as plt

N = 50  # Rate of exploration
K = 10  # Number of arms
mr = [0.12, 0.23, 0.34, 0.45, 0.56, 0.67, 0.78, 0.87, 0.89, 0.51]  # Mean reward of each arm during exploration
T = 100  # Number of subsequent rounds
rew = []
for x in range(K):
    rew.append(0.0)
print("Exploration start.")
for x in range(K):
    for y in range(N):
        u = random.normalvariate(mr[x], 0.1)
        rew[x] = (rew[x] * y + u) / (y + 1)
umax = rew[0]
a = 0
for x in range(K - 1):
    if rew[x + 1] > umax:
        umax = rew[x + 1]
        a = x + 1
print("Highest Average Reward=", umax)
print("Average reward of each arm", rew)
print("Arm with highest average reward", a + 1)
print("Exploration complete.")
exp = 0.0
print("Exploitation start.")
for x in range(T):
    u = random.normalvariate(mr[a], 0.1)
    exp = exp + u
print("Total Reward=", exp)

plt.plot(mr, rew)

# naming the x axis
plt.xlabel('Mean Reward')
# naming the y axis
plt.ylabel('Average Reward')

# giving a title to my graph
plt.title('Trend in Uniform Exploration')

# function to show the plot
plt.show()