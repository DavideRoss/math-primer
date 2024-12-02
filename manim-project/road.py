from manim import *
import numpy as np
import math

spline = [
    [(-5.5, 2.75, 0), (-3, 3, 0), (-4, 0, 0), (-2, -1.5, 0)],
    [(-2, -1.5, 0), (0, -3, 0), (3, -3, 0), (4, -2, 0)],
    [(4, -2, 0), (5, -1, 0), (6, 2, 0), (3, 2.75, 0)],
    [(3, 2.75, 0), (-3, 3.5, 0), (-2, -1, 0), (2, 0, 0)]
]

width = 0.75

# =================================================================================
# =================================================================================

def norm(p):
    return p / np.linalg.norm(p)

def position(x):
    i = math.floor(x) % len(spline)
    p1, p2, p3, p4 = spline[i]
    f = x % 1
    i = 1 - f

    return  i ** 3 * np.array(p1) + \
            3 * i ** 2 * f * np.array(p2) + \
            3 * i * f ** 2 * np.array(p3) + \
            f ** 3 * np.array(p4)

def velocity(x):
    i = math.floor(x) % len(spline)
    p1, p2, p3, p4 = spline[i]
    f = x % 1
    i = 1 - f

    return  3 * i ** 2 * (np.array(p2) - np.array(p1)) + \
            6 * i * f * (np.array(p3) - np.array(p2)) + \
            3 * f ** 2 * (np.array(p4) - np.array(p3))

def acceleration(x):
    i = math.floor(x) % len(spline)
    p1, p2, p3, p4 = spline[i]
    f = x % 1
    i = 1 - f

    return  6 * i * (np.array(p3) - 2 * np.array(p2) + np.array(p1)) + \
            6 * f * (np.array(p4) - 2 * np.array(p3) + np.array(p2))

def curvature(x):
    vel = velocity(x)
    accel = acceleration(x)
    cross = np.abs(vel[0] * accel[1] - vel[1] * accel[0])
    return cross / (np.linalg.norm(vel) ** 3)

def get_length(dt=0.01, end=-1):
    if end < 0:
        end = len(spline)

    t = 0
    length = 0
    last_point = spline[0][0]

    while t <= end:
        new_point = position(t)
        length += math.dist(new_point, last_point)
        last_point = new_point
        t += dt

    return length

times = []
distances = []

def build_lut(dt=0.01):
    t = 0
    length = 0
    last_point = spline[0][0]

    while t <= len(spline):
        new_point = position(t)
        length += math.dist(new_point, last_point)
        last_point = new_point

        times.append(t)
        distances.append(length)

        t += dt

def remap(x, omin, omax, nmin, nmax):
    orange = omax - omin
    nrange = nmax - nmin
    return (((x - omin) * nrange) / orange) + nmin

def d2t(d):
    for i in range(len(distances) - 1):
        if distances[i] <= d and distances[i + 1] > d:
            return remap(
                d,
                distances[i], distances[i + 1],
                times[i], times[i + 1]
            )
        
    return d / get_length()
            
# =================================================================================
# =================================================================================

def BaseBezier(scene):
    for i, curve in enumerate(spline):
        bezier = CubicBezier(curve[0], curve[1], curve[2], curve[3], color=RED)
        scene.add(bezier)

        if i == 0:
            scene.add(Dot(curve[0], radius=0.06, color=RED).set_z_index(10))
        scene.add(Dot(curve[3], radius=0.06, color=RED).set_z_index(10))

def build_segment(scene, t, line=True):
    pos = position(t)
    tangent = norm(velocity(t))
    normal = np.array((tangent[1], -tangent[0], 0))
    binormal = np.array((-tangent[1], tangent[0], 0))

    scene.add(Dot(pos).set_z_index(10))
    if line:
        scene.add(Line(pos + normal * width, pos + binormal * width, stroke_width = 1))
        scene.add(Dot(pos + normal * width), Dot(pos + binormal * width))

    return pos, tangent, normal, binormal

# =================================================================================
# =================================================================================

class Road1(Scene):
    def construct(self):
        BaseBezier(self)

class Road2(Scene):
    def construct(self):
        BaseBezier(self)

        t = 0.8
        pos = position(t)
        self.add(Dot(pos))

class Road3(Scene):
    def construct(self):
        BaseBezier(self)

        t = 0.8
        pos = position(t)
        tangent = norm(velocity(t))

        self.add(Dot(pos).set_z_index(10))
        self.add(Arrow(start=pos, end=pos + tangent, buff=0, color=GREEN))

class Road4(Scene):
    def construct(self):
        BaseBezier(self)

        t = 0.8
        pos = position(t)
        tangent = norm(velocity(t))
        normal = (tangent[1], -tangent[0], 0)

        self.add(Dot(pos).set_z_index(10))
        self.add(Arrow(start=pos, end=pos + tangent, buff=0, color=GREEN))
        self.add(Arrow(start=pos, end=pos + normal, buff=0, color=BLUE))

class Road5(Scene):
    def construct(self):
        BaseBezier(self)

        t = 0.8
        pos, tangent, normal, _ = build_segment(self, t)
        self.add(Arrow(start=pos, end=pos + tangent, buff=0, color=GREEN))
        self.add(Arrow(start=pos, end=pos + normal, buff=0, color=BLUE).set_z_index(8))

class Road6(Scene):
    def construct(self):
        BaseBezier(self)

        dt = 0.24999
        t = 0
        while t <= len(spline):
            build_segment(self, t)
            t += dt


def track(scene, vertices):
    for i in range(0, len(vertices) - 1):
        scene.add(Line(vertices[i], vertices[i + 1]))

class Road7(Scene):
    def construct(self):
        BaseBezier(self)

        top = []
        bottom = []

        dt = 0.24999
        t = 0
        while t <= len(spline):
            pos, _, normal, binormal = build_segment(self, t)
            top.append(pos + normal * width)
            bottom.append(pos + binormal * width)
            t += dt

        track(self, top)
        track(self, bottom)

class Road8(Scene):
    def construct(self):
        BaseBezier(self)

        top = []
        bottom = []

        dt = 0.09999
        t = 0
        while t <= len(spline):
            pos, _, normal, binormal = build_segment(self, t)
            top.append(pos + normal * width)
            bottom.append(pos + binormal * width)
            t += dt

        track(self, top)
        track(self, bottom)

class Road9(Scene):
    def construct(self):
        BaseBezier(self)

        build_lut()

        top = []
        bottom = []

        total_length = get_length()
        segments = 30
        dt = total_length / segments - 0.0001
        t = 0
        while t <= total_length:
            pos, _, normal, binormal = build_segment(self, d2t(t))
            top.append(pos + normal * width)
            bottom.append(pos + binormal * width)
            t += dt

        track(self, top)
        track(self, bottom)

class Road10(Scene):
    def construct(self):
        BaseBezier(self)

        build_lut()

        top = []
        bottom = []

        total_length = get_length()
        segments = 30
        dt = total_length / segments - 0.0001
        t = 0
        while t <= total_length:
            new_t = d2t(t)

            if curvature(new_t) >= 0.175:
                pos, _, normal, binormal = build_segment(self, new_t)
                top.append(pos + normal * width)
                bottom.append(pos + binormal * width)

            t += dt

        track(self, top)
        track(self, bottom)