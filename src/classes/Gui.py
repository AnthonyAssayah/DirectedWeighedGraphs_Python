import math

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import ArrowStyle


class Gui:
    def __init__(self, DGA):
        self.DGA = DGA
        self.screen_size = 100
        self.draw()

    def draw(self):
        plt.axis([0, self.screen_size, 0, self.screen_size])
        self.draw_edges()
        self.draw_nodes()
        plt.show()

    def draw_nodes(self):
        for n in self.DGA.get_graph().get_all_v().values():
            loc = n.get_location()
            plt.plot(loc.x, loc.y, 'ro')
            plt.text(loc.x, loc.y, str(n.get_key()))

    def draw_edges(self):
        ArrowStyle.Fancy(head_length=.4, head_width=.4, tail_width=.4)
        for n in self.DGA.get_graph().get_all_v().values():
            for e in n.get_out().values():
                loc1 = n.get_location()
                loc2 = self.DGA.get_graph().get_all_v()[e.get_destination()].get_location()

                plt.arrow(x=loc1.x, y=loc1.y, dx=(loc2.x - loc1.x) * 0.9, dy=(loc2.y - loc1.y) * 0.9, width=.00007, facecolor='blue', edgecolor='none')