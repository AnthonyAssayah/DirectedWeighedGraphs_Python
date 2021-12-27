import unittest
from src.classes.Node import Node
from src.classes.Edge import Edge
from src.classes.Geolocation import Geolocation


def create_Edge() -> Edge:
    g1 = Geolocation(7, -1, 3.5);
    g2 = Geolocation(8, 3, 5.5);
    node1 = Node(g1, 4);
    node2 = Node(g2, 7);
    edge = (node1, node2, 9.5)
    return edge


class TestNode(unittest.TestCase):

    def test_get_source(self):
        edge = create_Edge()
        src = 4
        self.assertEqual((edge[0]), src)
