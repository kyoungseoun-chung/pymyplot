#!/usr/bin/env python3
"""Presets to prepare the plot for the Elevier manuscript (mostly for the JCP).
It follows guidelines from https://www.elsevier.com/authors/policies-and-guidelines/artwork-and-media-instructions/artwork-sizing
"""
from dataclasses import dataclass

from cycler import cycler

from .figsize import Figsize
from .fonts import FontBase
from .lines import LineBase
from .markers import MarkerBase
from pymyplot import get_color
from pymyplot import myplt


@dataclass
class ELMarker(MarkerBase):
    """Follows the font size."""

    default_size: float = 10.0


@dataclass
class ELLine(LineBase):
    """Guide line suggest the line weight range from 0.1 pt to 1.5 pt for eps format figure.
    Therefore, if user set `default_linewidth=1.0`, `w-0.5` yields 0.125 pt and `w-6` yields 1.5pt, which meets the guideline.
    """

    default_linewidth: float = 1.0


@dataclass
class ELFont(FontBase):
    """Guide line suggests 7pt for the normal text and no smaller than 6pt for subscript and superscript.
    However, here we use 10pt for the normal text to be safe. Therefore, the minimum size will be 7.5pt."""

    default_size: float = 10.0
    default_family: str = "sans-serif"
    default_font: str = "Helvetica"
    use_tex: bool = True


@dataclass
class ELFigsize(Figsize):
    """Elsevier column dimension.
    * single: 9 cm
    * double: 19 cm
    * 1/2 column: 140 cm
    """

    column_single: float = 9
    column_double: float = 19
    row_default: float = 6


@dataclass
class ELdpi:
    """DPI setup
    * line: 600 dpi
    * color: 300 dpi
    """

    halftone: float = 300
    art: float = 500
    line: float = 1000


# Figure format
fig_format = "eps"

# Custom axis related font size

Font = ELFont()
Line = ELLine()
Marker = ELMarker()
FigSize = ELFigsize()
DPI = ELdpi()

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
myplt.rcParams["figure.dpi"] = DPI.halftone
myplt.rcParams["savefig.dpi"] = DPI.line

# Cycler
# Follows the recommended color palette in get_color method
default_cycler = cycler(
    color=[
        get_color("sky-700"),
        get_color("red-500"),
        get_color("green-600"),
        get_color("yellow-500"),
        get_color("cyan-400"),
        get_color("fuchsia-700"),
        get_color("gray-400"),
    ]
) + cycler(linestyle=["-", "--", ":", "-.", "-", "--", ":"])

myplt.rc("axes", prop_cycle=default_cycler)
