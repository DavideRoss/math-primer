from manim import *
import math
import numpy as np

def Base(scene, add_cp_line=False):
    gap = 3
    height = 2

    p1 = LEFT * gap + DOWN * height
    p2 = LEFT * gap * 0.5 + UP * height
    p3 = RIGHT * gap * 0.5 + UP * height
    p4 = RIGHT * gap + DOWN * height

    # l1 = Line(p1, p2, stroke_width=1)
    # l2 = Line(p3, p4, stroke_width=1)
    # scene.add(l1, l2)

    # if add_cp_line:
    #     l3 = Line(p2, p3, stroke_width=1)
    #     scene.add(l3)

    for p in [p1, p4]:
        d = Dot(p).set_z_index(1000)
        scene.add(d)

    # for p in [p2, p3]:
    #     d = Dot(p, stroke_width=2, color=BLACK, stroke_color=WHITE)
    #     scene.add(d)

    scale = 0.75
    t1 = MathTex(r"P_1").scale(scale).move_to(p1 + DOWN * 0.5).set_color(PURPLE_A)
    # t2 = MathTex(r"P_2").scale(scale).move_to(p2 + UP * 0.5).set_color(TEAL)
    # t3 = MathTex(r"P_3").scale(scale).move_to(p3 + UP * 0.5).set_color(GREEN)
    t4 = MathTex(r"P_4").scale(scale).move_to(p4 + DOWN * 0.5).set_color(YELLOW)
    # scene.add(t1, t2, t3, t4)
    scene.add(t1, t4)

    return p1, p2, p3, p4

class Cubic1(Scene):
    def construct(self):
        p1, p2, p3, p4 = Base(self)
        
        bezier = CubicBezier(p1, p2, p3, p4, color=RED)
        self.add(bezier)

class CubicLerp1(Scene):
    def construct(self):
        p1, p2, p3, p4 = Base(self, True)

        t = ValueTracker(0.5)
        
        lerp1 = lambda x: p1 * (1 - x) + p2 * x
        lerp2 = lambda x: p2 * (1 - x) + p3 * x
        lerp3 = lambda x: p3 * (1 - x) + p4 * x

        l1 = Dot(lerp1(0.5)).add_updater(lambda y: y.move_to(lerp1(t.get_value())))
        l2 = Dot(lerp2(0.5)).add_updater(lambda y: y.move_to(lerp2(t.get_value())))
        l3 = Dot(lerp3(0.5)).add_updater(lambda y: y.move_to(lerp3(t.get_value())))
        self.add(l1, l2, l3)

        t1 = MathTex("a").scale(0.8).move_to(lerp1(0.5) + LEFT * 0.3).add_updater(lambda y: y.move_to(lerp1(t.get_value()) + LEFT * 0.3))
        t2 = MathTex("b").scale(0.8).move_to(lerp2(0.5) + UP * 0.3).add_updater(lambda y: y.move_to(lerp2(t.get_value()) + UP * 0.3))
        t3 = MathTex("c").scale(0.8).move_to(lerp3(0.5) + RIGHT * 0.3).add_updater(lambda y: y.move_to(lerp3(t.get_value()) + RIGHT * 0.3))
        self.add(t1, t2, t3)

        self.wait()
        self.play(t.animate.set_value(1), run_time=1.5)
        self.play(t.animate.set_value(0), run_time=3)
        self.play(t.animate.set_value(0.5), run_time=1.5)
        self.wait()

class CubicLerp2(Scene):
    def construct(self):
        p1, p2, p3, p4 = Base(self, True)

        t = ValueTracker(0.5)
        
        lerp1 = lambda x: p1 * (1 - x) + p2 * x
        lerp2 = lambda x: p2 * (1 - x) + p3 * x
        lerp3 = lambda x: p3 * (1 - x) + p4 * x
        lerp4 = lambda x: lerp1(x) * (1 - x) + lerp2(x) * x
        lerp5 = lambda x: lerp2(x) * (1 - x) + lerp3(x) * x

        l1 = Dot(lerp1(0.5)).add_updater(lambda y: y.move_to(lerp1(t.get_value())))
        l2 = Dot(lerp2(0.5)).add_updater(lambda y: y.move_to(lerp2(t.get_value())))
        l3 = Dot(lerp3(0.5)).add_updater(lambda y: y.move_to(lerp3(t.get_value())))
        self.add(l1, l2, l3)

        t1 = MathTex("a").scale(0.8).move_to(lerp1(0.5) + LEFT * 0.3).add_updater(lambda y: y.move_to(lerp1(t.get_value()) + LEFT * 0.3))
        t2 = MathTex("b").scale(0.8).move_to(lerp2(0.5) + UP * 0.3).add_updater(lambda y: y.move_to(lerp2(t.get_value()) + UP * 0.3))
        t3 = MathTex("c").scale(0.8).move_to(lerp3(0.5) + RIGHT * 0.3).add_updater(lambda y: y.move_to(lerp3(t.get_value()) + RIGHT * 0.3))
        self.add(t1, t2, t3)

        line1 = Line(lerp1(0.5), lerp2(0.5), stroke_width=1).add_updater(lambda y: y.become(Line(lerp1(t.get_value()), lerp2(t.get_value()), stroke_width=1)))
        line2 = Line(lerp2(0.5), lerp3(0.5), stroke_width=1).add_updater(lambda y: y.become(Line(lerp2(t.get_value()), lerp3(t.get_value()), stroke_width=1)))
        self.add(line1, line2)

        l4 = Dot(lerp4(0.5)).add_updater(lambda y: y.move_to(lerp4(t.get_value())))
        l5 = Dot(lerp5(0.5)).add_updater(lambda y: y.move_to(lerp5(t.get_value())))
        self.add(l4, l5)

        t4 = MathTex("d").scale(0.8).move_to(lerp4(0.5) + LEFT * 0.25 + UP * 0.25).add_updater(lambda y: y.move_to(lerp4(t.get_value())  + LEFT * 0.25 + UP * 0.25))
        t5 = MathTex("e").scale(0.8).move_to(lerp5(0.5) + RIGHT * 0.25 + UP * 0.25).add_updater(lambda y: y.move_to(lerp5(t.get_value())  + RIGHT * 0.25 + UP * 0.25))
        self.add(t4, t5)

        self.wait()
        self.play(t.animate.set_value(1), run_time=1.5)
        self.play(t.animate.set_value(0), run_time=3)
        self.play(t.animate.set_value(0.5), run_time=1.5)
        self.wait()

class CubicLerp3(Scene):
    def construct(self):
        p1, p2, p3, p4 = Base(self, True)

        t = ValueTracker(0.5)
        
        lerp1 = lambda x: p1 * (1 - x) + p2 * x
        lerp2 = lambda x: p2 * (1 - x) + p3 * x
        lerp3 = lambda x: p3 * (1 - x) + p4 * x
        lerp4 = lambda x: lerp1(x) * (1 - x) + lerp2(x) * x
        lerp5 = lambda x: lerp2(x) * (1 - x) + lerp3(x) * x
        lerp6 = lambda x: lerp4(x) * (1 - x) + lerp5(x) * x

        l1 = Dot(lerp1(0.5)).add_updater(lambda y: y.move_to(lerp1(t.get_value())))
        l2 = Dot(lerp2(0.5)).add_updater(lambda y: y.move_to(lerp2(t.get_value())))
        l3 = Dot(lerp3(0.5)).add_updater(lambda y: y.move_to(lerp3(t.get_value())))
        self.add(l1, l2, l3)

        t1 = MathTex("a").scale(0.8).move_to(lerp1(0.5) + LEFT * 0.3).add_updater(lambda y: y.move_to(lerp1(t.get_value()) + LEFT * 0.3))
        t2 = MathTex("b").scale(0.8).move_to(lerp2(0.5) + UP * 0.3).add_updater(lambda y: y.move_to(lerp2(t.get_value()) + UP * 0.3))
        t3 = MathTex("c").scale(0.8).move_to(lerp3(0.5) + RIGHT * 0.3).add_updater(lambda y: y.move_to(lerp3(t.get_value()) + RIGHT * 0.3))
        self.add(t1, t2, t3)

        line1 = Line(lerp1(0.5), lerp2(0.5), stroke_width=1).add_updater(lambda y: y.become(Line(lerp1(t.get_value()), lerp2(t.get_value()), stroke_width=1)))
        line2 = Line(lerp2(0.5), lerp3(0.5), stroke_width=1).add_updater(lambda y: y.become(Line(lerp2(t.get_value()), lerp3(t.get_value()), stroke_width=1)))
        self.add(line1, line2)

        l4 = Dot(lerp4(0.5)).add_updater(lambda y: y.move_to(lerp4(t.get_value())))
        l5 = Dot(lerp5(0.5)).add_updater(lambda y: y.move_to(lerp5(t.get_value())))
        self.add(l4, l5)

        t4 = MathTex("d").scale(0.8).move_to(lerp4(0.5) + LEFT * 0.25 + UP * 0.25).add_updater(lambda y: y.move_to(lerp4(t.get_value())  + LEFT * 0.25 + UP * 0.25))
        t5 = MathTex("e").scale(0.8).move_to(lerp5(0.5) + RIGHT * 0.25 + UP * 0.25).add_updater(lambda y: y.move_to(lerp5(t.get_value())  + RIGHT * 0.25 + UP * 0.25))
        self.add(t4, t5)

        line3 = Line(lerp4(0.5), lerp5(0.5), stroke_width=1).add_updater(lambda y: y.become(Line(lerp4(t.get_value()), lerp5(t.get_value()), stroke_width=1)))
        self.add(line3)

        fd = Dot(lerp6(0.5), color=RED).add_updater(lambda y: y.move_to(lerp6(t.get_value()))).set_z_index(2000)
        self.add(fd)

        t6 = MathTex(r"P(t)", color=RED).scale(0.8).move_to(lerp6(0.5) + DOWN * 0.4).add_updater(lambda y: y.move_to(lerp6(t.get_value()) + DOWN * 0.4)).set_z_index(2000)
        self.add(t6)

        self.wait()
        self.play(t.animate.set_value(1), run_time=1.5)
        self.play(t.animate.set_value(0), run_time=3)
        self.play(t.animate.set_value(0.5), run_time=1.5)
        self.wait()

class CubicLerp4(Scene):
    def construct(self):
        p1, p2, p3, p4 = Base(self, True)

        t = ValueTracker(0.5)
        
        lerp1 = lambda x: p1 * (1 - x) + p2 * x
        lerp2 = lambda x: p2 * (1 - x) + p3 * x
        lerp3 = lambda x: p3 * (1 - x) + p4 * x
        lerp4 = lambda x: lerp1(x) * (1 - x) + lerp2(x) * x
        lerp5 = lambda x: lerp2(x) * (1 - x) + lerp3(x) * x
        lerp6 = lambda x: lerp4(x) * (1 - x) + lerp5(x) * x

        l1 = Dot(lerp1(0.5)).add_updater(lambda y: y.move_to(lerp1(t.get_value())))
        l2 = Dot(lerp2(0.5)).add_updater(lambda y: y.move_to(lerp2(t.get_value())))
        l3 = Dot(lerp3(0.5)).add_updater(lambda y: y.move_to(lerp3(t.get_value())))
        self.add(l1, l2, l3)

        t1 = MathTex("a").scale(0.8).move_to(lerp1(0.5) + LEFT * 0.3).add_updater(lambda y: y.move_to(lerp1(t.get_value()) + LEFT * 0.3))
        t2 = MathTex("b").scale(0.8).move_to(lerp2(0.5) + UP * 0.3).add_updater(lambda y: y.move_to(lerp2(t.get_value()) + UP * 0.3))
        t3 = MathTex("c").scale(0.8).move_to(lerp3(0.5) + RIGHT * 0.3).add_updater(lambda y: y.move_to(lerp3(t.get_value()) + RIGHT * 0.3))
        self.add(t1, t2, t3)

        line1 = Line(lerp1(0.5), lerp2(0.5), stroke_width=1).add_updater(lambda y: y.become(Line(lerp1(t.get_value()), lerp2(t.get_value()), stroke_width=1)))
        line2 = Line(lerp2(0.5), lerp3(0.5), stroke_width=1).add_updater(lambda y: y.become(Line(lerp2(t.get_value()), lerp3(t.get_value()), stroke_width=1)))
        self.add(line1, line2)

        l4 = Dot(lerp4(0.5)).add_updater(lambda y: y.move_to(lerp4(t.get_value())))
        l5 = Dot(lerp5(0.5)).add_updater(lambda y: y.move_to(lerp5(t.get_value())))
        self.add(l4, l5)

        t4 = MathTex("d").scale(0.8).move_to(lerp4(0.5) + LEFT * 0.25 + UP * 0.25).add_updater(lambda y: y.move_to(lerp4(t.get_value())  + LEFT * 0.25 + UP * 0.25))
        t5 = MathTex("e").scale(0.8).move_to(lerp5(0.5) + RIGHT * 0.25 + UP * 0.25).add_updater(lambda y: y.move_to(lerp5(t.get_value())  + RIGHT * 0.25 + UP * 0.25))
        self.add(t4, t5)

        line3 = Line(lerp4(0.5), lerp5(0.5), stroke_width=1).add_updater(lambda y: y.become(Line(lerp4(t.get_value()), lerp5(t.get_value()), stroke_width=1)))
        self.add(line3)

        fd = Dot(lerp6(0.5), color=RED).add_updater(lambda y: y.move_to(lerp6(t.get_value()))).set_z_index(2000)
        self.add(fd)

        t6 = MathTex(r"P(t)", color=RED).scale(0.8).move_to(lerp6(0.5) + DOWN * 0.4).add_updater(lambda y: y.move_to(lerp6(t.get_value()) + DOWN * 0.4)).set_z_index(2000)
        self.add(t6)

        bezier = CubicBezier(p1, p2, p3, p4, color=RED)
        self.add(bezier)

        self.wait()
        self.play(t.animate.set_value(1), run_time=1.5)
        self.play(t.animate.set_value(0), run_time=3)
        self.play(t.animate.set_value(0.5), run_time=1.5)
        self.wait()

class CubicLerp5(Scene):
    def construct(self):
        p1, _, _, p4 = Base(self, True)

        t = ValueTracker(0.5)
        m = ValueTracker(0)

        p2_pos = [
            LEFT * 3 * 0.5 + UP * 2,
            LEFT * 5 * 0.5 + UP * 0,
            RIGHT * 4 * 0.5 + UP * 2
        ]

        p3_pos = [
            RIGHT * 3 * 0.5 + UP * 2,
            RIGHT * 1 * 0.5 + UP * -2,
            LEFT * 4 * 0.5 + UP * 3
        ]
        
        def get_p2(x):
            i = math.floor(x)
            t = x % 1
            return p2_pos[i % len(p2_pos)] * (1 - t) + p2_pos[(i + 1) % len(p2_pos)] * t
    
        def get_p3(x):
            i = math.floor(x)
            t = x % 1
            return p3_pos[i % len(p3_pos)] * (1 - t) + p3_pos[(i + 1) % len(p3_pos)] * t

        lerp1 = lambda x: p1 * (1 - x) + get_p2(m.get_value()) * x
        lerp2 = lambda x: get_p2(m.get_value()) * (1 - x) + get_p3(m.get_value()) * x
        lerp3 = lambda x: get_p3(m.get_value()) * (1 - x) + p4 * x
        lerp4 = lambda x: lerp1(x) * (1 - x) + lerp2(x) * x
        lerp5 = lambda x: lerp2(x) * (1 - x) + lerp3(x) * x
        lerp6 = lambda x: lerp4(x) * (1 - x) + lerp5(x) * x

        lb1 = Line(p1, get_p2(m.get_value()), stroke_width=1).add_updater(lambda y: y.become(Line(p1, get_p2(m.get_value()), stroke_width=1)))
        lb2 = Line(get_p3(m.get_value()), p4, stroke_width=1).add_updater(lambda y: y.become(Line(get_p3(m.get_value()), p4, stroke_width=1)))
        lb3 = Line(get_p2(m.get_value()), get_p3(m.get_value()), stroke_width=1).add_updater(lambda y: y.become(Line(get_p2(m.get_value()), get_p3(m.get_value()), stroke_width=1)))
        self.add(lb1, lb2, lb3)

        d2 = Dot(get_p2(0), stroke_width=2, color=BLACK, stroke_color=WHITE).add_updater(lambda y: y.move_to(get_p2(m.get_value())))
        d3 = Dot(get_p3(0), stroke_width=2, color=BLACK, stroke_color=WHITE).add_updater(lambda y: y.move_to(get_p3(m.get_value())))
        self.add(d2, d3)

        t2 = MathTex(r"P_2").scale(0.75).move_to(get_p2(m.get_value()) + UP * 0.5).set_color(TEAL).add_updater(lambda y: y.move_to(get_p2(m.get_value()) + UP * 0.5))
        t3 = MathTex(r"P_3").scale(0.75).move_to(get_p3(m.get_value()) + UP * 0.5).set_color(GREEN).add_updater(lambda y: y.move_to(get_p3(m.get_value()) + UP * 0.5))
        self.add(t2, t3)

        l1 = Dot(lerp1(0.5)).add_updater(lambda y: y.move_to(lerp1(t.get_value())))
        l2 = Dot(lerp2(0.5)).add_updater(lambda y: y.move_to(lerp2(t.get_value())))
        l3 = Dot(lerp3(0.5)).add_updater(lambda y: y.move_to(lerp3(t.get_value())))
        self.add(l1, l2, l3)

        t1 = MathTex("a").scale(0.8).move_to(lerp1(0.5) + LEFT * 0.3).add_updater(lambda y: y.move_to(lerp1(t.get_value()) + LEFT * 0.3))
        t2 = MathTex("b").scale(0.8).move_to(lerp2(0.5) + UP * 0.3).add_updater(lambda y: y.move_to(lerp2(t.get_value()) + UP * 0.3))
        t3 = MathTex("c").scale(0.8).move_to(lerp3(0.5) + RIGHT * 0.3).add_updater(lambda y: y.move_to(lerp3(t.get_value()) + RIGHT * 0.3))
        self.add(t1, t2, t3)

        line1 = Line(lerp1(0.5), lerp2(0.5), stroke_width=1).add_updater(lambda y: y.become(Line(lerp1(t.get_value()), lerp2(t.get_value()), stroke_width=1)))
        line2 = Line(lerp2(0.5), lerp3(0.5), stroke_width=1).add_updater(lambda y: y.become(Line(lerp2(t.get_value()), lerp3(t.get_value()), stroke_width=1)))
        self.add(line1, line2)

        l4 = Dot(lerp4(0.5)).add_updater(lambda y: y.move_to(lerp4(t.get_value())))
        l5 = Dot(lerp5(0.5)).add_updater(lambda y: y.move_to(lerp5(t.get_value())))
        self.add(l4, l5)

        t4 = MathTex("d").scale(0.8).move_to(lerp4(0.5) + LEFT * 0.25 + UP * 0.25).add_updater(lambda y: y.move_to(lerp4(t.get_value())  + LEFT * 0.25 + UP * 0.25))
        t5 = MathTex("e").scale(0.8).move_to(lerp5(0.5) + RIGHT * 0.25 + UP * 0.25).add_updater(lambda y: y.move_to(lerp5(t.get_value())  + RIGHT * 0.25 + UP * 0.25))
        self.add(t4, t5)

        line3 = Line(lerp4(0.5), lerp5(0.5), stroke_width=1).add_updater(lambda y: y.become(Line(lerp4(t.get_value()), lerp5(t.get_value()), stroke_width=1)))
        self.add(line3)

        fd = Dot(lerp6(0.5), color=RED).add_updater(lambda y: y.move_to(lerp6(t.get_value()))).set_z_index(2000)
        self.add(fd)

        t6 = MathTex(r"P(t)", color=RED).scale(0.8).move_to(lerp6(0.5) + DOWN * 0.4).add_updater(lambda y: y.move_to(lerp6(t.get_value()) + DOWN * 0.4)).set_z_index(2000)
        self.add(t6)

        bezier = CubicBezier(p1, get_p2(0), get_p3(0), p4, color=RED) \
            .add_updater(lambda y: y.become(CubicBezier(p1, get_p2(m.get_value()), get_p3(m.get_value()), p4, color=RED)))
        self.add(bezier)

        # self.wait()
        self.play(m.animate.set_value(1), run_time=2)
        self.play(m.animate.set_value(2), run_time=2)
        self.play(m.animate.set_value(3), run_time=2)
        # self.wait()

class BezierSpline1(Scene):
    def construct(self):
        spline = [
            [(-6, 0, 0), (-4, 2, 0), (-2, -2, 0), (0, 0, 0)],
            [(0, 0, 0), (2, -2, 0), (4, -2, 0), (6, 0, 0)],
        ]

        colors = [RED, BLUE]

        for i, curve in enumerate(spline):
            bezier = CubicBezier(curve[0], curve[1], curve[2], curve[3], color=colors[i])
            self.add(bezier)

            for j, point in enumerate(curve):
                self.add(Dot(point))

                if j == 0 or j == 2:
                    self.add(Line(curve[j], curve[j + 1], stroke_width=1))

class BezierSpline2(Scene):
    def construct(self):
        v = ValueTracker(0)

        def get(x):
            return np.array((2, -2, 0)) * (1 - x) + np.array((2, 2, 0)) * x
        
        spline = [
            [(-6, 0, 0), (-4, 2, 0), (-2, -2, 0), (0, 0, 0)],
            [(0, 0, 0), get(0), (4, -2, 0), (6, 0, 0)],
        ]

        c1 = CubicBezier((-6, 0, 0), (-4, 2, 0), (-2, -2, 0), (0, 0, 0), color=RED)
        c2 = CubicBezier((0, 0, 0), get(v.get_value()), (4, -2, 0), (6, 0, 0), color=BLUE)
        c2.add_updater(lambda y: y.become(CubicBezier((0, 0, 0), get(v.get_value()), (4, -2, 0), (6, 0, 0), color=BLUE)))
        self.add(c1, c2)

        for j, point in enumerate(spline[0]):
            self.add(Dot(point))
            if j == 0 or j == 2:
                self.add(Line(spline[0][j], spline[0][j + 1], stroke_width=1))

        l1 = Line((0, 0, 0), get(v.get_value()), stroke_width=1)
        l1.add_updater(lambda y: y.become(Line((0, 0, 0), get(v.get_value()), stroke_width=1)))
        l2 = Line((4, -2, 0), (6, 0, 0), stroke_width=1)
        self.add(l1, l2)

        self.add(Dot((4, -2, 0)), Dot((6, 0, 0)))

        d1 = Dot(get(0)).add_updater(lambda y: y.move_to(get(v.get_value())))
        self.add(d1)

        self.wait()
        self.play(v.animate.set_value(1))
        self.wait()
        self.play(v.animate.set_value(0))
        self.wait()