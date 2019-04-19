"""

"""
import matplotlib.pyplot as plt

def graph_legend(ax, handles=None, labels=None, **kwargs):
    font = {'size': 9, 'weight': 'bold',
            'family': 'Univers 67 Condensed'}
    if handles is None or labels is None:
        handles, labels = ax.get_legend_handles_labels()
    leg = ax.legend(handles, labels, prop=font, **kwargs)

    # add title to legend
    leg = graph_legend_title(leg)

    return leg


def graph_legend_title(leg):
    leg.set_title('EXPLANATION', prop={'size': 9, 'weight': 'bold',
                                       'family': 'Univers 67 Condensed'})
    return leg


def heading( ax, letter=None, heading=None, x=0.00, y=1.01):
    text = None
    if letter is not None:
        font = {'family': 'Univers 67 Condensed Oblique',
                'size': 9,
                'weight': 'bold',
                'style': 'oblique'}
        if heading is None:
            letter = letter.replace('.', '')
        else:
            letter = letter.rstrip()
            if letter[-1] is not '.':
                letter += '.'
            letter += ' '
        ax.text(x, y, letter,
                va='bottom', ha='left',
                fontdict=font,
                transform=ax.transAxes)
        bbox = ax.get_window_extent().transformed(
            plt.gcf().dpi_scale_trans.inverted())
        width = bbox.width * 25.4  # inches to mm
        x += len(letter) * 1. / width
    if heading is not None:
        font = {'family': 'Univers 67 Condensed',
                'size': 9,
                'weight': 'bold',
                'style': 'normal'}
        text = ax.text(x, y, heading,
                       va='bottom', ha='left',
                       fontdict=font,
                       transform=ax.transAxes)
    return text


def remove_edge_ticks(ax, verbose=False):
    # update tick objects
    plt.draw()

    # get min and max value and ticks
    ymin, ymax = ax.get_ylim()
    yticks = ax.get_yticks()
    if verbose:
        print('y-axis: ', ymin, ymax)
        print(yticks)

    # remove edge ticks on y-axis
    ticks = ax.yaxis.majorTicks
    if float(yticks[0]) == ymin:
        ticks[0].tick1On = False
        ticks[0].tick2On = False
    if float(yticks[-1]) == ymax:
        ticks[-1].tick1On = False
        ticks[-1].tick2On = False

    # get min and max value and ticks
    xmin, xmax = ax.get_xlim()
    xticks = ax.get_xticks()
    if verbose:
        print('x-axis: ', xmin, xmax)
        print(xticks)

    # remove edge ticks on y-axis
    ticks = ax.xaxis.majorTicks
    if float(xticks[0]) == xmin:
        ticks[0].tick1On = False
        ticks[0].tick2On = False
    if float(xticks[-1]) == xmax:
        ticks[-1].tick1On = False
        ticks[-1].tick2On = False

    return ax