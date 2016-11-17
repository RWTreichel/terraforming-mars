"""
Testing area for hex math
http://www.redblobgames.com/grids/hexagons/
"""

import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

"""
Assumptions
    - Pointy Topped
    -
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Hex:
    def __init__(self, center, size):
        self.center = center
        self.size = size
        self.corners = np.array([(self.hex_corner(i).x, self.hex_corner(i).y) for i in range(6)])
        self.hex_patch = Polygon(self.corners, closed=True)

    def hex_corner(self, i):
        angle_deg = 60 * i + 30
        angle_rad = math.pi / 180 * angle_deg
        return Point(self.center.x + self.size * math.cos(angle_rad),
                     self.center.y + self.size * math.sin(angle_rad))


if __name__ == '__main__':
    my_hex = Hex(center=Point(0, 0), size=5)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.add_patch(my_hex.hex_patch)

    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_aspect(1)

    plt.show()
