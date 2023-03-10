#!/usr/bin/env python3
"""Test font module."""
import numpy as np
import pytest

from pymyplot import myplt as plt


def test_elsevier_setup() -> None:

    from pymyplot.elsevier import Line as ELLine

    for i in range(7):
        plt.plot(
            [i for i in range(7)],
            [i + 1 for _ in range(7)],
            linewidth=ELLine.width("w-40"),
            linestyle="-",
        )

    plt.show()


def test_cmap() -> None:

    from pymyplot.colors import TOLCmap

    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))

    n_row = 3
    figh = 0.35 + 0.15 + (n_row + (n_row - 1) * 0.1) * 0.22
    fig, axs = plt.subplots(nrows=n_row + 1, figsize=(6.4, figh))
    fig.subplots_adjust(top=1 - 0.35 / figh, bottom=0.15 / figh, left=0.2, right=0.99)

    axs[0].imshow(gradient, aspect="auto", cmap=TOLCmap.sunset())
    axs[0].text(
        -0.01,
        0.5,
        "sunset",
        va="center",
        ha="right",
        fontsize=10,
        transform=axs[0].transAxes,
    )
    axs[1].imshow(gradient, aspect="auto", cmap=TOLCmap.BuRd())
    axs[1].text(
        -0.01,
        0.5,
        "BuRd",
        va="center",
        ha="right",
        fontsize=10,
        transform=axs[1].transAxes,
    )
    axs[2].imshow(gradient, aspect="auto", cmap=TOLCmap.nightfall())
    axs[2].text(
        -0.01,
        0.5,
        "nightfall",
        va="center",
        ha="right",
        fontsize=10,
        transform=axs[2].transAxes,
    )
    axs[3].imshow(gradient, aspect="auto", cmap=TOLCmap.PrGn())
    axs[3].text(
        -0.01,
        0.5,
        "PrGn",
        va="center",
        ha="right",
        fontsize=10,
        transform=axs[3].transAxes,
    )
    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axs:
        ax.set_axis_off()

    plt.show()


def test_basic_setup() -> None:
    from pymyplot.scaling import SIZE_SCALE, WIDTH_SCALE, FONT_WEIGHT
    from pymyplot.basic import Font as BasicFont
    from pymyplot.basic import Line as BasicLine
    from pymyplot.basic import Marker as BasicMarker

    assert BasicFont.default_size == 16.0
    assert BasicMarker.default_size == 16.0
    assert BasicLine.default_linewidth == 1.0

    for k, v in SIZE_SCALE.items():
        assert pytest.approx(BasicFont.size(k)) == v * BasicFont.default_size

    for k, v in SIZE_SCALE.items():
        assert pytest.approx(BasicMarker.size(k)) == v * BasicMarker.default_size

    for k, v in WIDTH_SCALE.items():
        assert pytest.approx(BasicLine.width(k)) == v * BasicLine.default_linewidth

    for k, v in FONT_WEIGHT.items():
        assert pytest.approx(BasicFont.weight(k)) == v

    assert plt.rcParams["legend.fontsize"] == BasicFont.size("text-lg")
    assert plt.rcParams["figure.titlesize"] == BasicFont.size("text-2xl")
    assert plt.rcParams["axes.labelsize"] == BasicFont.size("text-base")
    assert plt.rcParams["xtick.labelsize"] == BasicFont.size("text-xs")
    assert plt.rcParams["ytick.labelsize"] == BasicFont.size("text-sm")


def test_aip_setup() -> None:

    from pymyplot.scaling import SIZE_SCALE, WIDTH_SCALE
    from pymyplot.aip import Font as AIPFont
    from pymyplot.aip import Line as AIPLine
    from pymyplot.aip import Marker as AIPMarker

    assert AIPFont.default_size == 12.0
    assert AIPMarker.default_size == 10.0
    assert AIPLine.default_linewidth == 1.0

    for k, v in SIZE_SCALE.items():
        assert pytest.approx(AIPFont.size(k)) == v * AIPFont.default_size

    for k, v in SIZE_SCALE.items():
        assert pytest.approx(AIPMarker.size(k)) == v * AIPMarker.default_size

    for k, v in WIDTH_SCALE.items():
        assert pytest.approx(AIPLine.width(k)) == v * AIPLine.default_linewidth

    assert plt.rcParams["legend.fontsize"] == AIPFont.size("text-base")
    assert plt.rcParams["figure.titlesize"] == AIPFont.size("text-2xl")
    assert plt.rcParams["axes.labelsize"] == AIPFont.size("text-base")
    assert plt.rcParams["xtick.labelsize"] == AIPFont.size("text-sm")
    assert plt.rcParams["ytick.labelsize"] == AIPFont.size("text-sm")
