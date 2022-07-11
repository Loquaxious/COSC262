class Vec:
    """A simple vector in 2D. Also used as a position vector for points"""
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

    def __str__(self):
        return "({}, {})".format(self.x, self.y)
        
        
def signed_area(a, b, c):
    """Twice the area of the triangle abc.
       Positive if abc are in counter clockwise order.
       Zero if a, b, c are colinear.
       Otherwise negative.
    """
    p = b - a
    q = c - a
    return p.x * q.y - q.x * p.y


def is_on_segment(p, a, b):
    """Returns true if and only if the point p lies somewhere on the line segment from a to b"""
    if signed_area(p, a, b) == 0:
        if (p - a).lensq() <= (a - b).lensq() and (p - b).lensq() <= (a - b).lensq():
            return True
        else:
            return False
    else:
        return False
    
    
def is_ccw(a, b, c):
    """True iff triangle abc is counter-clockwise."""
    p = b - a
    q = c - a
    area = p.x * q.y - q.x * p.y
    
    if area == 0:
        raise ValueError("area = 0") 
    return area > 0    
    
    
def classify_points(line_start, line_end, points):
    """
    Takes an infinite line defined by start and end and a list of points and 
    returns a two tuple of integers:
    Where the first element is the number of points from points that are to the 
    RHS of the line and second element is all the integers on the LHS of the line
    """
    l_count = 0
    r_count = 0
    for p in points:
        if is_ccw(line_start, line_end, p):
            l_count += 1
        else:
            r_count += 1
    return (r_count, l_count)
    
points = [
    Vec(1, 99),
    Vec(0, 100),
    Vec(50, 0),
    Vec(50, 1),
    Vec(50, 99),
    Vec(50, 50),
    Vec(100, 100),
   Vec(99, 99)]

print(classify_points(Vec(0, 49), Vec(100, 49), points))    