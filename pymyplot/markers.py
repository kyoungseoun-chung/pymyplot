#!/usr/bin/env python3
"""Marker base class"""
from dataclasses import dataclass

from matplotlib.markers import MarkerStyle

marker_scaling = {
    "xx-small": 0.1,
    "x-small": 0.3,
    "small": 0.5,
    "medium": 1.0,
    "large": 1.5,
    "x-large": 2.0,
    "xx-large": 3.0,
    "normal": 1.0,
}


@dataclass
class MarkerBase:

    default_size: float = 6.0

    def style(self, style_key: str) -> MarkerStyle:

        return MarkerStyle(style_key)

    def size(self, size_key: str) -> float:

        assert size_key in [
            "xx-small",
            "x-small",
            "small",
            "medium",
            "large",
            "x-large",
            "xx-large",
            "normal",
        ], f"Marker: {size_key} is not available!"

        return marker_scaling[size_key] * self.default_size
