import math


class Geolocation:

    # Initialize a new 3D location(x,y,z)
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    # Return the distances between two points
    def distance(self, loc) -> float:
        return math.sqrt(math.pow(self.x - loc.x(), 2) + math.pow(self.y - loc.y(), 2) + math.pow(self.z - loc.z(), 2))

    # Return x coordinate
    def x(self) -> float:
        return self.x

    # Return y coordinate
    def y(self) -> float:
        return self.y

    # Return z coordinate
    def z(self) -> float:
        return self.z
