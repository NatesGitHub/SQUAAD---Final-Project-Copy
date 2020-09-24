'''
ISSUE #9462: Matplotlib

Code based on code from original issue:
https://github.com/matplotlib/matplotlib/issues/9462

Issue is present in both Python2 and Python3 on Ubuntu.
'''

import matplotlib.pyplot as plt

fig = plt.figure()

# number of frames, if less than 4 there is no alignment issue
nFrames = 4

# cycle through each frame
for k in range(nFrames):
    ax = fig.add_subplot(1, nFrames, k+1, aspect='equal')
    plt.tick_params(axis='both', which='both', bottom='off', top='off',
                    labelbottom='off', left='off', right='off',
                    labelleft='off')

plt.subplots_adjust(wspace=0)

# saves a PNG file with expected behaviour (aligned boxes)
plt.savefig('alignmentTest_no_bbox_inches.png', format='png')

# saves a PNG file with unexpected behaviour (misaligned boxes)
plt.savefig('alignmentTest_bbox_inches_tight.png', format='png',
            bbox_inches='tight')
