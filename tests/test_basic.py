#!/usr/bin/env python3
"""Test font module."""
import pytest

from pymyplot.basic import Font
from pymyplot.basic import Line
from pymyplot.basic import Marker


def test_fonts() -> None:

    assert pytest.approx(Font.size("medium")) == 12.0
    assert pytest.approx(Font.size("small")) == 12.0 * 0.833


def test_lines() -> None:

    assert pytest.approx(Line.width("thin")) == 0.5
    assert Line.style("solid") == "-"


def test_markers() -> None:

    assert pytest.approx(Marker.size("small")) == 10 * 0.5
