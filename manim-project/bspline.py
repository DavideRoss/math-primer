import numpy as np
from scipy import interpolate as scint
from manim import *

class BSpline(Scene):
    def construct(self):
        ctr = np.array([
            (3 , 1), (2.5, 4), (0, 1), (-2.5, 4),
            (-3, 0), (-2.5, -4), (0, -1), (2.5, -4), (3, -1)
        ])

        pg = []
        for x, y in ctr:
            pg.append((x, y, 0))
            # d = Dot((x, y, 0), color=GREEN)
            # self.add(d)

        cp = Polygram(pg)
        self.add(cp)

        x = ctr[:,0]
        y = ctr[:,1]

        l = len(x)  
        t = np.linspace(0, 1, l - 2, endpoint=True)
        t = np.append([0, 0, 0], t)
        t = np.append(t, [1, 1, 1])

        tck=[t, [x, y], 3]
        u3=np.linspace(0, 1, (max(l * 2 , 70)), endpoint=True)
        out = scint.splev(u3, tck)

        for i in range(len(out[0])):
            d = Dot((out[0][i], out[1][i], 0))
            self.add(d)