from manim import *
import numpy as np

from utils import *

def fun1(x):
    return (2 ** x - x ** 3 + 2 * x ** 2) / 3

def planes(scene):
    plane = NumberPlane(
        x_range=(-10, 10, .1),
        y_range=(-6, 6, .1),
        background_line_style={
            'stroke_color': TEAL,
            'stroke_width': .2,
            'stroke_opacity': 0.4
        },
        axis_config={
            'include_ticks': True,
            'tick_size': .025,
            'color': GREY_D
        }
    )

    plane2 = NumberPlane(
        x_range=(-10, 10, 1),
        y_range=(-6, 6, 1),
        background_line_style={
            'stroke_color': TEAL,
            'stroke_width': 1,
            'stroke_opacity': 0.4
        },
        axis_config={
            'include_ticks': True,
            'tick_size': .1,
            'color': GREY_D
        }
    )

    zoom = 2.5

    plane.scale(zoom)
    plane.move_to(DOWN * 2 + LEFT * 2)

    plane2.scale(zoom)
    plane2.move_to(DOWN * 2 + LEFT * 2)

    scene.add(plane, plane2)
    return plane

class Delta1(Scene):
    def construct(self):
        plane = planes(self)

        graph = plane.plot(fun1)

        dot1 = Dot(plane.c2p(1, fun1(1)), color=RED)
        dot2 = Dot(plane.c2p(2, fun1(2)), color=RED)

        line = Line(dot1.get_center(), dot2.get_center(), color=RED).set_length(100)

        vl1 = Line(dot1.get_center(), plane.c2p(1, 0)).set_color(ORANGE)
        vl2 = Line(dot2.get_center(), plane.c2p(2, 0)).set_color(ORANGE)

        brace = Brace(Line(plane.c2p(1, 0), plane.c2p(2, 0)))
        brace_text = brace.get_tex("dt")

        f = formula(r'f(x)=\frac{2^x-x^3+2x^2}{3}')
        f.scale(0.5)
        f.move_to(UP * 3 + LEFT * 2)

        self.add(graph, vl1, vl2, brace, brace_text, line, dot1, dot2, f)

class Delta2(Scene):
    def construct(self):
        plane = planes(self)
        graph = plane.plot(fun1)

        t = ValueTracker(2)

        dot1 = Dot(plane.c2p(1, fun1(1)), color=RED)
        dot2 = Dot(plane.c2p(t.get_value(), fun1(t.get_value())), color=RED)

        dot2.add_updater(lambda x: x.move_to(plane.c2p(t.get_value(), fun1(t.get_value()))))

        line = Line(dot1.get_center(), dot2.get_center(), color=RED).set_length(100)
        line.add_updater(lambda x: x.become(Line(dot1.get_center(), dot2.get_center(), color=RED).set_length(100)))

        vl1 = Line(dot1.get_center(), plane.c2p(1, 0)).set_color(ORANGE)
        vl2 = Line(dot2.get_center(), plane.c2p(2, 0)).set_color(ORANGE)
        vl2.add_updater(lambda x: x.become(Line(dot2.get_center(), plane.c2p(t.get_value(), 0)).set_color(ORANGE)))

        brace = Brace(Line(plane.c2p(1, 0), plane.c2p(2, 0)))
        brace_text = brace.get_tex("dt")
        brace.add_updater(lambda x: x.become(Brace(Line(plane.c2p(1, 0), plane.c2p(t.get_value(), 0)))))
        brace_text.add_updater(lambda x: x.become(brace.get_text("dt")))

        f = formula(r'f(x)=\frac{2^x-x^3+2x^2}{3}')
        f.scale(0.5)
        f.move_to(UP * 3 + LEFT * 2)

        self.add(graph, vl1, vl2, brace, brace_text, line, dot1, dot2, f)

        self.wait()
        self.play(t.animate.set_value(1), run_time=3)
        self.wait()
        self.play(t.animate.set_value(2), run_time=3)
        self.wait()

class Delta3(Scene):
    def construct(self):
        plane = planes(self)
        graph = plane.plot(fun1)

        t = ValueTracker(1)
    
        def tan_point():
            return Dot(plane.c2p(t.get_value(), fun1(t.get_value())), color=RED)
        
        dot = tan_point()
        dot.add_updater(lambda y: y.become(tan_point()))
        
        def tangent():
            return Line(plane.c2p(1, 0), plane.c2p(0, 0)) \
                .set_length(100) \
                .move_to(plane.c2p(t.get_value(), fun1(t.get_value()))) \
                .rotate(plane.angle_of_tangent(t.get_value(), graph)) \
                .set_color(ORANGE)
        
        line = tangent()
        line.add_updater(lambda y: y.become(tangent()))

        f = formula(r'f(x)=\frac{2^x-x^3+2x^2}{3}')
        f.scale(0.5)
        f.move_to(UP * 3 + LEFT * 2)

        self.add(graph, line, dot, f)

        self.wait()
        self.play(t.animate.set_value(-1), run_time=2)
        self.wait()
        self.play(t.animate.set_value(2.5), run_time=2)
        self.wait()
        self.play(t.animate.set_value(1), run_time=2)
        self.wait()

class Delta4(Scene):
    def construct(self):
        plane = planes(self)
        graph = plane.plot(fun1)

        der = plane.plot_derivative_graph(graph, color=ORANGE)

        self.add(graph, der)