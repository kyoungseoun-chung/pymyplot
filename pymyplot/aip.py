#!/usr/bin/env python3
"""Presets to prepare the plot for the AIP manuscript"""
from dataclasses import dataclass

from cycler import cycler

from .fonts import FontBase
from .lines import LineBase
from .markers import MarkerBase
from pymyplot import cm
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

    def __post_init__(self):

        # Custom axis related font size
        myplt.rcParams["legend.fontsize"] = self.size("small")
        myplt.rcParams["figure.titlesize"] = self.size("large")
        myplt.rcParams["axes.labelsize"] = self.size("medium")
        myplt.rcParams["xtick.labelsize"] = self.size("small")
        myplt.rcParams["ytick.labelsize"] = self.size("small")

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


# Max size
@dataclass
class AIPFigsize:
    """Column dimension.
    * single: 8.5 cm
    * double: 17
    """

    column_single: float = 8.5 * cm
    column_double: float = 17 * cm

    def width(self, c_type: str) -> float:
        """Width of the figure. Same as column length."""
        assert c_type in ["single", "double", "s", "d"]

        if c_type == "single" or c_type == "s":
            return self.column_single
        else:
            return self.column_double

    def height(self, num_row: int) -> float:
        """Height of the figure. 6 cm * `num_row`."""

        return num_row * 6 * cm


# DPI
@dataclass
class AIPdpi:
    """DPI setup
    * line: 600 dpi
    * color: 300 dpi
    """

    line: float = 600
    color: float = 300

    def __post_init__(self):

        # Set default dpi
        myplt.rcParams["figure.dpi"] = self.color
        myplt.rcParams["savefig.dpi"] = self.line


# Figure format
fig_format = "eps"

Font = AIPFont()
Line = AIPLine()
Marker = AIPMarker()
FigSize = AIPFigsize()
DPI = AIPdpi()
