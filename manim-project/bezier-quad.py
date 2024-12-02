from manim import *

class Lerp1(Scene):
    def construct(self):
        v = ValueTracker(0.5)

        gap = 3

        p1 = LEFT * gap
        p2 = RIGHT * gap

        l = Line(p1, p2, stroke_width=1)
        self.add(l)

        d1 = Dot(p1, radius=0.12, stroke_width=3, color=RED, stroke_color=RED_E)
        d2 = Dot(p2, radius=0.12, stroke_width=3, color=BLUE, stroke_color=BLUE_E)
        self.add(d1, d2)

        t1 = MathTex(r"P_0")
        t1.move_to(p1 + LEFT)
        t1.set_color(RED)
        self.add(t1)

        t2 = MathTex(r"P_1")
        t2.move_to(p2 + RIGHT)
        t2.set_color(BLUE)
        self.add(t2)

        def lerp1():
            return p1 * (1 - v.get_value()) + p2 * v.get_value()
        
        d3 = Dot(lerp1(), radius=0.08)
        d3.add_updater(lambda y: y.move_to(lerp1()))
        self.add(d3)

        t3 = MathTex(r"P_A")
        t3.move_to(lerp1() + DOWN * 0.6)
        t3.add_updater(lambda y: y.move_to(lerp1() + DOWN * 0.6))
        self.add(t3)

        self.wait()
        self.play(v.animate.set_value(1))
        self.play(v.animate.set_value(0))
        self.play(v.animate.set_value(0.5))
        self.wait()

class Lerp2(Scene):
    def construct(self):
        v = ValueTracker(0.5)

        gap = 3

        p1 = LEFT * gap + DOWN * 1.5
        p2 = UP * gap + DOWN * 1.5
        p3 = RIGHT * gap + DOWN * 1.5

        l1 = Line(p1, p2, stroke_width=1)
        l2 = Line(p2, p3, stroke_width=1)
        self.add(l1, l2)

        d1 = Dot(p1, radius=0.12, stroke_width=3, color=RED, stroke_color=RED_E)
        d2 = Dot(p2, radius=0.12, stroke_width=3, color=BLUE, stroke_color=BLUE_E)
        d3 = Dot(p3, radius=0.12, stroke_width=3, color=GREEN, stroke_color=GREEN_E)
        self.add(d1, d2, d3)

        t1 = MathTex(r"P_0")
        t1.move_to(p1 + DOWN * 0.6 + LEFT * 0.6)
        t1.set_color(RED)
        self.add(t1)

        t2 = MathTex(r"P_1")
        t2.move_to(p2 + UP * 0.6)
        t2.set_color(BLUE)
        self.add(t2)

        t3 = MathTex(r"P_2")
        t3.move_to(p3 + DOWN * 0.6 + RIGHT * 0.6)
        t3.set_color(GREEN)
        self.add(t3)

        def lerp1(x=-1):
            if x == -1:
                x = v.get_value()

            return p1 * (1 - x) + p2 * x
        
        def lerp2(x=-1):
            if x == -1:
                x = v.get_value()

            return p2 * (1 - x) + p3 * x
        
        d3 = Dot(lerp1(), radius=0.08)
        d3.add_updater(lambda y: y.move_to(lerp1()))
        self.add(d3)

        d4 = Dot(lerp2(), radius=0.08)
        d4.add_updater(lambda y: y.move_to(lerp2()))
        self.add(d4)

        t3 = MathTex(r"P_A")
        t3.scale(0.75)
        t3.move_to(lerp1() + UP * 0.5 + LEFT * 0.5)
        self.add(t3)

        t4 = MathTex(r"P_B")
        t4.scale(0.75)
        t4.move_to(lerp2() + UP * 0.5 + RIGHT * 0.5)
        self.add(t4)

class Lerp3(Scene):
    def construct(self):
        v = ValueTracker(0.5)

        gap = 3

        p1 = LEFT * gap + DOWN * 1.5
        p2 = UP * gap + DOWN * 1.5
        p3 = RIGHT * gap + DOWN * 1.5

        l1 = Line(p1, p2, stroke_width=1)
        l2 = Line(p2, p3, stroke_width=1)
        self.add(l1, l2)

        d1 = Dot(p1, radius=0.12, stroke_width=3, color=RED, stroke_color=RED_E)
        d2 = Dot(p2, radius=0.12, stroke_width=3, color=BLUE, stroke_color=BLUE_E)
        d3 = Dot(p3, radius=0.12, stroke_width=3, color=GREEN, stroke_color=GREEN_E)
        self.add(d1, d2, d3)

        t1 = MathTex(r"P_0")
        t1.move_to(p1 + DOWN * 0.6 + LEFT * 0.6)
        t1.set_color(RED)
        self.add(t1)

        t2 = MathTex(r"P_1")
        t2.move_to(p2 + UP * 0.6)
        t2.set_color(BLUE)
        self.add(t2)

        t3 = MathTex(r"P_2")
        t3.move_to(p3 + DOWN * 0.6 + RIGHT * 0.6)
        t3.set_color(GREEN)
        self.add(t3)

        def lerp1(x=-1):
            if x == -1:
                x = v.get_value()

            return p1 * (1 - x) + p2 * x
        
        def lerp2(x=-1):
            if x == -1:
                x = v.get_value()

            return p2 * (1 - x) + p3 * x
        
        d3 = Dot(lerp1(), radius=0.08)
        d3.add_updater(lambda y: y.move_to(lerp1()))
        self.add(d3)

        d4 = Dot(lerp2(), radius=0.08)
        d4.add_updater(lambda y: y.move_to(lerp2()))
        self.add(d4)

        t3 = MathTex(r"P_A")
        t3.scale(0.75)
        t3.move_to(lerp1() + UP * 0.5 + LEFT * 0.5)
        t3.add_updater(lambda y: y.move_to(lerp1() + UP * 0.5 + LEFT * 0.5))
        self.add(t3)

        t4 = MathTex(r"P_B")
        t4.scale(0.75)
        t4.move_to(lerp2() + UP * 0.5 + RIGHT * 0.5)
        t4.add_updater(lambda y: y.move_to(lerp2() + UP * 0.5 + RIGHT * 0.5))
        self.add(t4)

        self.wait()
        self.play(v.animate.set_value(1), run_time=1.5)
        self.play(v.animate.set_value(0), run_time=3)
        self.play(v.animate.set_value(0.5), run_time=1.5)
        self.wait()

class Lerp4(Scene):
    def construct(self):
        v = ValueTracker(0.5)

        gap = 3

        p1 = LEFT * gap + DOWN * 1.5
        p2 = UP * gap + DOWN * 1.5
        p3 = RIGHT * gap + DOWN * 1.5

        l1 = Line(p1, p2, stroke_width=1)
        l2 = Line(p2, p3, stroke_width=1)
        self.add(l1, l2)

        d1 = Dot(p1, radius=0.12, stroke_width=3, color=RED, stroke_color=RED_E)
        d2 = Dot(p2, radius=0.12, stroke_width=3, color=BLUE, stroke_color=BLUE_E)
        d3 = Dot(p3, radius=0.12, stroke_width=3, color=GREEN, stroke_color=GREEN_E)
        self.add(d1, d2, d3)

        t1 = MathTex(r"P_0")
        t1.move_to(p1 + DOWN * 0.6 + LEFT * 0.6)
        t1.set_color(RED)
        self.add(t1)

        t2 = MathTex(r"P_1")
        t2.move_to(p2 + UP * 0.6)
        t2.set_color(BLUE)
        self.add(t2)

        t3 = MathTex(r"P_2")
        t3.move_to(p3 + DOWN * 0.6 + RIGHT * 0.6)
        t3.set_color(GREEN)
        self.add(t3)

        def lerp1(x=-1):
            if x == -1:
                x = v.get_value()

            return p1 * (1 - x) + p2 * x
        
        def lerp2(x=-1):
            if x == -1:
                x = v.get_value()

            return p2 * (1 - x) + p3 * x
        
        def lerp3():
            return lerp1() * (1 - v.get_value()) + lerp2() * v.get_value()
        
        d3 = Dot(lerp1(), radius=0.08)
        d3.add_updater(lambda y: y.move_to(lerp1()))
        self.add(d3)

        d4 = Dot(lerp2(), radius=0.08)
        d4.add_updater(lambda y: y.move_to(lerp2()))
        self.add(d4)

        d5 = Dot(lerp3(), radius=0.08)
        d5.add_updater(lambda y: y.move_to(lerp3()))
        self.add(d5)

        t3 = MathTex(r"P_A")
        t3.scale(0.75)
        t3.move_to(lerp1() + UP * 0.5 + LEFT * 0.5)
        t3.add_updater(lambda y: y.move_to(lerp1() + UP * 0.5 + LEFT * 0.5))
        self.add(t3)

        t4 = MathTex(r"P_B")
        t4.scale(0.75)
        t4.move_to(lerp2() + UP * 0.5 + RIGHT * 0.5)
        t4.add_updater(lambda y: y.move_to(lerp2() + UP * 0.5 + RIGHT * 0.5))
        self.add(t4)

        t5 = MathTex(r"P_C")
        t5.scale(0.75)
        t5.move_to(lerp3() + DOWN * 0.5)
        t5.add_updater(lambda y: y.move_to(lerp3() + DOWN * 0.5))
        self.add(t5)

        l2 = Line(lerp1(), lerp2(), stroke_width=1)
        l2.add_updater(lambda y: y.become(Line(lerp1(), lerp2(), stroke_width=1)))
        self.add(l2)

        self.wait()
        self.play(v.animate.set_value(1), run_time=1.5)
        self.play(v.animate.set_value(0), run_time=3)
        self.play(v.animate.set_value(0.5), run_time=1.5)
        self.wait()

class Lerp5(Scene):
    def construct(self):
        v = ValueTracker(0.5)

        gap = 3

        p1 = LEFT * gap + DOWN * 1.5
        p2 = UP * gap + DOWN * 1.5
        p3 = RIGHT * gap + DOWN * 1.5

        l1 = Line(p1, p2, stroke_width=1)
        l2 = Line(p2, p3, stroke_width=1)
        self.add(l1, l2)

        d1 = Dot(p1, radius=0.12, stroke_width=3, color=RED, stroke_color=RED_E)
        d2 = Dot(p2, radius=0.12, stroke_width=3, color=BLUE, stroke_color=BLUE_E)
        d3 = Dot(p3, radius=0.12, stroke_width=3, color=GREEN, stroke_color=GREEN_E)
        self.add(d1, d2, d3)

        t1 = MathTex(r"P_0")
        t1.move_to(p1 + DOWN * 0.6 + LEFT * 0.6)
        t1.set_color(RED)
        self.add(t1)

        t2 = MathTex(r"P_1")
        t2.move_to(p2 + UP * 0.6)
        t2.set_color(BLUE)
        self.add(t2)

        t3 = MathTex(r"P_2")
        t3.move_to(p3 + DOWN * 0.6 + RIGHT * 0.6)
        t3.set_color(GREEN)
        self.add(t3)

        def lerp1(x=-1):
            if x == -1:
                x = v.get_value()

            return p1 * (1 - x) + p2 * x
        
        def lerp2(x=-1):
            if x == -1:
                x = v.get_value()

            return p2 * (1 - x) + p3 * x
        
        def lerp3():
            return lerp1() * (1 - v.get_value()) + lerp2() * v.get_value()
        
        d3 = Dot(lerp1(), radius=0.08)
        d3.add_updater(lambda y: y.move_to(lerp1()))
        self.add(d3)

        d4 = Dot(lerp2(), radius=0.08)
        d4.add_updater(lambda y: y.move_to(lerp2()))
        self.add(d4)

        def norm_lerp(x):
            f = (x + 3) / 6
            finv = 1 - f
            return -1.5 * finv * finv + 2 * f * finv * 1.5 + f * f * -1.5
        
        bez = FunctionGraph(lambda x: norm_lerp(x), [-gap, gap, 0.1], color=RED)
        self.add(bez)

        d5 = Dot(lerp3(), radius=0.08)
        d5.add_updater(lambda y: y.move_to(lerp3()))
        self.add(d5)

        t3 = MathTex(r"P_A")
        t3.scale(0.75)
        t3.move_to(lerp1() + UP * 0.5 + LEFT * 0.5)
        t3.add_updater(lambda y: y.move_to(lerp1() + UP * 0.5 + LEFT * 0.5))
        self.add(t3)

        t4 = MathTex(r"P_B")
        t4.scale(0.75)
        t4.move_to(lerp2() + UP * 0.5 + RIGHT * 0.5)
        t4.add_updater(lambda y: y.move_to(lerp2() + UP * 0.5 + RIGHT * 0.5))
        self.add(t4)

        t5 = MathTex(r"P_C")
        t5.scale(0.75)
        t5.move_to(lerp3() + DOWN * 0.5)
        t5.add_updater(lambda y: y.move_to(lerp3() + DOWN * 0.5))
        self.add(t5)

        l2 = Line(lerp1(), lerp2(), stroke_width=1)
        l2.add_updater(lambda y: y.become(Line(lerp1(), lerp2(), stroke_width=1)))
        self.add(l2)

        self.wait()
        self.play(v.animate.set_value(1), run_time=1.5)
        self.play(v.animate.set_value(0), run_time=3)
        self.play(v.animate.set_value(0.5), run_time=1.5)
        self.wait()

class Lerp6(Scene):
    def construct(self):
        v = ValueTracker(0)

        gap = 3
        e_width = 3
        e_height = 2
        traj = Ellipse(e_width, e_height).move_to(UP * (gap - e_height / 2) + DOWN * 1.5)

        def f():
            return traj.point_at_angle(PI * 2 * v.get_value() + PI / 2)
        
        def lerp1(x=-1):
            x = v.get_value() if x == 1 else x
            return p1 * (1 - x) + f() * x
        
        def lerp2(x=-1):
            x = v.get_value() if x == 1 else x
            return f() * (1 - x) + p3 * x
        
        def lerp3(x=-1):
            x = v.get_value() if x == 1 else x
            return lerp1(x) * (1 - x) + lerp2(x) * x

        p1 = LEFT * gap + DOWN * 1.5
        p2 = UP * gap + DOWN * 1.5
        p3 = RIGHT * gap + DOWN * 1.5

        l1 = Line(p1, p2, stroke_width=1)
        l2 = Line(p2, p3, stroke_width=1)
        self.add(l1, l2)

        d1 = Dot(p1, radius=0.12, stroke_width=3, color=RED, stroke_color=RED_E)
        d2 = Dot(p2, radius=0.12, stroke_width=3, color=BLUE, stroke_color=BLUE_E)
        d3 = Dot(p3, radius=0.12, stroke_width=3, color=GREEN, stroke_color=GREEN_E)
        self.add(d1, d2, d3)        

        t1 = MathTex(r"P_0").move_to(p1 + DOWN * 0.6 + LEFT * 0.6).set_color(RED)
        t2 = MathTex(r"P_1").move_to(p2 + UP * 0.6).set_color(BLUE)
        t3 = MathTex(r"P_2").move_to(p3 + DOWN * 0.6 + RIGHT * 0.6).set_color(GREEN)
        self.add(t1, t2, t3)

        pa = Dot(lerp1(0.5))
        pb = Dot(lerp2(0.5))
        pc = Dot(lerp3(0.5))
        self.add(pa, pb, pc)

        d2.add_updater(lambda y: y.move_to(f()))
        t2.add_updater(lambda y: y.move_to(UP * 0.6 + f()))
        l1.add_updater(lambda y: y.become(Line(p1, f(), stroke_width=1)))
        l2.add_updater(lambda y: y.become(Line(p3, f(), stroke_width=1)))

        self.play(v.animate.set_value(1), run_time=5)