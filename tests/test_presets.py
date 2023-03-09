#!/usr/bin/env python3
"""Test font module."""
import pytest

from pymyplot.aip import Font as AIPFont
from pymyplot.aip import Line as AIPLine
from pymyplot.aip import Marker as AIPMarker
from pymyplot.basic import Font as BasicFont
from pymyplot.basic import Line as BasicLine
from pymyplot.basic import Marker as BasicMarker


def test_basic_setup() -> None:
    from pymyplot.scaling import SIZE_SCALE, WIDTH_SCALE, FONT_WEIGHT

    assert BasicFont.default_size == 16.0
    assert BasicMarker.default_size == 16.0
    assert BasicLine.default_linewidth == 1.0

    for k, v in SIZE_SCALE.items():
        assert pytest.approx(BasicFont.size(k)) == v * BasicFont.default_size

    for k, v in SIZE_SCALE.items():
        assert (
            pytest.approx(BasicMarker.size(k)) == v * BasicMarker.default_size
        )

    for k, v in WIDTH_SCALE.items():
        assert (
            pytest.approx(BasicLine.width(k))
            == v * BasicLine.default_linewidth
        )

    for k, v in FONT_WEIGHT.items():
        assert pytest.approx(BasicFont.weight(k)) == v


def test_aip_setup() -> None:
    from pymyplot.scaling import SIZE_SCALE, WIDTH_SCALE

    assert AIPFont.default_size == 12.0
    assert AIPMarker.default_size == 10.0
    assert AIPLine.default_linewidth == 1.0

    for k, v in SIZE_SCALE.items():
        assert pytest.approx(AIPFont.size(k)) == v * AIPFont.default_size

    for k, v in SIZE_SCALE.items():
        assert pytest.approx(AIPMarker.size(k)) == v * AIPMarker.default_size

    for k, v in WIDTH_SCALE.items():
        assert pytest.approx(AIPLine.width(k)) == v * AIPLine.default_linewidth
