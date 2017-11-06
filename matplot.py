import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

x = np.arange(0, 200, 1)
y = []
for i in range(0,200) :
    if i == 0 :
        y.append(random.random())
    else :
        y.append(ranavg(y[i-1], i-1))

fig = plt.figure()
plt.xlim(0, 200)
plt.ylim(0, 1)
graph, = plt.plot([], [], 'o')

def ranavg(a, n):
    if n == 0 :
        a = random.random()
    else :
        a = a*n+random.random()
        n = n+1
        a = a/n
    return a

def animate(i):
    graph.set_data(x[:i+1], y[:i+1])
    return graph

ani = FuncAnimation(fig, animate, frames=200, interval=200)
plt.show()