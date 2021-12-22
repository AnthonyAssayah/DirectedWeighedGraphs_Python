import unittest
from unittest import TestCase
from src.classes.DiGraph import DiGraph
from src.classes.DiGraphAlgo import DiGraphAlgo
from src.classes.Node import Node
from src.classes.Geolocation import Geolocation


def create_graph() -> DiGraphAlgo:
    DWG = DiGraph()

    for i in range(9):
        DWG.add_node(i)

    DWG.add_edge(0, 1, 1)  # 1
    DWG.add_edge(0, 2, 3)  # 2
    DWG.add_edge(3, 0, 5)  # 3
    DWG.add_edge(3, 1, 2)  # 4
    DWG.add_edge(1, 3, 6)  # 5
    DWG.add_edge(3, 4, 1)  # 6
    DWG.add_edge(1, 4, 2)  # 7
    DWG.add_edge(5, 1, 4)  # 8
    DWG.add_edge(4, 5, 4)  # 9
    DWG.add_edge(4, 2, 9)  # 10
    DWG.add_edge(2, 5, 3)  # 11

    GraphAlgo = DiGraphAlgo(DWG)

    return GraphAlgo


class TestGraphAlgo(unittest.TestCase):

    def test_get_graph(self):
        graph_Algo = create_graph()
        graph = graph_Algo.get_graph()
        self.assertTrue(graph_Algo.get_graph, graph)

    def test_load_from_json(self):
        Algo = create_graph()
        self.assertTrue(Algo.load_from_json("../../data/A0.json"))
        self.assertTrue(Algo.load_from_json("../../data/A1.json"))
        self.assertTrue(Algo.load_from_json("../../data/A2.json"))
        self.assertTrue(Algo.load_from_json("../../data/A3.json"))
        self.assertFalse(Algo.load_from_json("../../data/A6.json"))

    def test_save_to_json(self):
        Algo = create_graph()
        Algo.load_from_json("../../data/A0.json")
        self.assertTrue(Algo.save_to_json("G0.json"))
        Algo.load_from_json("../../data/A1.json")
        self.assertTrue(Algo.save_to_json("G1.json"))
        Algo.load_from_json("../../data/A2.json")
        self.assertTrue(Algo.save_to_json("G2.json"))

    def test_shortest_path(self):
        Algo = create_graph()
        algo = Algo.shortest_path(0, 3)
        shortest = (3, [0, 1, 3])
        self.assertEqual(shortest, algo)

    def test_tsp(self):
        assert False

    def test_center_point(self):
        assert False

    def test_plot_graph(self):
        assert False
