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
