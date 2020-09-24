'''
Feature Request #326

Since we did not modify any existing code and only added code,
in this file we list where the code has been selected to be added
and list what was added.
'''


# in pyplot.py, after function `def title(s, *args, **kwargs)`
def set_axes_color(color):
    """
    Sets overall colour of axes spines, ticks, axis labels, and title.

    Parameters
    ----------
    color : string
        color to be set for the current axes.

    """
    gca().set_axes_color(color)


# in _axes.py, after function `def annotate(self, *args, **kwargs)`
# and also indented the same
def set_axes_color(self, color):
    """
    Sets overall colour of axes spines, ticks, axis labels, and title.

    Parameters
    ----------
    color : string
        color to be set for the current axes.

    """
    self.spines['bottom'].set_color(color)
    self.spines['top'].set_color(color)
    self.spines['right'].set_color(color)
    self.spines['left'].set_color(color)

    self.tick_params(axis='x', colors=color)
    self.tick_params(axis='y', colors=color)

    self.yaxis.label.set_color(color)
    self.xaxis.label.set_color(color)

    self.title.set_color(color)