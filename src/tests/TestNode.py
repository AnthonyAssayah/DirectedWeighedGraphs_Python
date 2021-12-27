import unittest
from src.classes.Node import Node
from src.classes.Geolocation import Geolocation


def create_Node() -> Node:
    g1 = Geolocation(7, -1, 3.5);
    node1 = Node(g1, 4);
    return node1


class TestNode(unittest.TestCase):

    def test_get_Location(self):
        node = create_Node()
        g = Geolocation(7, -1, 3.5);
        g1 = node.location
        self.assertEqual(g.__repr__(), g1.__repr__())

    def test_set_Location(self):
        node = create_Node()
        g = Geolocation(1, 1, 1)
        node.set_location(g)
        g_new = node.location
        self.assertEqual(g, g_new)

    def test_get_key(self):
        node = create_Node()
        key = 4
        self.assertEqual(node.key, key)

    def test_set_key(self):
        node = create_Node()
        key = 5
        node.set_key(key)
        key_new = node.key
        self.assertEqual(key, key_new)

    def test_get_info(self):
        node = create_Node()
        info = "white"
        self.assertNotEqual(node.info, info)

    def test_set_info(self):
        node = create_Node()
        info = "black"
        node.set_info(info)
        info_new = node.info
        self.assertEqual(info, info_new)

    def test_get_tag(self):
        node = create_Node()
        tag = 1
        self.assertNotEqual(node.tag, tag)

    def test_set_tag(self):
        node = create_Node()
        tag = 1
        node.set_tag(tag)
        tag_new = node.tag
        self.assertEqual(tag, tag_new)
