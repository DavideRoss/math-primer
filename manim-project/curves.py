import numpy as np
from scipy import interpolate as scint
from manim import *

class BSpline(Scene):
    def construct(self):
        ctr = np.array([
            (3 , 0), (2.5, 3.5), (0, -1), (-2.5, 3.5), (-3, 0)
        ])

        for i in range(len(ctr) - 1):
            self.add(Line(
                (ctr[i][0], ctr[i][1], 0),
                (ctr[i + 1][0], ctr[i + 1][1], 0),
                stroke_width=1
            ))

        x = ctr[:,0]
        y = ctr[:,1]

        l = len(x)  
        t = np.linspace(0, 1, l - 2, endpoint=True)
        t = np.append([0, 0, 0], t)
        t = np.append(t, [1, 1, 1])

        tck=[t, [x, y], 3]
        u3=np.linspace(0, 1, (max(l * 2 , 70)), endpoint=True)
        out = scint.splev(u3, tck)

        for i in range(len(out[0]) - 1):
            self.add(Line(
                (out[0][i], out[1][i], 0),
                (out[0][i + 1], out[1][i + 1], 0),
                color=RED
            ))

        self.add(Dot((out[0][0], out[1][0], 0)))
        self.add(Dot((out[0][-1], out[1][-1], 0)))

class Hermite(Scene):
    def construct(self):
        pts = [(-3, 0, 0), (3, 0, 0)]
        tans = [(5, 10, 0), (-5, 10, 0)]

        def hermite(p0, p1, t0, t1):
            t = np.linspace(0, 1, 100)

            h1 = 2 * t ** 3 - 3 * t ** 2 + 1
            h2 = -2 * t ** 3 + 3 * t ** 2
            h3 = t ** 3 - 2 * t ** 2 + t
            h4 = t ** 3 - t ** 2

            x = h1 * p0[0] + h2 * p1[0] + h3 * t0[0] + h4 * t1[0]
            y = h1 * p0[1] + h2 * p1[1] + h3 * t0[1] + h4 * t1[1]

            return x, y
        
        x, y = hermite(pts[0], pts[1], tans[0], tans[1])
        
        for i in range(len(x) - 1):
            self.add(Line(
                (x[i], y[i], 0),
                (x[i + 1], y[i + 1], 0),
                color=RED
            ))

        self.add(
            Arrow(
                start=(x[0], y[0], 0),
                end=(x[0], y[0], 0) + (np.array(tans[0]) / np.linalg.norm(np.array(tans[0])) * 2.0),
                buff=0,
                color=BLUE
            )
        )

        self.add(
            Arrow(
                start=(x[-1], y[-1], 0),
                end=(x[-1], y[-1], 0) + (np.array(tans[1]) / np.linalg.norm(np.array(tans[1])) * 2.0),
                buff=0,
                color=BLUE
            )
        )

        self.add(
            Dot((x[0], y[0], 0)),
            Dot((x[-1], y[-1], 0)),
        )

class CatmullRom(Scene):
    def construct(self):
        pts = [
            (-3, -2, 0), (-1, 2, 0), (1, -2, 0), (3, 2, 0)
        ]

        def catmull(p0, p1, p2, p3):
            tau = 0.5
            p0 = np.array(p0)
            p1 = np.array(p1)
            p2 = np.array(p2)
            p3 = np.array(p3)

            pts = []
            t = 0
            while t <= 1:
                pt = tau * (
                    (2.0 * p1) + \
                    (-p0 + p2) * t + \
                    (2 * p0 - 5 * p1 + 4 * p2 - p3) * t ** 2 + \
                    (-p0 + 3 * p1 - 3 * p2 + p3) * t ** 3
                )

                pts.append(pt)

                t += 1 / 100
            
            return pts
        
        def display(p0, p1, p2, p3, color=RED, stroke_width=2):
            cat = catmull(p0, p1, p2, p3)

            for i in range(len(cat) - 1):
                self.add(Line(
                    (cat[i][0], cat[i][1], 0),
                    (cat[i + 1][0], cat[i + 1][1], 0),
                    color=color,
                    stroke_width=stroke_width
                ))

        display(pts[0], pts[1], pts[2], pts[3],stroke_width=5)
        display((4, 0, 0), pts[0], pts[1], pts[2], stroke_width=1)
        display(pts[1], pts[2], pts[3], (-3.5, 3.5, 0), stroke_width=1)

        for p in pts:
            self.add(Dot(p))
        