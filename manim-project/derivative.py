from manim import *
import numpy as np

from utils import *

def eval(x):
    return (2 ** x - x ** 3 + 2 * x ** 2) / 3

def basis(scene):
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
            'color': GREY_C
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
            'color': GREY_C
        }
    )

    zoom = 2.5

    plane.scale(zoom)
    plane.move_to(DOWN * 2 + LEFT * 2)

    plane2.scale(zoom)
    plane2.move_to(DOWN * 2 + LEFT * 2)

    graph = plane.plot(eval, color=RED)

    scene.add(plane, plane2, graph)
    return (plane, graph)

def dot_label(pos, label):
    dot = Dot(pos, color=GREEN)
    label = MathTex(label).move_to(dot.get_center() + UP * 0.5)
    return dot, label

class Delta0(Scene):
    def construct(self):
        plane, _ = basis(self)
        dot_label(self, plane.c2p(1, eval(1)), r"x_{0}")

class Delta1(Scene):
    def construct(self):
        plane, _ = basis(self)
        dot1, label1 = dot_label(plane.c2p(1, eval(1)), r"x_{0}")
        dot2, label2 = dot_label(plane.c2p(2, eval(2)), r"x_{1}")
        self.add(dot1, label1, dot2, label2)

        line1 = DashedLine(dot1.get_center(), plane.c2p(2, eval(1)))
        brace1 = Brace(line1)
        brace_text1 = brace1.get_text(r"dx")
        self.add(line1, brace1, brace_text1)

        line2 = DashedLine(dot2.get_center(), plane.c2p(2, eval(1)))
        brace2 = Brace(line2, direction=[1, 0, 0])
        brace_text2 = brace2.get_text(r"dy")
        self.add(line2, brace2, brace_text2)
        
        self.add(dot1, dot2)

        f = formula(r"slope = \frac{y_1 - y_0}{x_1 - x_0} = \frac{dy}{dx}")
        f.scale(0.75)
        f.move_to(UP * 3 + LEFT * -1)

        self.add(f)

class Delta2(Scene):
    def construct(self):
        plane, _ = basis(self)
        dot1, label1 = dot_label(plane.c2p(1, eval(1)), r"x_{0}")
        dot2, label2 = dot_label(plane.c2p(2, eval(2)), r"x_{1}")
        self.add(dot1, label1, dot2, label2)

        line1 = DashedLine(dot1.get_center(), plane.c2p(2, eval(1)))
        brace1 = Brace(line1)
        brace_text1 = brace1.get_text(r"dx")
        self.add(line1, brace1, brace_text1)

        line2 = DashedLine(dot2.get_center(), plane.c2p(2, eval(1)))
        brace2 = Brace(line2, direction=[1, 0, 0])
        brace_text2 = brace2.get_text(r"dy")
        self.add(line2, brace2, brace_text2)

        tan = Line(dot1.get_center(), dot2.get_center(), color=GREEN).set_length(100)
        self.add(tan)
        
        self.add(dot1, dot2)

        f = formula(r"slope = \frac{y_1 - y_0}{x_1 - x_0} = \frac{dy}{dx}")
        f.scale(0.75)
        f.move_to(UP * 3 + LEFT * -1)

        self.add(f)

class Delta3(Scene):
    def construct(self):
        plane, graph = basis(self)

        t = ValueTracker(2)

        dot1, label1 = dot_label(plane.c2p(1, eval(1)), r"x_{0}")
        dot2, label2 = dot_label(plane.c2p(t.get_value(), eval(t.get_value())), r"x_{1}")
        self.add(dot1, label1, dot2, label2)

        dot2.add_updater(
            lambda y: y.become(dot_label(plane.c2p(t.get_value(), eval(t.get_value())), r"x_{1}")[0])
        )

        label2.add_updater(
            lambda y: y.become(dot_label(plane.c2p(t.get_value(), eval(t.get_value())), r"x_{1}")[1])
        )

        def dashed(pos1, pos2, text, dir=[0, -1, 0]):
            group = VGroup()
            line = DashedLine(pos1, pos2)
            brace = Brace(line, direction=dir)
            brace_text = brace.get_text(text)
            group.add(line, brace, brace_text)
            return group
        
        g1 = dashed(dot1.get_center(), plane.c2p(t.get_value(), eval(1)), r"dx")
        g1.add_updater(
            lambda y: y.become(dashed(dot1.get_center(), plane.c2p(t.get_value(), eval(1)), r"dx"))
        )
        self.add(g1)

        g2 = dashed(dot2.get_center(), plane.c2p(t.get_value(), eval(1)), r"dy", [1, 0, 0])
        g2.add_updater(
            lambda y: y.become(dashed(
                plane.c2p(t.get_value(), eval(t.get_value())),
                plane.c2p(t.get_value(), eval(1)),
                r"dy",
                [1, 0, 0]
            ))
        )
        self.add(g2)

        tan = Line(dot1.get_center(), dot2.get_center(), color=GREEN).set_length(100)
        self.add(tan)

        def tan_updater(y):
            if distance(dot1.get_center(), dot2.get_center()) < 0.0001:
                new_line = Line(plane.c2p(1, 0), plane.c2p(0, 0), color=GREEN) \
                    .set_length(100) \
                    .move_to(plane.c2p(t.get_value(), eval(t.get_value()))) \
                    .rotate(plane.angle_of_tangent(t.get_value(), graph))
            else:
                new_line = Line(dot1.get_center(), dot2.get_center(), color=GREEN).set_length(100)

            y.become(new_line)

        tan.add_updater(tan_updater)
        
        self.add(dot1, dot2)

        f = formula(r"slope = \frac{y_1 - y_0}{x_1 - x_0} = \frac{dy}{dx}")
        f.scale(0.75)
        f.move_to(UP * 3 + LEFT * -1)

        self.add(f)

        self.wait()
        self.play(t.animate.set_value(1), run_time=3)
        self.wait()
        self.play(t.animate.set_value(2), run_time=3)
        self.wait()

class Delta4(Scene):
    def construct(self):
        plane, graph = basis(self)
        der = plane.plot_derivative_graph(graph, color=GREEN)
        self.add(der)

        f = formula(r"\frac{d }{dx}\left(\frac{2^x-x^3+2x^2}{3}\right)=\frac{1}{3}\left(-3x^2+4x+2^x\log(2)\right)")
        f.scale(0.75)
        f.move_to(UP * 3 + LEFT * -1)

        self.add(f)
        