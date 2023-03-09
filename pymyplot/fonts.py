#!/usr/bin/env python3
"""
Font module
"""
from dataclasses import dataclass

from pymyplot import get_color
from pymyplot.scaling import FONT_WEIGHT
from pymyplot.scaling import HEIGHT_SCALE
from pymyplot.scaling import SIZE_SCALE


@dataclass
class FontBase:

    default_size: float = 16.0
    """Default fontsize. Set to 16px."""
    default_family: str = "sans-serif"
    default_font: str = "Helvetica"
    use_tex: bool = True

    def size(self, size_key: str) -> float:
        """Return size of the font using the size_key.
        For the scaling factors, see: `pymyplot.scaling.SIZE_SCALE`
        """

        assert size_key in list(SIZE_SCALE.keys())

        return SIZE_SCALE[size_key] * self.default_size

    def weight(self, weight_key: str) -> int:
        """Return font weight. Follows tailwindcss convention."""

        assert weight_key in list(FONT_WEIGHT.keys())

        return FONT_WEIGHT[weight_key]

    def color(self, color_code: str) -> str:
        """Return color of the font using the color_code. The color_code follows tailwindcss convention."""

        return get_color(color_code)

    def linespacing(self, spacing_key: str) -> float:
        """Line spacing. Multiplication factor of the font size. Also uses tailwindcss convention `leading-*`."""

        assert spacing_key in list(HEIGHT_SCALE.keys())

        return HEIGHT_SCALE[spacing_key]
