'''
ISSUE #8818: Matplotlib

Issue is present in both Python2 and Python3.
'''

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

# structured array
pts = np.array([(1, 1), (2, 2)], dtype=[("ones", float), ("twos", float)])

# exhibits 'expected' behaviour:
# will plot data from names/labels "ones" and "twos"

# this creates a scatterplot of (1, 1) and (2, 2)
plt.subplot(2, 2, 1)
plt.scatter("ones", "twos", data=pts)
plt.title('scatter("ones", "twos", data=pts)')

# this also creates a scatterplot of (1, 1) and (2, 2)
plt.subplot(2, 2, 2)
plt.scatter(pts["ones"], pts["twos"])
plt.title('scatter(pts["ones"], pts["twos"])')

# exhibits 'unexpected' behaviour:
# will mistaken name/label "twos" as a format string

# this raises a ValueError from reading "twos" as a format string
plt.subplot(2, 2, 3)
# plt.plot("ones", "twos", data=pts)
plt.title('plot("ones", "twos" data=pts)\n(issue #8818)')

# exhibits 'expected' behaviour:
# will plot data from names/labels "ones" and "twos"

# this creates a line from (1, 1) to (2, 2)
plt.subplot(2, 2, 4)
plt.plot(pts["ones"], pts["twos"])
plt.title('plot(pts["ones"], pts["twos"])')

plt.subplots_adjust(hspace=0.6, wspace=0.4)

plt.show()
