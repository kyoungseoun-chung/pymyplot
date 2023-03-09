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

    def h(self, num_row: int) -> float:
        """Height of the figure. 6 cm * `num_row`."""

        return num_row * self.row_default * cm
