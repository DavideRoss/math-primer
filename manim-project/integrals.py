from manim import *

from utils import *

def eval(x):
    return x

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

class Int0(Scene):
    def construct(self):
        basis(self)
        
        f1 = formula(r"f'(x) = x")
        f1.scale(0.75)
        f1.move_to(UP * 3 + LEFT * 5.5)
        self.add(f1)

        f2 = formula(r"\frac{d}{dx} x^a = ax^{a-1}")
        f2.scale(0.75)
        f2.move_to(UP * 3 + LEFT * 3)
        self.add(f2)

class Int1(Scene):
    def construct(self):
        basis(self)
        
        f1 = formula(r"f'(x) = x")
        f1.scale(0.75)
        f1.move_to(UP * 3 + LEFT * 5.5)
        self.add(f1)

        f2 = formula(r"\frac{d}{dx} x^a = ax^{a-1}")
        f2.scale(0.75)
        f2.move_to(UP * 3 + LEFT * 3)
        self.add(f2)

        f3 = formula(r"\int_{}^{}x^adx = \frac{x^{a+1}}{a+1} + C")
        f3.scale(0.75)
        f3.move_to(UP * 3 + LEFT * -.5)
        self.add(f3)

class Int2(Scene):
    def construct(self):
        plane, _ = basis(self)

        graph2 = plane.plot(lambda x: (x ** 2) / 2, color=BLUE)
        self.add(graph2)
        
        f1 = formula(r"f'(x) = x")
        f1.scale(0.75)
        f1.move_to(UP * 3 + LEFT * 5.5)
        self.add(f1)

        f2 = formula(r"\frac{d}{dx} x^a = ax^{a-1}")
        f2.scale(0.75)
        f2.move_to(UP * 3 + LEFT * 3)
        self.add(f2)

        f3 = formula(r"\int_{}^{}x^adx = \frac{x^{a+1}}{a+1} + C")
        f3.scale(0.75)
        f3.move_to(UP * 3 + LEFT * -.5)
        self.add(f3)

        f4 = formula(r"f(x) = \frac{x^2}{2} + C", color=BLUE)
        f4.scale(0.75)
        f4.move_to(UP * 3 + RIGHT * 5.5)
        self.add(f4)

class Int3(Scene):
    def construct(self):
        plane, _ = basis(self)

        graph2 = plane.plot(lambda x: (x ** 2) / 2, color=BLUE)
        self.add(graph2)

        f = formula(r"f(x) = \frac{x^2}{2} + C", color=BLUE)
        f.scale(0.75)
        f.move_to(UP * 3 + RIGHT * 5.5)
        self.add(f)

        f1 = formula(r"f'(x) = x")
        f1.scale(0.75)
        f1.move_to(UP * 3 + LEFT * 5.5)
        self.add(f1)

class Int4(Scene):
    def construct(self):
        plane, _ = basis(self)

        graph2 = plane.plot(lambda x: (x ** 2) / 2, color=BLUE)
        self.add(graph2)

        g3 = plane.plot(lambda x: x + 0.5, color=YELLOW)
        self.add(g3)

        f = formula(r"f(x) = \frac{x^2}{2} + C", color=BLUE)
        f.scale(0.75)
        f.move_to(UP * 3 + RIGHT * 5.5)
        self.add(f)

        f1 = formula(r"f'(x) = x")
        f1.scale(0.75)
        f1.move_to(UP * 3 + LEFT * 5.5)
        self.add(f1)

        f2 = formula(r"f'(x) = x+\frac{1}{2}", color=YELLOW)
        f2.scale(0.75)
        f2.move_to(UP * 1.75 + LEFT * 5.5)
        self.add(f2)
        

class Int5(Scene):
    def construct(self):
        plane, _ = basis(self)

        graph2 = plane.plot(lambda x: (x ** 2) / 2, color=BLUE)
        self.add(graph2)

        g3 = plane.plot(lambda x: x + 0.5, color=YELLOW)
        self.add(g3)

        g4 = plane.plot(lambda x: x + 1.25, color=PINK)
        self.add(g4)

        f = formula(r"f(x) = \frac{x^2}{2} + C", color=BLUE)
        f.scale(0.75)
        f.move_to(UP * 3 + RIGHT * 5.5)
        self.add(f)

        f1 = formula(r"f'(x) = x")
        f1.scale(0.75)
        f1.move_to(UP * 3 + LEFT * 5.5)
        self.add(f1)

        f2 = formula(r"f'(x) = x+\frac{1}{2}", color=YELLOW)
        f2.scale(0.75)
        f2.move_to(UP * 1.75 + LEFT * 5.5)
        self.add(f2)

        f3 = formula(r"f'(x) = x+\frac{5}{4}", color=PINK)
        f3.scale(0.75)
        f3.move_to(UP * .25 + LEFT * 5.5)
        self.add(f3)
        