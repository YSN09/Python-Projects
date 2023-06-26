# To check whether the flipping of coins follow a normal distribution
import numpy as np 
import matplotlib.pyplot as plt 
final = []
for y in range(10000):
    tails = [0]
    for x in range(10):
        coin = np.random.randint(0,2)
        if coin == 0:
            tails.append(tails[x] + coin)
        else:
            tails.append(tails[x] + coin)
    final.append(tails[-1])

plt.hist(final, bins = 10)
plt.show()
