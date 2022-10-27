#!/usr/bin/env python3
"""Test font module."""
import pytest

from pymyplot.aip import Font as AIPFont
from pymyplot.aip import Line as AIPLine
from pymyplot.aip import Marker as AIPMarker
from pymyplot.basic import Font as BasicFont
from pymyplot.basic import Line as BasicLine
from pymyplot.basic import Marker as BasicMarker


def test_basic_fonts() -> None:

    assert pytest.approx(BasicFont.size("medium")) == 12.0
    assert pytest.approx(BasicFont.size("small")) == 12.0 * 0.833


def test_basic_lines() -> None:

    assert pytest.approx(BasicLine.width("thin")) == 0.5
    assert BasicLine.style("solid") == "-"


def test_basic_markers() -> None:

    assert pytest.approx(BasicMarker.size("small")) == 10 * 0.5


def test_aip_fonts() -> None:

    assert pytest.approx(AIPFont.size("medium")) == 12.0
    assert pytest.approx(AIPFont.size("small")) == 12.0 * 0.833


def test_aip_lines() -> None:

    assert pytest.approx(AIPLine.width("thin")) == 0.5
    assert AIPLine.style("solid") == "-"


def test_aip_markers() -> None:

    assert pytest.approx(AIPMarker.size("small")) == 10 * 0.5
