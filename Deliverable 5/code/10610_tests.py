import matplotlib.pyplot as plt
import datetime
import numpy as np

x = np.array([1,4,9])

#test 1
fig, ax = plt.subplots()
heights = np.array([[1,2,3],[2,4,6],[4,8,12]])
ax.bar_2d_height(x,heights,align='center')
plt.savefig("testbar1.png")

#test 2
fig, ax2 = plt.subplots()
x = np.array([1,2,3,4,5,10])
heights = np.array([[1,2,3,6,4,2],[2,4,1,2,10,11]])
ax2.bar_2d_height(x,heights,width=[0.1,0.1,0.1,0.1,0.1,0.1],
                  colors=['r','k'])
plt.savefig("testbar2.png")

#test 3
fig,ax3 = plt.subplots()
x = np.array([25,50])
heights = np.array([[5,10],[7.5,12.5],[10,15],[1,1],[20,30]])
widths = [0.5,0.5]
ax3.bar_2d_height(x,heights,widths)
plt.savefig("testbar3.png")

#test 4
fig,ax4 = plt.subplots()
x = np.array([1,2,3,4])
heights = np.array([1,2,4,5])
ax4.bar_2d_height(x,heights,widths)
plt.savefig("testbar4.png")
