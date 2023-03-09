#!/usr/bin/env python3
"""Marker base class"""
from dataclasses import dataclass

from matplotlib.markers import MarkerStyle

from pymyplot.scaling import SIZE_SCALE


@dataclass
class MarkerBase:

    default_size: float = 16.0

    def style(self, style_key: str) -> MarkerStyle:
        """Return marker style. It follows matplotlib convention.
        Return type is `matplotlib.markers.MarkerStyle` to be properly used in plot with types.
        """

        return MarkerStyle(style_key)

    def size(self, size_key: str) -> float:
        """Return size of the marker using the size_key.
        For the scaling factors, see: `pymyplot.scaling.SIZE_SCALE`
        """

        assert size_key in list(SIZE_SCALE.keys())

        return SIZE_SCALE[size_key] * self.default_size
