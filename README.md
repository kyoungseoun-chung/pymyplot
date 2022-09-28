# Pymyplot

A collection of useful presets for the visualization of scientific data. It is intended for personal use only.

## Usage

### Basic

In the module, `myplt` overwrites `matplotlib.pyplot`. This is intended to apply custom `matplotlib.pyplot.rcparams` for a specific plot preset when it is imported. (e.g. `pymyplot.aip`)

```python
>>> from pymyplot import myplt  # myplt overwrites matplotlib.pyplot
>>> from pymyplot import aip # Presets following the AIP journal guidelines
>>> fig, ax = myplt.subplots(...)
>>> ax.plot(..., linewidth=aip.Line.thin)
>>> myplt.save_fig(..., format=aip.fig_format, dpi=aip.DIP.line)
```

### Colors

`pymyplot` uses colors from [TailwindCSS](https://tailwindcss.com). You can access to the colors using TailwindCSS syntax.

```python
>>> from pymyplot import get_color
>>> get_color("red-400")
"#f87171"
```
