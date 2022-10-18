#!/usr/bin/env python3
"""Presets to prepare the plot for the AIP manuscipt"""
from dataclasses import dataclass

from cycler import cycler

from pymyplot import cm
from pymyplot import get_color
from pymyplot import myplt


# Lines
@dataclass
class Line:
    """Collection of line width.
    * thiner: 0.1 pt
    * thin: 0.5 pt
    * normal: 1 pt
    * thick: 2 pt
    * thicker: 3 pt
    """

    thiner: float = 0.1
    thin: float = 0.5
    normal: float = 1
    thick: float = 2
    thicker: float = 3


# Max size
@dataclass
class Coloum:
    """Coloumn dimesnion.
    * single: 8.5 cm
    * double: 17
    """

    single: float = 8.5 * cm
    double: float = 17 * cm


# Fonts
@dataclass
class Font:
    """Font size
    * smaller: 8 pt
    * samll: 10 pt
    * noraml: 12 pt
    * large: 14 pt
    * larger: 16 pt
    """

    tiny: float = 4
    smallest: float = 6
    smaller: float = 8
    small: float = 10
    normal: float = 12
    large: float = 14
    larger: float = 16


# DPI
@dataclass
class DPI:
    """DPI setup
    * line: 600 dpi
    * color: 300 dpi
    """

    line: float = 600
    color: float = 300


# Figure format
fig_format = "eps"

myplt.rcParams["figure.dpi"] = 100
myplt.rcParams["savefig.dpi"] = DPI.line

# Set default font sizes
myplt.rcParams["font.size"] = Font.normal
myplt.rcParams["legend.fontsize"] = Font.smaller
myplt.rcParams["figure.titlesize"] = Font.large
myplt.rcParams["axes.labelsize"] = Font.normal
myplt.rcParams["xtick.labelsize"] = Font.smaller
myplt.rcParams["ytick.labelsize"] = Font.smaller

# Set font style
myplt.rcParams["text.usetex"] = True
myplt.rcParams["font.family"] = "sans-serif"
myplt.rcParams["font.sans-serif"] = "Helvetica"

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
