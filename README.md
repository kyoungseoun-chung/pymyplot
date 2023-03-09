# Pymyplot

A collection of useful presets for the visualization of scientific data. It is intended for personal usage but feel free to take a look at it. Also, the intention of this package is to use convention of [tailwincss](www.tailwindcss.com).

> As I noticed, publishing this package to pypi.org appears to be overkill. Nevertheless, I have decided to do so in order to have better access to the library for my own personal use.

## Requirements

- python >= 3.9
- matplotlib >= 3.6.0

## Installation

You can use either [poetry](https://python-poetry.org) or pip.

```bash
pip install pymyplot
# or
poetry add pymyplot
```

## Usage

### Basic

In the module, `myplt` overwrites `matplotlib.pyplot`. This is intended to apply custom `matplotlib.pyplot.rcparams` for a specific plot preset when it is imported. (e.g. `pymyplot.aip`)

```python
>>> from pymyplot import myplt as plt  # myplt overwrites matplotlib.pyplot
>>> from pymyplot.basic import Line, Font, Marker
# Basic presets come with
# Line: default_linewidth = 1.0
# Font: default_font_size = 16.0, default_family = "sans-serif", default_font = "Helvetica"
# Marker: default_size = 16.0
>>> fig, ax = plt.subplots(...)
>>> ax.text(..., fontsize=Font.size("sm"))
>>> ax.plot(..., linewidth=Line.width("w-1.5"), marker=Marker.style("solid"))
>>> ax.scatter(..., s=Marker.size("sm"))
```

`pymyplot` also uses `tailwindcss` color convention.

```python
>>> from pymyplot import get_color
>>> get_color("red-400")
"#f87171"
```

Each `Font`, `Line`, and `Marker` class is interfacing `get_color` method. Therefore, you can also use:

```python
>>> Font.color("red-400")
"#f87171"
```
