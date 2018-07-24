import random
import matplotlib.pyplot as plt

mr = [0.12, 0.23, 0.34, 0.45, 0.56, 0.67, 0.78, 0.82, 0.89, 0.51]  # Mean reward of each arm during exploration
T = 100
ap = random.randint(0, 9)
umax = random.normalvariate(mr[ap], 0.1)
am = ap
rew = umax
et = []
et.append(1)
avg = []
avg.append(rew)
print("Arm number ", ap + 1, " played.")
for x in range(T - 1):
    et.append(random.random())
    if et[x+1] >= 0.5:
        ap = random.randint(0, 9)
        u = random.normalvariate(mr[ap], 0.1)
        rew += u
        avg.append(u)
        print("New arm number", ap + 1, "played.")
        if u > umax:
            umax = u
            am = ap
    else:
        u = random.normalvariate(mr[am], 0.1)
        rew += u
        avg.append(u)
        print("Arm number", am + 1, "played again.")
print("Total Reward", rew)

plt.plot(et, avg)

# naming the x axis
plt.xlabel('epsilon ε')
# naming the y axis
plt.ylabel('Average Reward')

# giving a title to my graph
plt.title('Trend in Epsilon Greedy')

# function to show the plot
plt.show()