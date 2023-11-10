class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def midpoint(self, other):
        mx = (self.x + other.x) / 2
        my = (self.y + other.y) / 2
        return Point(mx, my)

    def slope_to(self, other):
        if self.x == other.x:
           
            return float('inf')
        return (other.y - self.y) / (other.x - self.x)

    def area_of_triangle(self, p2, p3):
        
        return 0.5 * abs((self.x * (p2.y - p3.y) + p2.x * (p3.y - self.y) + p3.x * (self.y - p2.y)))

    def perimeter_of_triangle(self, p2, p3):
        
        side1 = self.distance_to(p2)
        side2 = p2.distance_to(p3)
        side3 = p3.distance_to(self)
        return side1 + side2 + side3

    def area_of_circle(self, radius):
        # Area of a circle
        return math.pi * radius**2

    def circumference_of_circle(self, radius):
        # Circumference of a circle
        return 2 * math.pi * radius

    @staticmethod
    def intersection_point(line1_start, line1_end, line2_start, line2_end):
        # Calculate the intersection point of two lines
        x1, y1 = line1_start.x, line1_start.y
        x2, y2 = line1_end.x, line1_end.y
        x3, y3 = line2_start.x, line2_start.y
        x4, y4 = line2_end.x, line2_end.y

        denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

        if denominator == 0:
            return None  # Lines are parallel or coincident

        intersection_x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denominator
        intersection_y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denominator

        return Point(intersection_x, intersection_y)

    def gradient_of_line(self, other):
        
        if self.x == other.x:
            
            return None
        return (other.y - self.y) / (other.x - self.x)

    def gradient_of_distance(self, other):
        
        delta_x = other.x - self.x
        delta_y = other.y - self.y
        distance = self.distance_to(other)
        gradient_x = -(delta_x / distance)
        return gradient_x

  
