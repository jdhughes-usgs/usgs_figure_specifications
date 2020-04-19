"""

"""
import numpy as np
import matplotlib.pyplot as plt

def graph_legend(ax, handles=None, labels=None, **kwargs):
    font = {'size': 9, 'weight': 'bold',
            'family': 'Univers 67 Condensed'}
    if handles is None or labels is None:
        handles, labels = ax.get_legend_handles_labels()
    leg = ax.legend(handles, labels, prop=font, **kwargs)

    # add title to legend
    if 'title' in kwargs:
        title = kwargs.pop('title')
    else:
        title = None
    leg = graph_legend_title(leg, title=title)

    return leg


def graph_legend_title(leg, title=None):
    if title is None:
        title = 'EXPLANATION'
    elif title.lower() == 'none':
        title = None
    leg.set_title(title, prop={'size': 9, 'weight': 'bold',
                               'family': 'Univers 67 Condensed'})
    return leg


def heading(ax, letter=None, heading=None, x=0.00, y=1.01):
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

def set_font(bold=True, italic=True, fontsize=9):
    if bold:
        weight = 'bold'
        family = 'Univers 67'
    else:
        weight = 'normal'
        family = 'Univers 57'

    if italic:
        family += ' Condensed Oblique'
        style = 'oblique'
    else:
        family += ' Condensed'
        style = 'normal'
    font = {'family': family,
            'size': fontsize,
            'weight': weight,
            'style': style}

    return font

def add_text(ax=None, text='', x=0., y=0., transform=True,
             bold=True, italic=True, fontsize=9,
             ha='left', va='bottom', **kwargs):
    if ax is None:
        return None

    if transform:
        transform = ax.transAxes
    else:
        transform = ax.transData

    font = set_font(bold=bold, italic=italic,
                    fontsize=fontsize)

    text_obj = ax.text(x, y, text,
                       va=va, ha=ha,
                       fontdict=font,
                       transform=transform, **kwargs)
    return text_obj

def add_annotation(ax=None, text='', xy=None, xytext=None,
                   bold=True, italic=True, fontsize=9,
                   ha='left', va='bottom', **kwargs):
    if ax is None:
        return None

    if xy is None:
        xy = (0., 0.)

    if xytext is None:
        xytext = (0., 0.)

    font = set_font(bold=bold, italic=italic,
                    fontsize=fontsize)

    # add font information to kwargs
    if kwargs is None:
        kwargs = font
    else:
        for key, value in font.items():
            kwargs[key] = value

    # create annotation
    ann_obj = ax.annotate(text, xy, xytext,
                          va=va, ha=ha,
                          **kwargs)

    return ann_obj

def remove_edge_ticks(ax, verbose=False):
    # update tick objects
    plt.draw()

    # get min and max value and ticks
    ymin, ymax = ax.get_ylim()
    # check for condition where y-axis values are reversed
    if ymax < ymin:
        y = ymin
        ymin = ymax
        ymax = y
    yticks = ax.get_yticks()
    if verbose:
        print('y-axis: ', ymin, ymax)
        print(yticks)

    # remove edge ticks on y-axis
    ticks = ax.yaxis.majorTicks
    for iloc in [0, -1]:
        if np.allclose(float(yticks[iloc]), ymin):
            ticks[iloc].tick1line.set_visible = False
            ticks[iloc].tick2line.set_visible = False
        if np.allclose(float(yticks[iloc]), ymax):
            ticks[iloc].tick1line.set_visible = False
            ticks[iloc].tick2line.set_visible = False

    # get min and max value and ticks
    xmin, xmax = ax.get_xlim()
    # check for condition where x-axis values are reversed
    if xmax < xmin:
        x = xmin
        xmin = xmax
        xmax = x
    xticks = ax.get_xticks()
    if verbose:
        print('x-axis: ', xmin, xmax)
        print(xticks)

    # remove edge ticks on y-axis
    ticks = ax.xaxis.majorTicks
    for iloc in [0, -1]:
        if np.allclose(float(xticks[iloc]), xmin):
            ticks[iloc].tick1line.set_visible = False
            ticks[iloc].tick2line.set_visible = False
        if np.allclose(float(xticks[iloc]), xmax):
            ticks[iloc].tick1line.set_visible = False
            ticks[iloc].tick2line.set_visible = False

    return ax