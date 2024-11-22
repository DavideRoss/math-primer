from manim import *

def formula(formula, opacity=0.5):
    group = VGroup()

    text = MathTex(formula)
    rect = SurroundingRectangle(text, color=RED, fill_color=RED, corner_radius=0.1, buff=.25)
    rect.set_fill(RED, opacity)

    group.add(rect)
    group.add(text)

    return group

def vertical_asymptote(plane, x, range=10):
    return DashedLine(plane.c2p(x, -range), plane.c2p(x, range), dash_length=.25, stroke_width=1.5)

def horizontal_asymptote(plane, y, range=10):
    return DashedLine(plane.c2p(-range, y), plane.c2p(range, y), dash_length=.25, stroke_width=1.5)