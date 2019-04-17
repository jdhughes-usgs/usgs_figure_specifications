import matplotlib as mpl
import matplotlib.pyplot as plt


class Graph(object):
    def __init__(self):
        rc_dict = {'font.family': 'Univers 57 Condensed',
                   'axes.labelsize': 9,
                   'axes.titlesize': 9,
                   'axes.linewidth': 0.5,
                   'xtick.labelsize': 8,
                   'xtick.top': True,
                   'xtick.bottom': True,
                   'xtick.major.size': 7.2,
                   'xtick.minor.size': 3.6,
                   'xtick.major.width': 0.5,
                   'xtick.minor.width': 0.5,
                   'xtick.direction': 'in',
                   'ytick.labelsize': 8,
                   'ytick.left': True,
                   'ytick.right': True,
                   'ytick.major.size': 7.2,
                   'ytick.minor.size': 3.6,
                   'ytick.major.width': 0.5,
                   'ytick.minor.width': 0.5,
                   'ytick.direction': 'in',
                   'pdf.fonttype': 42,
                   'savefig.dpi': 300,
                   'savefig.transparent': True,
                   'legend.fontsize': 9,
                   'legend.frameon': False,
                   'legend.markerscale': 1.
                   }
        mpl.rcParams.update(rc_dict)
        return

    def legend(self, ax, **kwargs):
        leg = ax.legend(prop={'size': 9, 'weight': 'bold',
                              'family': 'Univers 67 Condensed'},
                        **kwargs)
        self.legend_title(leg)
        return leg

    def legend_title(self, leg):
        leg.set_title('EXPLANATION', prop={'size': 9, 'weight': 'bold',
                                           'family': 'Univers 67 Condensed'})
        return

    def heading(self, ax, letter=None, heading=None, x=0.00, y=1.01):
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
