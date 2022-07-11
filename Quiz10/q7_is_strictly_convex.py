class Vec:
    """A simple vector in 2D. Also use for points (position vector)"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)
        
    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scale):
        """Multiplication by a scalar"""
        return Vec(self.x * scale, self.y * scale)
        
    def dot(self, other):
        return self.x * other.x + self.y * other.y
        
    def lensq(self):
        return self.dot(self)
        
        
def is_ccw(a, b, c):
    """True iff triangle abc is counter-clockwise"""
    p = b - a
    q = c - a
    area = p.x * q.y - q.x * p.y
    # May want to throw an exception if area == 0
    return area > 0 

def is_strictly_convex(vertices):
    """Takes a list of three or more points and returns True 
    if and only if the vertices, taken in order, define a strictly-convex 
    counter-clockwise polygon"""
    result = None
    n = len(vertices)
    for i in range(n-2):
        if is_ccw(vertices[i], vertices[i+1], vertices[i+2]):
            result = True
        else:
            return False
    if is_ccw(vertices[n-2], vertices[n-1], vertices[0]):
        result = True
    else:
        return False

    if is_ccw(vertices[n-1], vertices[0], vertices[1]):
        return result
    else:
        return False


verts = [
    (0, 0),
    (100, 0),
    (100, 100),
    (0, 100)]
points = [Vec(v[0], v[1]) for v in verts]
print(is_strictly_convex(points))
#True

verts = [
    (0, 0),
    (0, 100),
    (100, 100),
    (100, 0)]
points = [Vec(v[0], v[1]) for v in verts]
print(is_strictly_convex(points))
#False

verts = [
    (60, 60),
    (100, 0),
    (100, 100),
    (0, 100)]
points = [Vec(v[0], v[1]) for v in verts]
print(is_strictly_convex(points))
#False

verts = [
    (0, 0),
    (100, 0),
    (50, 50),
    (0, 100)]
points = [Vec(v[0], v[1]) for v in verts]
print(is_strictly_convex(points))
#False

verts = [
    (0, 0),
    (100, 0),
    (0, 100),
    (1, 50)]
points = [Vec(v[0], v[1]) for v in verts]
print(is_strictly_convex(points))
#false