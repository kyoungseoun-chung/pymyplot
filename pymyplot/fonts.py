#!/usr/bin/env python3
"""
font_scalings = {
    'xx-small': 0.579,
    'x-small':  0.694,
    'small':    0.833,
    'medium':   1.0,
    'large':    1.200,
    'x-large':  1.440,
    'xx-large': 1.728,
    'larger':   1.2,
    'smaller':  0.833,
    None:       1.0,
}
"""
from dataclasses import dataclass

from matplotlib.font_manager import font_scalings

from pymyplot import get_color
from pymyplot import myplt


@dataclass
class FontBase:

    default_size: float = 10.0
    default_family: str = "sans-serif"
    default_font: str = "Helvetica"
    use_tex: bool = True

    def __post_init__(self):

        myplt.rcParams["font.size"] = self.default_size
        myplt.rcParams["font.family"] = self.default_family
        myplt.rcParams["font.sans-serif"] = self.default_font
        myplt.rcParams["text.usetex"] = self.use_tex

    def size(self, size_key: str) -> float:

        assert size_key in [
            "xx-small",
            "x-small",
            "small",
            "medium",
            "large",
            "x-large",
            "xx-large",
            "larger",
            "smaller",
        ], f"Font: {size_key} is not available!"

        return font_scalings[size_key] * self.default_size

    def color(self, color_code: str) -> str:

        return get_color(color_code)
