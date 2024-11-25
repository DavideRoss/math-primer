from manim import *

from utils import *

def eval(x):
    return (2 ** x - x ** 3 + 1 * x ** 2) / 3

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

    zoom = 4

    plane.scale(zoom)
    plane.move_to(DOWN * 2 + LEFT * 2)

    plane2.scale(zoom)
    plane2.move_to(DOWN * 2 + LEFT * 2)

    graph = plane.plot(eval, color=RED)

    scene.add(plane, plane2, graph)
    return (plane, graph)

def integration_sum(plane, zoom, min=-1, max=2, step=0.1):
    group = VGroup()

    width = step * zoom

    x = min
    while x <= max:
        r = Rectangle(BLUE, eval(x) * zoom, width)
        r.move_to(plane.c2p(x + step / 2, eval(x) / 2))
        r.set_fill(BLUE, 0.5)
        group.add(r)

        p = Dot(plane.c2p(x, eval(x)))
        group.add(p)

        x += step

    return group

# =================================================================================
# =================================================================================

class IntArea0(Scene):
    def construct(self):
        plane, _ = basis(self)

        rects = integration_sum(plane, 4, step=0.25)
        self.add(rects)