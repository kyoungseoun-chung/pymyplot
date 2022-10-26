#!/usr/bin/env python3
"""Basic plot setting"""
from dataclasses import dataclass

from cycler import cycler

from .fonts import FontBase
from .lines import LineBase
from .markers import MarkerBase
from pymyplot import get_color
from pymyplot import myplt


@dataclass
class BasicMarker(MarkerBase):

    default_size: float = 10


@dataclass
class BasicLine(LineBase):

    default_linewidth: float = 1.0


@dataclass
class BasicFont(FontBase):

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


Font = BasicFont()
Line = BasicLine()
Marker = BasicMarker()
