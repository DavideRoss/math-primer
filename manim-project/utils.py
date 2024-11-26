from manim import *

import numpy as np

def formula(formula, opacity=0.5, color=RED, rect_size=-1):
    group = VGroup()

    text = MathTex(formula)
    rect = SurroundingRectangle(text, color, fill_color=color, corner_radius=0.1, buff=.25)

    if rect_size > 0:
        rect = RoundedRectangle(
            width=rect_size,
            height=text.height + 2 * 0.25,
            color=color, fill_color=color, corner_radius=0.1
        )
        
    rect.set_fill(color, opacity)

    group.add(rect)
    group.add(text)

    return group

def vertical_asymptote(plane, x, range=10):
    return DashedLine(plane.c2p(x, -range), plane.c2p(x, range), dash_length=.25, stroke_width=1.5)

def horizontal_asymptote(plane, y, range=10):
    return DashedLine(plane.c2p(-range, y), plane.c2p(range, y), dash_length=.25, stroke_width=1.5)

def distance(p1, p2):
    return np.linalg.norm(p2 - p1)