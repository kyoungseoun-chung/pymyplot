#!/usr/bin/env python3
"""Figure size module."""
from dataclasses import dataclass

from pymyplot import cm


@dataclass
class Figsize:
    """Column dimension.
    * single: 8.5 cm
    * double: 17
    """

    column_single: float = 8.5
    column_double: float = 17
    row_default: float = 6

    @property
    def w_sc(self) -> float:
        """Width of the single column figure."""
        return self.column_single * cm

    @property
    def w_dc(self) -> float:
        """Width of the double column figure."""
        return self.column_double * cm

    @property
    def w_hc(self) -> float:
        """Width of the 1-1/2 column figure."""
        return 0.5 * (self.column_double + self.column_single) * cm

    @property
    def h_sr(self) -> float:
        """Height of the single row figure."""
        return self.row_default * cm

    @property
    def h_dr(self) -> float:
        """Height of the double row figure."""
        return self.row_default * 2 * cm

    @property
    def h_hr(self) -> float:
        """Height of the 1-1/2 row figure."""
        return self.row_default * 1.5 * cm

    def w(self, width_scale: float) -> float:
        """Width of the figure. 8.5 cm * `num_col`."""
        return width_scale * self.column_single * cm

    def h(self, height_scale: float) -> float:
        """Height of the figure. 6 cm * `num_row`."""

        return height_scale * self.row_default * cm
