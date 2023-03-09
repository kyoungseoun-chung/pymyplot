#!/usr/bin/env python3
"""Line base object."""
from dataclasses import dataclass

from .markers import MarkerStyle
from pymyplot import get_color
from pymyplot.scaling import WIDTH_SCALE


linestyle_set = {
    "solid": "-",
    "dotted": ":",
    "dashed": "--",
    "dashdot": "-.",
    "loosely dotted": (0, (1, 10)),
    "dotted": (0, (1, 1)),
    "densely dotted": (0, (1, 1)),
    "long dash with offset": (5, (10, 3)),
    "loosely dashed": (0, (5, 10)),
    "dashed": (0, (5, 5)),
    "densely dashed": (0, (5, 1)),
    "loosely dashdotted": (0, (3, 10, 1, 10)),
    "dashdotted": (0, (3, 5, 1, 5)),
    "densely dashdotted": (0, (3, 1, 1, 1)),
    "dashdotdotted": (0, (3, 5, 1, 5, 1, 5)),
    "loosely dashdotdotted": (0, (3, 10, 1, 10, 1, 10)),
    "densely dashdotdotted": (0, (3, 1, 1, 1, 1, 1)),
}


@dataclass
class LineBase:

    default_linewidth = 1.0

    def width(self, width_key: str) -> float:
        """Return width of the line using the width key.
        For the scaling factors, see: `pymyplot.scaling.WIDTH_SCALE`
        """

        assert width_key in list(WIDTH_SCALE.keys())

        return WIDTH_SCALE[width_key] * self.default_linewidth

    def color(self, color_code: str) -> str:

        return get_color(color_code)

    def marker(self, style_key: str) -> MarkerStyle:

        return MarkerStyle(style_key)

    def style(self, style_key: str) -> tuple:

        return linestyle_set[style_key]
