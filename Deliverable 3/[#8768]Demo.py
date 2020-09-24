'''
ISSUE #8768: Matplotlib

Code based on code from original issue:
https://github.com/matplotlib/matplotlib/issues/8768

Issue is present in both Python2 and Python3.
'''

import matplotlib.pyplot as plt

fig = plt.figure()

# single tick
plt.subplot(2, 1, 1)
plt.loglog([0.11, 0.21], [0.11, 0.21])
plt.title('axes with single tick')

# no ticks
plt.subplot(2, 1, 2)
plt.loglog([0.11, 0.12], [0.11, 0.12])
plt.title('axes with no tick')

plt.subplots_adjust(hspace=0.6)

plt.show()
