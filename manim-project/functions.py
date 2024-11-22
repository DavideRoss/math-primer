from manim import *
import math

import numpy as np

class FunctionSin(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range=(-10, 10, 1),
            y_range=(-6, 6, 1),
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            }
        )

        graph = plane.plot(lambda x: math.sin(x), x_range=(-10, 10), color=RED)
        self.add(plane, graph)

class FunctionSquare(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range=(-10, 10, 1),
            y_range=(-5, 10, 1),
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            }
        )

        graph = plane.plot(lambda x: x ** 2, color=RED)
        self.add(plane, graph)

class FunctionTangent(Scene):
    def construct(self):
        zoom = 1
        plane = NumberPlane(
            x_range=(-10, 10, 1 / zoom),
            y_range=(-5, 5, 1 / zoom),
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            }
        )

        tan_group = VGroup()
        approx_factor = 0.934
        for n in range(-2, 3):
            graph = plane.plot(
                lambda x: np.tan(x),
                x_range=(
                    (-PI/2) * approx_factor + n * PI,
                    (PI/2) * approx_factor + n * PI,
                    0.05
                ),
                color=RED
            )

            tan_group.add(graph)

        # graph = plane.plot(lambda x: math.tan(x))
        self.add(plane, tan_group)

class FunctionCos(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range=(-10, 10, 1),
            y_range=(-5, 5, 1),
            background_line_style={
                "stroke_color": BLUE,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            }
        )

        disc_lines = VGroup()

        for x in range(-2, 3):
            disc_line = DashedLine(plane.coords_to_point(x * PI + PI / 2, -10), plane.coords_to_point(x * PI + PI / 2, 10), dash_length=.25, stroke_width=1)
            disc_lines.add(disc_line)
            dot = Dot(plane.coords_to_point(x * PI + PI / 2, 0), radius=.05, color=PURE_RED)
            disc_lines.add(dot)

        graph = plane.plot(lambda x: math.cos(x), x_range=(-10, 10), color=GREEN)
        self.add(graph, disc_lines)

class FunctionCircle(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range=(-10, 10, 1),
            y_range=(-10, 10, 1),
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            }
        )

        circle = Circle(
            radius=2.0,
            color=RED,
        )

        self.add(plane, circle)

class FunctionRandom(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range=(-10, 10, 1),
            y_range=(-10, 10, 1),
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            }
        )

        raph = plane.plot(lambda x: 2 - 4 * np.random.random(), color=RED)

        self.add(plane, raph)
