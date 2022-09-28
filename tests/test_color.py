#!/usr/bin/env python3
from pymyplot import get_color


def test_colors() -> None:

    black = get_color("black")

    assert black == "#000"

    rose_50 = get_color("rose-50")

    assert rose_50 == "#fff1f2"
