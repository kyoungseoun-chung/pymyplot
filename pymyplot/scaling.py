#!/usr/bin/env python3
"""Size scaling based on tailwind scaling."""

SIZE_SCALE: dict[str, float] = {
    "text-xs": 0.75,
    "text-sm": 0.875,
    "text-base": 1.0,
    "text-lg": 1.125,
    "text-xl": 1.25,
    "text-2xl": 1.5,
    "text-3xl": 1.875,
    "text-4xl": 2.25,
    "text-5xl": 3.0,
    "text-6xl": 3.75,
    "text-7xl": 4.5,
    "text-8xl": 6.0,
    "text-9xl": 8.0,
}
"""Size scaling. It follows tailwindcss convention. Used both for font and marker size.
>>>  SIZE_SCALE["text-xs"]
0.75
"""

WIDTH_SCALE: dict[str, float] = {
    "w-0": 0.0,
    "w-0.5": 0.125,
    "w-1": 0.25,
    "w-1.5": 0.375,
    "w-2": 0.5,
    "w-2.5": 0.625,
    "w-3": 0.75,
    "w-3.5": 0.875,
    "w-4": 1.0,
    "w-5": 1.25,
    "w-6": 1.5,
    "w-7": 1.75,
    "w-8": 2.0,
    "w-9": 2.25,
    "w-10": 2.5,
    "w-11": 2.75,
    "w-12": 3.0,
    "w-14": 3.5,
    "w-16": 4.0,
    "w-20": 5.0,
    "w-24": 6.0,
    "w-28": 7.0,
    "w-32": 8.0,
    "w-36": 9.0,
    "w-40": 10.0,
}
"""Width scaling. It follows tailwindcss convention. Used for line width.
>>> WIDTH_SCALE["w-0.5"]
0.125
"""

FONT_WEIGHT: dict[str, int] = {
    "font-thin": 100,
    "font-extralight": 200,
    "font-light": 300,
    "font-normal": 400,
    "font-medium": 500,
    "font-semibold": 600,
    "font-bold": 700,
    "font-extrabold": 800,
    "font-black": 900,
}
"""Font weight scaling. It follows tailwindcss convention.
>>> FONT_WEIGHT["font-bold"]
700
"""
