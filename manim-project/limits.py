from manim import *
from utils import *

import math
import numpy as np

class Const(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range=(-3, 11, 1),
            y_range=(-3, 7, 1),
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            }
        )

        plane.scale(1.5)

        dot = Dot(plane.coords_to_point(3, 1), color=GREEN)
        lines = plane.get_lines_to_point(plane.c2p(3, 1))

        formula = formula(r"\lim_{x \to 3} x-2")
        formula.move_to(LEFT * 3 + UP * 2.5)

        graph = plane.plot(lambda x: x - 2, color=RED)
        self.add(plane, graph, lines, dot, formula)

class Sin(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range=(-10, 10, 1),
            y_range=(-5, 5, 1),
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            }
        )

        lim_point = plane.c2p(PI, 0)

        dot = Dot(lim_point, color=GREEN)
        lines = plane.get_lines_to_point(lim_point)

        formula = formula(r"\lim_{x \to \pi} 2sin(x)")
        formula.move_to(LEFT * 4 + UP * 2.85)

        graph = plane.plot(lambda x: 2 * math.sin(x), color=RED)
        self.add(plane, graph, lines, dot, formula)

class Log(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range=(-10, 10, 1),
            y_range=(-5, 5, 1),
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            }
        )

        # lim_point = plane.c2p(-1, 0)

        # dot = Dot(lim_point, color=GREEN)
        # lines = plane.get_lines_to_point(lim_point)

        formula = formula(r"\lim_{x \to -1} \log(x + 1)")
        formula.move_to(LEFT * 4 + UP * 2.85)

        asint = vertical_asymptote(plane, -1)

        graph = plane.plot(lambda x: np.log(x + 1), [0.00001 - 1, 10, 0.005], color=RED)
        self.add(plane, graph, asint, formula)

class Div1(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range=(-10, 10, 1),
            y_range=(-5, 5, 1),
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            }
        )

        # lim_point = plane.c2p(-1, 0)

        # dot = Dot(lim_point, color=GREEN)
        # lines = plane.get_lines_to_point(lim_point)

        formula1 = eval(r"\lim_{x \to +\infty} \frac{1}{x}")
        formula1.move_to(LEFT * 5 + UP * 2.85)

        graph1 = plane.plot(lambda x: 1.0/x, [-10, -0.001, 0.005], color=RED)
        graph2 = plane.plot(lambda x: 1.0/x, [0.001, 10, 0.005], color=RED)
        self.add(plane, graph1, graph2, formula1)

class Div2(Scene):
    def construct(self):
        formula2 = eval(r"\lim_{x \to 0} \frac{1}{x}", 0.7)
        formula2.move_to(LEFT * 2.5 + UP * 2.85)

        self.add(formula2)