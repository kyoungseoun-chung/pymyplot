#!/usr/bin/env python3
import matplotlib.pyplot as plt

from pymyplot.colors import get_color


# Unit conversion
cm = 1 / 2.54
px = 1 / plt.rcParams["figure.dpi"]

# Overwrite matplotlib.pyplot to myplt so that can have a specific plot style when the preset (e.g. pymyplot.aip) is imported
myplt = plt


__all__ = ["get_color"]