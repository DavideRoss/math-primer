from manim import *

from utils import *

def eval(x):
    return x

def basis(scene, fun=eval):
    x_range = 15
    y_range = 10

    plane = NumberPlane(
        x_range=(-x_range, x_range, .1),
        y_range=(-y_range, y_range, .1),
        background_line_style={
            'stroke_color': TEAL,
            'stroke_width': .2,
            'stroke_opacity': 0.4
        },
        axis_config={
            'include_ticks': True,
            'tick_size': .025,
            'color': GREY_C
        },
        x_axis_config={
            'include_numbers': True,
            'numbers_to_include': [0,1,2,3,4,5,6,7,8,9,10],
            'decimal_number_config': {
                'num_decimal_places': 0,
                'unit': 's'
            }
        },
        y_axis_config={
            'length': 100,
            'include_numbers': True,
            'numbers_to_include': [0,1,2,3,4,5,6,7,8,9,10],
            'decimal_number_config': {
                'num_decimal_places': 0,
                'unit': '00m'
            }
        }
    )

    plane2 = NumberPlane(
        x_range=(-x_range, x_range, 1),
        y_range=(-y_range, y_range, 1),
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

    # Normal
    # zoom = 1.225
    # pos = DOWN * 3 + LEFT * 6.1

    # 5
    zoom = 1.13
    pos = DOWN * 3.25 + LEFT * 5.7

    plane.scale(zoom)
    plane.move_to(pos)

    plane2.scale(zoom)
    plane2.move_to(pos)

    scene.add(plane, plane2)
    return plane

def sim(dt=1, sim_length=10):
    t = 0.0
    x = []
    y = []

    velocity = 0.0
    position = 0.0
    force = 10.0
    mass = 1.0

    while t <= sim_length:
        x.append(t)
        y.append(position / 100)

        position += velocity * dt
        velocity += (force / mass) * dt

        t += dt

    return (x, y)

def sim_semi(dt=1, sim_length=10):
    t = 0.0
    x = []
    y = []

    velocity = 0.0
    position = 0.0
    force = 10.0
    mass = 1.0

    while t <= sim_length:
        x.append(t)
        y.append(position / 100)

        velocity += (force / mass) * dt
        position += velocity * dt

        t += dt

    return (x, y)

class Num1(Scene):
    def construct(self):
        plane = basis(self)

        xval, yval = sim()
        sim_graph = plane.plot_line_graph(
            x_values=xval,
            y_values=yval,
            line_color=RED
        )

        line1 = DashedLine(plane.c2p(10, 0), plane.c2p(10, 4.5))
        line2 = DashedLine(plane.c2p(0, 4.5), plane.c2p(10, 4.5))
        self.add(line1, line2)

        t = MathTex(r"450m", color=GREEN)
        t.scale(1.5)
        t.move_to(plane.c2p(5, 4.5) + UP * 0.2 + t.height / 2)
        self.add(t)

        self.add(sim_graph)

class Num2(Scene):
    def construct(self):
        plane = basis(self)

        xval, yval = sim()
        sim_graph = plane.plot_line_graph(
            x_values=xval,
            y_values=yval,
            line_color=RED
        )

        line1 = DashedLine(plane.c2p(10, 0), plane.c2p(10, 4.5))
        line2 = DashedLine(plane.c2p(0, 4.5), plane.c2p(10, 4.5))
        self.add(line1, line2)

        t = MathTex(r"450m", color=GREEN)
        t.scale(1.5)
        t.move_to(plane.c2p(5, 4.5) + UP * 0.2 + t.height / 2)
        self.add(t)

        self.add(sim_graph)

        f = formula(r"p = p_{0} +v_{0}t + \frac{1}{2}at^2")
        f.scale(0.75)
        f.move_to(LEFT * 3 + DOWN * 0.25)
        self.add(f)

class Num3(Scene):
    def construct(self):
        plane = basis(self)

        xval, yval = sim()
        sim_graph = plane.plot_line_graph(
            x_values=xval,
            y_values=yval,
            line_color=RED
        )

        line1 = DashedLine(plane.c2p(10, 0), plane.c2p(10, 5.0))
        line2 = DashedLine(plane.c2p(0, 5.0), plane.c2p(10, 5.0))
        self.add(line1, line2)

        t = MathTex(r"500m", color=GREEN)
        t.scale(1.5)
        t.move_to(plane.c2p(5, 5.0) + UP * 0.2 + t.height / 2)
        self.add(t)

        self.add(sim_graph)

        g2 = plane.plot(lambda x: (5 * x ** 2) / 100, x_range=(0, 10, .1), color=BLUE)
        self.add(g2)

        d = Dot(plane.c2p(10, 5))
        self.add(d)

        f = formula(r"p = p_{0} +v_{0}t + \frac{1}{2}at^2")
        f.scale(0.75)
        f.move_to(LEFT * 3 + DOWN * 0.25)
        self.add(f)

class Num4(Scene):
    def construct(self):
        plane = basis(self)

        xval, yval = sim(dt=0.033)
        sim_graph = plane.plot_line_graph(
            x_values=xval,
            y_values=yval,
            line_color=RED,
            add_vertex_dots=False
        )

        last_val = yval[-1]

        line1 = DashedLine(plane.c2p(10, 0), plane.c2p(10, last_val))
        line2 = DashedLine(plane.c2p(0, last_val), plane.c2p(10, last_val))
        self.add(line1, line2)

        t = MathTex("{:.2f}m".format(last_val * 100), color=GREEN)
        t.scale(1.5)
        t.move_to(plane.c2p(5, 5.0) + UP * 0.2 + t.height / 2)
        self.add(t)

        self.add(sim_graph)

        g2 = plane.plot(lambda x: (5 * x ** 2) / 100, x_range=(0, 10, .1), color=BLUE)
        self.add(g2)

        d = Dot(plane.c2p(10, 5))
        self.add(d)

        f = formula(r"p = p_{0} +v_{0}t + \frac{1}{2}at^2")
        f.scale(0.75)
        f.move_to(LEFT * 3 + DOWN * 0.25)
        self.add(f)

class Num5(Scene):
    def construct(self):
        plane = basis(self)

        xval, yval = sim(dt=1.0)
        sim_graph = plane.plot_line_graph(
            x_values=xval,
            y_values=yval,
            line_color=RED
        )

        xval2, yval2 = sim_semi(dt=1.0)
        sim_graph2 = plane.plot_line_graph(
            x_values=xval2,
            y_values=yval2,
            line_color=YELLOW
        )

        last_val = yval[-1]
        last_val2 = yval2[-1]

        line2 = DashedLine(plane.c2p(0, last_val), plane.c2p(10, last_val))
        self.add(line2)

        t = MathTex(r"450m", color=RED)
        t.scale(1.5)
        t.move_to(plane.c2p(5, last_val) + DOWN * (0.2 + t.height / 2))
        self.add(t)

        line3 = DashedLine(plane.c2p(10, 0), plane.c2p(10, last_val2))
        line4 = DashedLine(plane.c2p(0, last_val2), plane.c2p(10, last_val2))
        self.add(line3, line4)

        t2 = MathTex(r"550m", color=GREEN)
        t2.scale(1.5)
        t2.move_to(plane.c2p(5, last_val2) + UP * (0.2 + t.height / 2))
        self.add(t2)

        self.add(sim_graph, sim_graph2)

        g2 = plane.plot(lambda x: (5 * x ** 2) / 100, x_range=(0, 10, .1), color=BLUE)
        self.add(g2)

        d = Dot(plane.c2p(10, 5))
        self.add(d)