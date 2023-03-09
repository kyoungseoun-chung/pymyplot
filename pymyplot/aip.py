#!/usr/bin/env python3
"""Presets to prepare the plot for the AIP manuscript"""
from dataclasses import dataclass

from cycler import cycler

from .figsize import Figsize
from .fonts import FontBase
from .lines import LineBase
from .markers import MarkerBase
from pymyplot import get_color
from pymyplot import myplt


@dataclass
class AIPMarker(MarkerBase):

    default_size: float = 10


@dataclass
class AIPLine(LineBase):

    default_linewidth: float = 1.0


@dataclass
class AIPFont(FontBase):

    default_size: float = 12.0
    default_family: str = "sans-serif"
    default_font: str = "Helvetica"
    use_tex: bool = True


@dataclass
class AIPFigsize(Figsize):
    """Column dimension.
    * single: 8.5 cm
    * double: 17
    """

    column_single: float = 8.5
    column_double: float = 17
    row_default: float = 6


# DPI
@dataclass
class AIPdpi:
    """DPI setup
    * line: 600 dpi
    * color: 300 dpi
    """

    line: float = 600
    color: float = 300


# Figure format
fig_format = "eps"

# Custom axis related font size

Font = AIPFont()
Line = AIPLine()
Marker = AIPMarker()
FigSize = AIPFigsize()
DPI = AIPdpi()

# Default settings
myplt.rcParams["legend.fontsize"] = Font.size("text-base")
myplt.rcParams["figure.titlesize"] = Font.size("text-2xl")
myplt.rcParams["axes.labelsize"] = Font.size("text-base")
myplt.rcParams["xtick.labelsize"] = Font.size("text-sm")
myplt.rcParams["ytick.labelsize"] = Font.size("text-sm")

myplt.rcParams["font.size"] = Font.default_size
myplt.rcParams["font.family"] = Font.default_family
myplt.rcParams["font.sans-serif"] = Font.default_font
myplt.rcParams["text.usetex"] = Font.use_tex

# Set default dpi
myplt.rcParams["figure.dpi"] = DPI.color
myplt.rcParams["savefig.dpi"] = DPI.line
# Cycler
default_cycler = cycler(
    color=[
        get_color("red-600"),
        get_color("blue-600"),
        get_color("green-600"),
        get_color("orange-600"),
        get_color("purple-600"),
    ]
) + cycler(linestyle=["-", "--", ":", "-.", "-"])

myplt.rc("axes", prop_cycle=default_cycler)
