    @docstring.dedent_interpd
    def bar_2d_height(self, x, heights, width=None, colors=None,
                      *args, **kwargs):
        r"""
        Make a bar plot.

        Call signatures::

           bar_2d_height(x, heights, width=None, colors=None, align='center',
                                                                      **kwargs)

        The bars are position dependent on the width as width is used to help
        calculate the offset in order to position the group of bars to be
        centered correctly around their corresponding x point.
        If number of bars is even, then the point will be directly between
        the 2 middle bars.
        If number of bars is odd, then the point will be directly in the middle
        of the middle bar.
        Offset calculated will make sure there are no gaps between the bars

        Parameters
        ----------
        x : sequence of scalars
            The x coordinates of the bars. See also *align* for the
            alignment of the bars to the coordinates.

        heights : scalar o array-like of sequence of scalars i.e. 2D array
            of height for each bar. Each sequence of scalars in heights MUST
            be the same length as x.

        width : scalar or array-like, optional
            The width(s) of the bars (default: 0.8).
            will apply to all bars as well as be used in the offset positions
            of each bar.

        bottom : scalar or array-like, optional
            The y coordinate(s) of the bars bases (default: 0).

        align : {'center', 'edge'}, optional, default: 'center'
            Alignment of the bars to the *x* coordinates:

            - 'center': Center the base on the *x* positions.
            - 'edge': Align the left edges of the bars with the *x* positions.

            To align the bars on the right edge pass a negative *width* and
            ``align='edge'``.

        Other Parameters
        ----------------
        colors : scalar or array-like, optional
            each color in colors will be applied to corresponding bar based
            on index. colors length must be same as length of heights parameter

        edgecolor : scalar or array-like, optional
            The colors of the bar edges.

        linewidth : scalar or array-like, optional
            Width of the bar edge(s). If 0, don't draw edges.

        tick_label : string or array-like, optional
            The tick labels of the bars.
            Default: None (Use default numeric labels.)

        xerr, yerr : scalar or array-like of shape(N,) or shape(2,N), optional
            If not *None*, add horizontal / vertical errorbars to the bar tips.
            The values are +/- sizes relative to the data:

            - scalar: symmetric +/- values for all bars
            - shape(N,): symmetric +/- values for each bar
            - shape(2,N): separate + and - values for each bar

            Default: None

        ecolor : scalar or array-like, optional, default: 'black'
            The line color of the errorbars.

        capsize : scalar, optional
           The length of the error bar caps in points.
           Default: None, which will take the value from
           :rc:`errorbar.capsize`.

        error_kw : dict, optional
            Dictionary of kwargs to be passed to the `~.Axes.errorbar`
            method. Values of *ecolor* or *capsize* defined here take
            precedence over the independent kwargs.

        log : bool, optional, default: False
            If *True*, set the y-axis to be log scale.

        orientation : {'vertical',  'horizontal'}, optional
            *This is for internal use only.* Please use `barh` for
            horizontal bar plots. Default: 'vertical'.

        Notes
        -----
        All other parameters except colors (New and unique to bar_2d_height),
        width, heights (New and unique to bar_2d_height), and x will be
        directly used in this function. All other parameters of bar will not
        be touched and will simply be passed over as arguments for each bar.
            - x: will be altered for each bar by offsetting the value
            - width: although will be passed the same will be used to help
            calculate the offset of each bar.
            - heights: is just a 2D array of height parameter in bar and will
            simply be used to get the height for each bar
            - colors: must be an array/structured array of size heights, it
            will apply color of own choice to each bar.

        color parameter in bar should not be given to this function as normally
        color is only is only applied to one bar. colors should be used instead
        where size of colors is the number of bars i.e. length of heights. To
        apply custom colors to each bar, just enumerate colors with chars that
        correspond with the color associated with them.

        The optional arguments *color*, *edgecolor*, *linewidth*,
        *xerr*, and *yerr* can be either scalars or sequences of
        length equal to the number of bars.  This enables you to use
        bar as the basis for stacked bar charts, or candlestick plots.
        Detail: *xerr* and *yerr* are passed directly to
        :meth:`errorbar`, so they can also have shape 2xN for
        independent specification of lower and upper errors.

        Other optional kwargs:

        %(Rectangle)s
        """
        # keep track of the size of heights; less len(heights) calls
        size_heights = len(heights)
        # Some error checking for heights, must be 2d array
        if isinstance(heights, list):
            for y in range(size_heights):
                if not isinstance(heights[y], list):
                    raise ValueError('Input is not a 2d array')
        else:
            try:
                if not len(heights.shape) == 2:
                    raise ValueError('Input is not a 2d array')
            except AttributeError:
                raise ValueError('Input is not a 2d array')

        # checks if the arrays inside heights are the same length
        height_inner_array_length = len(heights[0])
        for height_inner_array in heights:
            if len(height_inner_array) != height_inner_array_length:
                raise ValueError('Every array inside heights must be the same
                                 length')

        # Makes sure no size mismatch happen between heights, x, width, and
        # colors
        if len(x) != len(heights[0]):
            raise ValueError('The array of x axis is not the same size as the
                             arrays in the heights array')
        if isinstance(colors, list):
            if len(heights) != len(colors):
                raise ValueError('The array of colors is not the same size as
                                 heights array')
        if isinstance(width, list):
            if len(x) != len(width):
                raise ValueError('The array of widths is not the same size as
                                 x array')
        # For new parameter colors which should be an array of length heights
        colorsb = []
        # if colors is None, it will enumerate colors with None else keep.
        if colors is None:
            for i in range(size_heights):
                colorsb.append(None)
            colorsb = np.array(colorsb)
        else:
            colorsb = colors
        # if width is None, set to default of 0.8
        if width is None:
            width = 0.8
        # Sets self.bar to be used to create multiple bars
        _barfunc = self.bar
        # Used to index height for use of offset and getting color from colorsb
        count_h = 0
        # for height in heights:
        while count_h < size_heights:
            # clone x to be reused without changing original values for
            # next bar.
            if (isinstance(x, list)):
                xlist = x[:]
            else:
                xlist = np.copy(x)
            # case where width is an array, must change x size of width times
            if isinstance(width, (list, np.ndarray, np.generic)):
                for w in range(len(width)):
                    offset = width[w]
                    # below makes sure that the offset equals the width of bar
                    # so as to make sure there are no gaps between them.
                    if (size_heights % 2) == 1:
                        current_offset = (offset*(size_heights - 1)/2)
                    else:
                        current_offset = (offset*size_heights/2)-(offset/2)
                    current_offset -= offset*(count_h)
                    xlist[w] -= current_offset
            else:
                # Like previous comment, used to get offset to make sure
                # there are no gaps between the set/group of bars.
                if (size_heights % 2) == 1:
                    current_offset = (width*(size_heights - 1)/2)
                else:
                    current_offset = (width*size_heights/2)-(width/2)
                current_offset -= width*(count_h)
                # Had to do it this way because list doesn't support what
                # numpy arrays suppor; subtracting all x elements by a y value.
                if isinstance(x, list):
                    xlist[:] = [y-current_offset for y in xlist]
            # For when not to adjust the x values because already adjusted
            if isinstance(x, list):
                _barfunc(xlist, heights[count_h], color=colorsb[count_h],
                         width=width,
                         *args, **kwargs)
            # For when to adjust the x values, since it hasnt been adjusted.
            else:
                _barfunc(x-current_offset, heights[count_h],
                         color=colorsb[count_h],
                         width=width,
                         *args, **kwargs)
            # keeps track of which bar.
            count_h += 1 
