#!/usr/bin/env python3
"""Basic plot setting"""
from dataclasses import dataclass

from cycler import cycler

from .fonts import FontBase
from .lines import LineBase
from .markers import MarkerBase
from pymyplot import get_color
from pymyplot import myplt
from pymyplot.figsize import Figsize


@dataclass
class BasicMarker(MarkerBase):

    default_size: float = 16


@dataclass
class BasicLine(LineBase):

    default_linewidth: float = 1.0


@dataclass
class BasicFont(FontBase):

    default_size: float = 16.0
    default_family: str = "sans-serif"
    default_font: str = "Helvetica"
    use_tex: bool = True


@dataclass
class BasicFigsize(Figsize):
    """Column dimension.
    * single: 8.5 cm
    * double: 17
    """

    column_single: float = 8.5
    column_double: float = 17
    row_default: float = 6


Font = BasicFont()
Line = BasicLine()
Marker = BasicMarker()

# Default settings
myplt.rcParams["legend.fontsize"] = Font.size("text-lg")
myplt.rcParams["figure.titlesize"] = Font.size("text-2xl")
myplt.rcParams["axes.labelsize"] = Font.size("text-base")
myplt.rcParams["xtick.labelsize"] = Font.size("text-xs")
myplt.rcParams["ytick.labelsize"] = Font.size("text-sm")

myplt.rcParams["font.size"] = Font.default_size
myplt.rcParams["font.family"] = Font.default_family
myplt.rcParams["font.sans-serif"] = Font.default_font
myplt.rcParams["text.usetex"] = Font.use_tex

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
