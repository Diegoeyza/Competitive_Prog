from dataclasses import dataclass
from itertools import islice, cycle
from typing import List
import math
from sys import stdin
import io

EPS = 1E-8
@dataclass
class point:
    x: float
    y: float

    def __add__(self, t):
        return point(self.x + t.x, self.y + t.y)
    def __sub__(self, t):
        return point(self.x - t.x, self.y - t.y)
    def dot(self, a):
        return self.x*a.x + self.y*a.y

    def norm(self):
        return math.sqrt(self.dot(self))
    
    def rotate(self, theta):
        return point(
            self.x*math.cos(theta) + self.y*math.sin(theta),
            self.x*math.sin(theta) - self.y*math.cos(theta),
        )
    
    def angle(self, a, c):
        s1 = a - self
        d1 = s1.norm()

        s2 = c - self
        d2 = s2.norm()

        return math.acos(s1.dot(s2)/(d1*d2))

    def cross(self, p):
        return self.x*p.y - p.x*self.y
    


@dataclass
class line:
    a: float
    b: float
    c: float

    @staticmethod
    def from_points(p1, p2):
        if abs(p1.x - p2.x) < EPS:
            return line(1.0, 0.0, -p1.x)
        else:
            a = -(p1.y - p2.y) / (p1.x - p2.x)
            b = 1.0
            c = -(a * p1.x) - p1.y
            return line(a, b, c)
        
    def slope(self):
        return -self.a / self.b
    def y_cross(self):
        return -self.c / self.b
    def x_cross(self):
        return -self.c / self.a
    
    def normal(self):
        return point(
            self.a / math.sqrt(self.a**2 + self.b**2),
            self.b / math.sqrt(self.a**2 + self.b**2)
        )
    def d(self):
        return -self.c / math.sqrt(self.a**2 + self.b**2)
    
    def intersect(self, l):
        return point(
            (self.b*l.c - l.b*self.c)/ (self.a*l.b - l.a*self.b),
            (self.a*l.c - l.a*self.c)/ (self.a*l.b - l.a*self.b)
        )
    
    def are_parallel(self, line):
        return abs(
            (self.a*line.a* + self.b*line.b)
            / (math.sqrt(self.a**2 + self.b**2)*math.sqrt(line.a**2 + line.b**2))
        - 1.0) < EPS
    
    def angle(self, line):
        return math.acos(
            (self.a*line.a + self.b*line.b)
            / (math.sqrt(self.a**2 + self.b**2)*math.sqrt(line.a**2+line.b**2))
        )

# @dataclass
# class segment:
#     p: point
#     q: point

#     def does_intersect(self, seg2, *, include_p=False, include_q=False):
#         cross1 = (seg2.q - self.p).cross(self.q - self.p)
#         cross2 = (seg2.p - self.p).cross(self.q - self.p)
#         cross3 = (self.q - seg2.p).cross(seg2.q - seg2.p)
#         cross4 = (self.p - seg2.p).cross(seg2.q - seg2.p)
#         return (
#             (cross1 * cross2 < 0 or
#                 (include_p and math.fabs(cross2) < EPS)
#                 or (include_q and math.fabs(cross1) < EPS))
#             and (cross3 * cross4 < 0
#                 or (include_p and math.fabs(cross4) < EPS)
#                 or (include_q and math.fabs(cross3) < EPS))
#         )



@dataclass
class segment:
    p: point
    q: point

    def does_intersect(self, seg2, *, include_p=False, include_q=False):
        """Checks if two segments intersect, considering endpoints and collinear overlap."""
        
        def on_segment(p, q, r):
            """Checks if point r lies on segment pq when collinear."""
            return min(p.x, q.x) <= r.x <= max(p.x, q.x) and min(p.y, q.y) <= r.y <= max(p.y, q.y)

        cross1 = (seg2.q - self.p).cross(self.q - self.p)
        cross2 = (seg2.p - self.p).cross(self.q - self.p)
        cross3 = (self.q - seg2.p).cross(seg2.q - seg2.p)
        cross4 = (self.p - seg2.p).cross(seg2.q - seg2.p)

        if (cross1 * cross2 < 0) and (cross3 * cross4 < 0):
            return True  

        if abs(cross1) < EPS and on_segment(self.p, self.q, seg2.q):
            return True
        if abs(cross2) < EPS and on_segment(self.p, self.q, seg2.p):
            return True
        if abs(cross3) < EPS and on_segment(seg2.p, seg2.q, self.q):
            return True
        if abs(cross4) < EPS and on_segment(seg2.p, seg2.q, self.p):
            return True

        # Check for strict endpoint touching (only count if include_p/include_q is enabled)
        if include_p and (abs(cross1) < EPS or abs(cross2) < EPS):
            return True
        if include_q and (abs(cross3) < EPS or abs(cross4) < EPS):
            return True

        return False





@dataclass
class polygon:
    vertices: List[point]

    def shifted_vertices(self, shift=1):
        # v2, v3, ...., vN, v1
        yield from islice(cycle(self.vertices), shift, len(self.vertices) + shift)
    
    @property
    def segments(self):
        for v1, v2 in zip(self.vertices, self.shifted_vertices()):
            yield segment(v1, v2)

    @property
    def perimeter(self):
        return sum((v1 - v2).norm() for v1, v2 in zip(self.vertices, self.shifted_vertices()))
    
    @property
    def area(self):
        return 0.5*sum(p2.y*p1.x - p2.x*p1.y for p1, p2 in zip(self.vertices, self.shifted_vertices()))
    
    @property
    def is_convex(self): #checks if a point is convex (inwards)
        clockwise = iter((p2 - p1).cross(p3 - p2) > 0
                        for p1, p2, p3 in zip(self.vertices,
                                            self.shifted_vertices(1),
                                            self.shifted_vertices(2)))
        first = next(clockwise)
        return all(first == x for x in clockwise)
    
    def is_inside(self, q):   #verifies if a point is into a polygon based on the fact that if the intersection count is even it is inside. you can also use the angles, if the sum is 360 its inside
        p = min(self.vertices, key=lambda v: v.x) - point(1, 0)
        crosses = sum(1 if segment(p, q).does_intersect(s, include_p=True) else 0 for s in self.segments)
        return crosses % 2 == 1
    
    def polygon_split(self, s):   #cuts the polygon with a line s and returns the 2 resulting polygons
        vertices1 = []
        vertices2 = []
        ds = s.p - s.q
        l = line.from_points(s.p, s.q)
        
        u = self.vertices[-1]
        side = ds.cross(u - s.q)
        for v in self.vertices:
            cross_prod = ds.cross(v - s.q)
            if cross_prod*side < 0: 
                p = line.from_points(u, v).intersect(l)
                vertices1.append(p)
                vertices2.append(p)
            if cross_prod <= 0:
                vertices1.append(v)
            if cross_prod >= 0:
                vertices2.append(v)
            side = cross_prod
            u = v
        return polygon(vertices1), polygon(vertices2)
    




def hull(points):  #given a set of random points, it returns a convex polygon that encapsulates all of the points
    if len(points) < 3:
        return polygon(points)
    q = min(points, key=lambda v: v.x)
    p = point(q.x, q.y - 1)
    ch = [p, q]
    while True:
        p, q = ch[-2], ch[-1]
        u = max((v for v in points if v != p and v != q),
        key=lambda x: q.angle(p, x))
        if u in ch:
            break
        ch.append(u)
    return polygon(ch[1:])



# -------------------------------------------------------------------------------------------------------------



def circumcircle(p1: point, p2: point, p3: point):
    # Midpoints of two segments
    mid1 = point((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)
    mid2 = point((p2.x + p3.x) / 2, (p2.y + p3.y) / 2)

    # Perpendicular bisectors
    l1 = line.from_points(mid1, point(mid1.x + (p2.y - p1.y), mid1.y - (p2.x - p1.x)))
    l2 = line.from_points(mid2, point(mid2.x + (p3.y - p2.y), mid2.y - (p3.x - p2.x)))

    # Intersection = circumcenter
    center = l1.intersect(l2)
    print(f"center={center}")
    h, k = center.x, center.y

    # Radius squared
    r2 = (p1 - center).dot(p1 - center)
    r = (p1 - center).norm() 
    print(f"rad={r}")

    # General form: x^2 + y^2 + Cx + Dy + E = 0
    C = -2 * h
    D = -2 * k
    E = h**2 + k**2 - r2

    # Print results
    print(f"(x - {h:+.3f})^2 + (y - {k:+.3f})^2 = {math.sqrt(r2):.3f}^2")
    print(f"x^2 + y^2 {C:+.3f}x {D:+.3f}y {E:+.3f} = 0")



stdin = io.StringIO("""7.0 -5.0 -1.0 1.0 0.0 -6.0
1.0 7.0 8.0 6.0 7.0 -2.0
""")

lin = [float(i) for i in stdin.readline().split()]
while len(lin)>0:
    print(lin)
    p1=point(lin[0],lin[1])
    p2=point(lin[2],lin[3])
    p3=point(lin[4],lin[5])
    circumcircle(p1,p2,p3)
    lin = [float(i) for i in stdin.readline().split()]








