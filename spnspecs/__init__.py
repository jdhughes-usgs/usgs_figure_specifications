"""
The spnspecs package implements SPN figure specifications for Graphs and
Diagrams, ...

"""

__name__ = 'spnspecs'
__author__ = 'Joseph D. Hughes'

from .version import __version__

# imports
from . import spnspecs
from .graphs import set_graph_specifications
from .maps import set_map_specifications
from .utils import graph_legend, graph_legend_title, \
    heading, set_font, add_text, add_annotation, \
    remove_edge_ticks

#from .mbase import run_model, which
