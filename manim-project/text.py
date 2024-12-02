from manim import *

class TextSin(Scene):
    def construct(self):
        t = MathTex(r"f(x) = sin(x)")
        t.scale(3)

        self.add(t)

class TextSquare(Scene):
    def construct(self):
        t = MathTex(r"f(x) = x^2")
        t.scale(3)

        self.add(t)

class TextTan(Scene):
    def construct(self):
        t = MathTex(r"f(x) = tan(x)")
        t.scale(3)

        self.add(t)

class TextTan2(Scene):
    def construct(self):
        t = MathTex(r"f(x) = \frac{sin(x)}{cos(x)}")
        t.scale(3)

        self.add(t)

class TextCircle(Scene):
    def construct(self):
        t = MathTex(r"y^2 + x^2 = r")
        t.scale(3)

        self.add(t)

class TextRandom(Scene):
    def construct(self):
        t = MathTex(r"f(x) = \mathord{?}\mathord{?}")
        t.scale(3)

        self.add(t)

class DerPower(Scene):
    def construct(self):
        t = MathTex(r"\frac{d}{dx} x^a = ax^{a-1}")
        t.scale(3)
        self.add(t)

class DerNatLog(Scene):
    def construct(self):
        t = MathTex(r"\frac{d}{dx} e^x = e^x")
        t.scale(3)
        self.add(t)

class DerSinLoop(Scene):
    def construct(self):
        t1 = MathTex(r"\frac{d}{dx}\sin(x) = \cos(x)").move_to(UP * 2).scale(1)
        t2 = MathTex(r"\frac{d}{dx}\cos(x) = -\sin(x)").move_to(LEFT * -3).scale(1)
        t3 = MathTex(r"\frac{d}{dx}-\sin(x) = -\cos(x)").move_to(UP * -2 ).scale(1)
        t4 = MathTex(r"\frac{d}{dx}-\cos(x) = \sin(x)").move_to(LEFT * 3).scale(1)

        ca = Arc(1, 0, PI / 2, arc_center=[0, 0, 0]).rotate(-PI / 50)
        c1 = ca.copy().move_to(-3.5 * LEFT + 1.5 * UP).add_tip(at_start=True)
        c2 = c1.copy().rotate(-PI / 2).move_to(-3.5 * LEFT -1.5 * UP)
        c3 = c2.copy().rotate(-PI / 2).move_to(3.5 * LEFT -1.5 * UP)
        c4 = c3.copy().rotate(-PI / 2).move_to(3.5 * LEFT +1.5 * UP)

        self.add(t1, t2, t3, t4)
        self.add(c1, c2, c3, c4)

class PhysicsForce(Scene):
    def construct(self):
        t = MathTex(r"F = ma")
        t.scale(3)
        self.add(t)

class PhysicsAccel1(Scene):
    def construct(self):
        t = MathTex(r"a = \frac{F}{m}")
        t.scale(3)
        self.add(t)

class PhysicsAccel2(Scene):
    def construct(self):
        t = MathTex(r"a = \frac{\Delta v}{\Delta t}")
        t.scale(3)
        self.add(t)

class PhysicsVel(Scene):
    def construct(self):
        t = MathTex(r"v = \frac{\Delta x}{\Delta t}")
        t.scale(3)
        self.add(t)

class NumImplEuler1(Scene):
    def construct(self):
        t = MathTex(r"v_{n+1} = v_n+a\Delta t")
        t.scale(1.5)
        self.add(t)

class NumImplEuler2(Scene):
    def construct(self):
        t = MathTex(r"x_{n+1}=x_n+v_{n+1}\Delta t")
        t.scale(1.5)
        self.add(t)

class NumVerlet(Scene):
    def construct(self):
        t = MathTex(r"x_{n+1} = x_n+(x_n-x_{n-1})+a\Delta t^2")
        t.scale(1.5)
        self.add(t)
class Riemann1(Scene):
    def construct(self):
        f = MathTex(r"\int_{a}^{b} f(x)dx \approx \lim_{n \to \infty} \sum_{i=1}^{n} f(x)dx")
        f.scale(2)
        self.add(f)

class Riemann2(Scene):
    def construct(self):
        f = MathTex(r"dx = \frac{b-a}{n}")
        f.scale(2)
        self.add(f)

class CubicBezier(Scene):
    def construct(self):
        form = VGroup()
        initial = MathTex("B(t) = ").set_color(RED)
        form.add(initial)

        pg = VGroup()
        pg.add(MathTex(r"(1 - t)^3 P_1 +").set_color(PURPLE_A))
        pg.add(MathTex(r"3(1 - t)^2t P_2 +").set_color(TEAL))
        pg.add(MathTex(r"3(1 - t)^2 P_3 +").set_color(GREEN))
        pg.add(MathTex(r"t^3 P_4").set_color(YELLOW))

        pg.arrange(DOWN, center=False, aligned_edge=LEFT)
        
        form.add(pg)
        form.arrange(RIGHT, aligned_edge=UP)

        initial.move_to(initial.get_center() + DOWN * 0.05)
        form.scale(1.5)
        self.add(form)

class Lerp(Scene):
    def construct(self):
        f = MathTex(r"f = (1-t)x + ty")
        f.scale(3)
        self.add(f)

class CubicDerivative0(Scene):
    def construct(self):
        form = VGroup()
        initial = MathTex("B(t) = ")
        form.add(initial)

        pg = VGroup()
        pg.add(MathTex(r"(1 - t)^3 P_1 +"))
        pg.add(MathTex(r"3(1 - t)^2t P_2 +"))
        pg.add(MathTex(r"3(1 - t)^2 P_3 +"))
        pg.add(MathTex(r"t^3 P_4"))

        pg.arrange(DOWN, center=False, aligned_edge=LEFT)
        
        form.add(pg)
        form.arrange(RIGHT, aligned_edge=UP)

        initial.move_to(initial.get_center() + DOWN * 0.05)
        form.scale(1.5)
        self.add(form)

class CubicDerivative1(Scene):
    def construct(self):
        form = VGroup()
        initial = MathTex("B'(t) = ")
        form.add(initial)

        pg = VGroup()
        pg.add(MathTex(r"3(1 - t)^2 (P_2 - P_1) +"))
        pg.add(MathTex(r"6(1 - t)t(P_3 - P_2) + "))
        pg.add(MathTex(r"3t^2(P_4 - P_3)"))

        pg.arrange(DOWN, center=False, aligned_edge=LEFT)
        
        form.add(pg)
        form.arrange(RIGHT, aligned_edge=UP)

        initial.move_to(initial.get_center() + DOWN * 0.05)
        form.scale(1.5)
        self.add(form)

class CubicDerivative2(Scene):
    def construct(self):
        form = VGroup()
        initial = MathTex("B''(t) = ")
        form.add(initial)

        pg = VGroup()
        pg.add(MathTex(r"6(1 - t)(P_3 - 2P_2 + P_1) +"))
        pg.add(MathTex(r"6t(1 - t)(P_4 - 2P_3 + P_2)"))

        pg.arrange(DOWN, center=False, aligned_edge=LEFT)
        
        form.add(pg)
        form.arrange(RIGHT, aligned_edge=UP)

        initial.move_to(initial.get_center() + DOWN * 0.05)
        form.scale(1.5)
        self.add(form)