import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import random

style.use('fivethirtyeight')

fig = plt.figure()
axs = fig.add_subplot(1, 1, 1)

def animate(a):
   x = []
   y = []
   
   for i in range(0, 10):
       x.append(i)
       y.append(random.randint(1, 10))

   axs.clear()
   axs.plot(x, y)
   
ani = animation.FuncAnimation(fig, animate, interval = 1000)

plt.show()
