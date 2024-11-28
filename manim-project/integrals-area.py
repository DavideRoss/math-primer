from manim import *

from utils import *

def eval(x):
    return (2.5 * (x - 1) - (x - 1) ** 3 + 1 * (x - 1) ** 2) / 3

def basis(scene, fun=eval):
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

    zoom = 3.5

    plane.scale(zoom)
    plane.move_to(DOWN * 2 + LEFT * 5)

    plane2.scale(zoom)
    plane2.move_to(DOWN * 2 + LEFT * 5)

    graph = plane.plot(fun, color=RED)

    scene.add(plane, plane2, graph)
    return (plane, graph)

def integration_sum(plane, zoom, min=0, max=3, step=0.1):
    group_rects = VGroup()
    group_dots = VGroup()

    width = step * zoom

    x = min
    while x <= max:
        r = Rectangle(BLUE, eval(x) * zoom, width)
        r.move_to(plane.c2p(x + step / 2, eval(x) / 2))
        if eval(x) >= 0:
            r.set_fill(BLUE, 0.25)
        else:
            r.set_stroke(RED)
            r.set_fill(RED, 0.25)

        group_rects.add(r)

        p = Dot(plane.c2p(x, eval(x)))
        group_dots.add(p)

        x += step

    return group_rects, group_dots

# =================================================================================
# =================================================================================

class IntAreaLinear0(Scene):
    def construct(self):
        plane, _ = basis(self, lambda x: 1)

        l = DashedLine(plane.c2p(3, -5), plane.c2p(3, 5))
        self.add(l)

        t1 = MathTex("0")
        t1.scale(0.75)
        t1.move_to(plane.c2p(0, 0) + DOWN * 0.35 + RIGHT * 0.35)
        self.add(t1)

        t2 = MathTex("3")
        t2.scale(0.75)
        t2.move_to(plane.c2p(3, 0) + DOWN * 0.35 + LEFT * 0.35)
        self.add(t2)

        t3 = MathTex(r"\text{Velocity} = \frac{\text{meters}}{\text{seconds}}")
        t3.scale(0.75)
        t3.move_to(UP * 2.5 + LEFT * 3)
        self.add(t3)

        t4 = MathTex(r"\text{Time} = \text{seconds}")
        t4.scale(0.75)
        t4.move_to(DOWN * 2.5)
        self.add(t4)

        d1 = Dot(plane.c2p(0, 1))
        d2 = Dot(plane.c2p(3, 1))
        self.add(d1, d2)

        f = formula(r"\int_{0}^{3}x dx = {?}")
        f.scale(0.75)
        f.move_to(UP * 2.5 + RIGHT * 3)
        self.add(f)

class IntAreaLinear1(Scene):
    def construct(self):
        plane, graph = basis(self, lambda x: 1)
        area = plane.get_area(
            graph,
            x_range=(0, 3),
            color=BLUE
        )

        self.add(area, graph)

        l = DashedLine(plane.c2p(3, -5), plane.c2p(3, 5))
        self.add(l)

        t1 = MathTex("0")
        t1.scale(0.75)
        t1.move_to(plane.c2p(0, 0) + DOWN * 0.35 + RIGHT * 0.35)
        self.add(t1)

        t2 = MathTex("3")
        t2.scale(0.75)
        t2.move_to(plane.c2p(3, 0) + DOWN * 0.35 + LEFT * 0.35)
        self.add(t2)

        t3 = MathTex(r"\text{Velocity} = \frac{\text{meters}}{\text{seconds}}")
        t3.scale(0.75)
        t3.move_to(UP * 2.5 + LEFT * 3)
        self.add(t3)

        t4 = MathTex(r"\text{Time} = \text{seconds}")
        t4.scale(0.75)
        t4.move_to(DOWN * 2.5)
        self.add(t4)

        d1 = Dot(plane.c2p(0, 1))
        d2 = Dot(plane.c2p(3, 1))
        self.add(d1, d2)

        f = formula(r"\int_{0}^{3}x dx = {?}")
        f.scale(0.75)
        f.move_to(UP * 2.5 + RIGHT * 3)
        self.add(f)

class IntArea0(Scene):
    def construct(self):
        plane, graph = basis(self)

        area1 = plane.get_area(
            graph,
            x_range=(1, 3),
            color=BLUE
        )

        area2 = plane.get_area(
            graph,
            x_range=(0, 1),
            color=RED
        )

        l = DashedLine(plane.c2p(3, -5), plane.c2p(3, 5))
        self.add(l)

        t1 = MathTex("0")
        t1.scale(0.75)
        t1.move_to(plane.c2p(0, 0) + DOWN * 0.35 + RIGHT * 0.35)
        self.add(t1)

        t2 = MathTex("3")
        t2.scale(0.75)
        t2.move_to(plane.c2p(3, 0) + DOWN * 0.35 + LEFT * 0.35)
        self.add(t2)

        self.add(area1, area2)
        self.add(graph)

        d1 = Dot(plane.c2p(0, eval(0)))
        d2 = Dot(plane.c2p(3, eval(3)))
        self.add(d1, d2)

        f = formula(r"\int_{0}^{3}f(x) dx = {?}", rect_size=5)
        f.scale(0.75)
        f.move_to(UP * 2.5 + LEFT * 2.75)
        self.add(f)

class IntArea1(Scene):
    def construct(self):
        plane, graph = basis(self)

        step = 0.3

        rects, dots = integration_sum(plane, 3.5, step=step)
        self.add(rects, dots)

        l = DashedLine(plane.c2p(3, -5), plane.c2p(3, 5))
        self.add(l)
        
        self.add(graph)
        self.add(dots)

        t1 = MathTex("0")
        t1.scale(0.75)
        t1.move_to(plane.c2p(0, 0) + DOWN * 0.35 + RIGHT * 0.35)
        self.add(t1)

        t2 = MathTex("3")
        t2.scale(0.75)
        t2.move_to(plane.c2p(3, 0) + DOWN * 0.35 + LEFT * 0.35)
        self.add(t2)

        # Area numerical calculation
        area = 0
        x = 0
        while x <= 3:
            area += eval(x) * step
            x += step

        f = formula(r"\int_{0}^{3}f(x) dx = " + "{:.4f}".format(round(area, 4)), rect_size=5)
        f.scale(0.75)
        f.move_to(UP * 2.5 + LEFT * 2.75)
        self.add(f)

class IntArea2(Scene):
    def construct(self):
        plane, graph = basis(self)

        step = 0.3

        rects, dots = integration_sum(plane, 3.5, step=step)
        self.add(rects, dots)

        l = DashedLine(plane.c2p(3, -5), plane.c2p(3, 5))
        self.add(l)
        
        self.add(graph)
        self.add(dots)

        t1 = MathTex("0")
        t1.scale(0.75)
        t1.move_to(plane.c2p(0, 0) + DOWN * 0.35 + RIGHT * 0.35)
        self.add(t1)

        t2 = MathTex("3")
        t2.scale(0.75)
        t2.move_to(plane.c2p(3, 0) + DOWN * 0.35 + LEFT * 0.35)
        self.add(t2)

        # Area numerical calculation
        area = 0
        x = 0
        while x <= 3:
            area += eval(x) * step
            x += step

        f = formula(r"\int_{0}^{3}f(x) dx = " + "{:.4f}".format(round(area, 4)), rect_size=5)
        f.scale(0.75)
        f.move_to(UP * 2.5 + LEFT * 2.75)
        self.add(f)

        f2 = formula(r"\sum_{i=1}^{n}f(x)\Delta x")
        f2.scale(0.75)
        f2.move_to(UP * 2.5 + RIGHT * 0.5)
        self.add(f2)

class IntArea3(Scene):
    def construct(self):
        plane, graph = basis(self)

        step = 0.3

        rects, dots = integration_sum(plane, 3.5, step=step)
        self.add(rects, dots)

        l = DashedLine(plane.c2p(3, -5), plane.c2p(3, 5))
        self.add(l)
        
        self.add(graph)
        self.add(dots)

        t1 = MathTex("0")
        t1.scale(0.75)
        t1.move_to(plane.c2p(0, 0) + DOWN * 0.35 + RIGHT * 0.35)
        self.add(t1)

        t2 = MathTex("3")
        t2.scale(0.75)
        t2.move_to(plane.c2p(3, 0) + DOWN * 0.35 + LEFT * 0.35)
        self.add(t2)

        # Area numerical calculation
        area = 0
        x = 0
        while x <= 3:
            area += eval(x) * step
            x += step

        f = formula(r"\int_{0}^{3}f(x) dx = " + "{:.4f}".format(round(area, 4)), rect_size=5)
        f.scale(0.75)
        f.move_to(UP * 2.5 + LEFT * 2.75)
        self.add(f)

        f2 = formula(r"\sum_{i=1}^{n}f(x)\Delta x")
        f2.scale(0.75)
        f2.move_to(UP * 2.5 + RIGHT * 0.5)
        self.add(f2)

        f3 = formula(r"\Delta x = \frac{b-a}{n} = \frac{3}{n}")
        f3.scale(0.75)
        f3.move_to(UP * 2.5 + RIGHT * 3.4)
        self.add(f3)

class IntArea4(Scene):
    def construct(self):
        plane, graph = basis(self)

        step = 0.3

        rects, dots = integration_sum(plane, 3.5, step=step)
        self.add(rects, dots)

        l = DashedLine(plane.c2p(3, -5), plane.c2p(3, 5))
        self.add(l)
        
        self.add(graph)
        self.add(dots)

        t1 = MathTex("0")
        t1.scale(0.75)
        t1.move_to(plane.c2p(0, 0) + DOWN * 0.35 + RIGHT * 0.35)
        self.add(t1)

        t2 = MathTex("3")
        t2.scale(0.75)
        t2.move_to(plane.c2p(3, 0) + DOWN * 0.35 + LEFT * 0.35)
        self.add(t2)

        # Area numerical calculation
        area = 0
        x = 0
        while x <= 3:
            area += eval(x) * step
            x += step

        f = formula(r"\int_{0}^{3}f(x) dx = " + "{:.4f}".format(round(area, 4)), rect_size=5)
        f.scale(0.75)
        f.move_to(UP * 2.5 + LEFT * 2.75)
        self.add(f)

        f2 = formula(r"\sum_{i=1}^{n}f(x)dx")
        f2.scale(0.75)
        f2.move_to(UP * 2.5 + RIGHT * 0.5)
        self.add(f2)

        f3 = formula(r"dx = \frac{b-a}{n} = \frac{3}{n}")
        f3.scale(0.75)
        f3.move_to(UP * 2.5 + RIGHT * 3.4)
        self.add(f3)

class IntArea5(Scene):
    def construct(self):
        plane, graph = basis(self)

        step = 0.3
        v = ValueTracker(0.3)

        rects, dots = integration_sum(plane, 3.5, step=step)
        self.add(rects, dots)

        rects.add_updater(lambda y: y.become(integration_sum(plane, 3.5, step=v.get_value())[0]))
        dots.add_updater(lambda y: y.become(integration_sum(plane, 3.5, step=v.get_value())[1]))

        l = DashedLine(plane.c2p(3, -5), plane.c2p(3, 5))
        self.add(l)
        
        self.add(graph)
        self.add(dots)

        t1 = MathTex("0")
        t1.scale(0.75)
        t1.move_to(plane.c2p(0, 0) + DOWN * 0.35 + RIGHT * 0.35)
        self.add(t1)

        t2 = MathTex("3")
        t2.scale(0.75)
        t2.move_to(plane.c2p(3, 0) + DOWN * 0.35 + LEFT * 0.35)
        self.add(t2)

        # Area numerical calculation
        def eval_rects(step):
            area = 0
            x = 0
            while x <= 3:
                area += eval(x) * step
                x += step
            return area
        
        area = eval_rects(v.get_value())

        def create_formula(area):
            f = formula(r"\int_{0}^{3}f(x) dx = " + "{:.4f}".format(round(area, 4)), rect_size=5)
            f.scale(0.75)
            f.move_to(UP * 2.5 + LEFT * 2.75)
            return f
        
        f = create_formula(area)
        f.add_updater(lambda y: y.become(create_formula(eval_rects(v.get_value()))))
        self.add(f)

        f2 = formula(r"\sum_{i=1}^{n}f(x)dx")
        f2.scale(0.75)
        f2.move_to(UP * 2.5 + RIGHT * 0.5)
        self.add(f2)

        f3 = formula(r"dx = \frac{b-a}{n} = \frac{3}{n}")
        f3.scale(0.75)
        f3.move_to(UP * 2.5 + RIGHT * 3.4)
        self.add(f3)

        self.wait()
        self.play(v.animate.set_value(0.05), run_time=3)
        self.wait()
        self.play(v.animate.set_value(0.3), run_time=3)
        self.wait()