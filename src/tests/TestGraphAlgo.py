import unittest
from src.classes.DiGraph import DiGraph
from src.classes.DiGraphAlgo import DiGraphAlgo


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

    def test_loadsaved_from_json(self):

        ##################### A0 ######################

        AlgoA0 = create_graph()
        A0 = AlgoA0.get_graph()
        AlgoA0.__init__(A0)
        loadedA0 = AlgoA0.load_from_json("../../data/A0.json")
        savedA0 = AlgoA0.save_to_json("A0Nodes.json")
        new_AlgoA0 = AlgoA0.get_graph()

        self.assertTrue(loadedA0)
        self.assertTrue(savedA0)
        self.assertEqual(AlgoA0.get_graph(), new_AlgoA0)

        # # ##################### A1 ######################

        AlgoA1 = create_graph()
        A1 = AlgoA1.get_graph()
        AlgoA1.__init__(A1)
        loadedA1 = AlgoA1.load_from_json("../../data/A1.json")
        savedA1 = AlgoA1.save_to_json("A1Nodes.json")
        new_AlgoA1 = AlgoA1.get_graph()

        self.assertTrue(loadedA1)
        self.assertTrue(savedA1)
        self.assertEqual(AlgoA1.get_graph(), new_AlgoA1)

        # # ##################### A2 ######################

        AlgoA2 = create_graph()
        A2 = AlgoA2.get_graph()
        AlgoA2.__init__(A2)
        loadedA2 = AlgoA2.load_from_json("../../data/A2.json")
        savedA2 = AlgoA2.save_to_json("A2Nodes.json")
        new_AlgoA2 = AlgoA2.get_graph()

        self.assertTrue(loadedA2)
        self.assertTrue(savedA2)
        self.assertEqual(AlgoA2.get_graph(), new_AlgoA2)

        # # ##################### A3 ######################

        AlgoA3 = create_graph()
        A3 = AlgoA3.get_graph()
        AlgoA3.__init__(A3)
        loadedA3 = AlgoA3.load_from_json("../../data/A3.json")
        savedA3 = AlgoA3.save_to_json("A3Nodes.json")
        new_AlgoA3 = AlgoA3.get_graph()

        self.assertTrue(loadedA3)
        self.assertTrue(savedA3)
        self.assertEqual(AlgoA3.get_graph(), new_AlgoA3)

        # # ##################### A4 ######################

        AlgoA4 = create_graph()
        A4 = AlgoA4.get_graph()
        AlgoA4.__init__(A4)
        loadedA4 = AlgoA4.load_from_json("../../data/A4.json")
        savedA4 = AlgoA4.save_to_json("A4Nodes.json")
        new_AlgoA4 = AlgoA4.get_graph()

        self.assertTrue(loadedA4)
        self.assertTrue(savedA4)
        self.assertEqual(AlgoA4.get_graph(), new_AlgoA4)

        # # ##################### A5 ######################

        AlgoA5 = create_graph()
        A5 = AlgoA5.get_graph()
        AlgoA5.__init__(A5)
        loadedA5 = AlgoA5.load_from_json("../../data/A5.json")
        savedA5 = AlgoA5.save_to_json("A5Nodes.json")
        new_AlgoA5 = AlgoA5.get_graph()

        self.assertTrue(loadedA5)
        self.assertTrue(savedA5)
        self.assertEqual(AlgoA5.get_graph(), new_AlgoA5)

        # ##################### 1000Nodes ######################

        Algo1000Nodes = create_graph()
        A1000Nodes = Algo1000Nodes.get_graph()
        Algo1000Nodes.__init__(A1000Nodes)
        loadedAlgo1000Nodes = Algo1000Nodes.load_from_json("../../data/1000Nodes.json")
        savedAlgo1000Nodes = Algo1000Nodes.save_to_json("1000NODES.json")
        new_Algo1000Nodes = Algo1000Nodes.get_graph()

        self.assertTrue(loadedAlgo1000Nodes)
        self.assertTrue(savedAlgo1000Nodes)
        self.assertEqual(Algo1000Nodes.get_graph(), new_Algo1000Nodes)

        # ##################### 10000Nodes ######################

        Algo10000Nodes = create_graph()
        A10000Nodes = Algo10000Nodes.get_graph()
        Algo10000Nodes.__init__(A10000Nodes)
        loadedAlgo10000Nodes = Algo10000Nodes.load_from_json("../../data/10000Nodes.json")
        savedAlgo10000Nodes = Algo10000Nodes.save_to_json("10000NODES.json")
        new_Algo10000Nodes = Algo10000Nodes.get_graph()

        self.assertTrue(loadedAlgo10000Nodes)
        self.assertTrue(savedAlgo10000Nodes)
        self.assertEqual(Algo10000Nodes.get_graph(), new_Algo10000Nodes)


    def test_shortest_path(self):

        ##################### A0 ######################

        AlgoA0 = DiGraphAlgo()
        AlgoA0.load_from_json("..\\..\\data\\A0.json")
        distA0 = AlgoA0.shortest_path(0, 2)
        compA0 = (3.165136835245062, [0, 1, 2])
        self.assertEqual(distA0, compA0)

        ##################### A1 ######################

        # AlgoA1 = DiGraphAlgo()
        # AlgoA1.load_from_json("..\\..\\data\\A1.json")
        # distA1 = AlgoA1.shortest_path(0, 2)
        # compA1 = (3.033632907652237, [0, 1, 2])
        # self.assertEqual(distA1, compA1)

        # ##################### A2 ######################

        # AlgoA2 = DiGraphAlgo()
        # AlgoA2.load_from_json("..\\..\\data\\A2.json")
        # distA2 = AlgoA2.shortest_path(0, 2)
        # compA2 = (3.033632907652237, [0, 1, 2])
        # self.assertEqual(distA2, compA2)

        # ##################### A3 ######################

        # AlgoA3 = DiGraphAlgo()
        # AlgoA3.load_from_json("..\\..\\data\\A3.json")
        # distA3 = AlgoA3.shortest_path(0, 2)
        # compA3 = (3.033632907652237, [0, 1, 2])
        # self.assertEqual(distA3, compA3)

        # ##################### A4 ######################

        # AlgoA4 = DiGraphAlgo()
        # AlgoA4.load_from_json("..\\..\\data\\A4.json")
        # distA4 = AlgoA4.shortest_path(0, 2)
        # compA4 = (2.095850038785596, [0, 1, 2])
        # self.assertEqual(distA4, compA4)

        # ##################### A5 ######################

        # AlgoA5 = DiGraphAlgo()
        # AlgoA5.load_from_json("..\\..\\data\\A5.json")
        # distA5 = AlgoA5.shortest_path(0, 2)
        # compA5 = (1.419506984729119, [0, 2])
        # self.assertEqual(distA5, compA5)


    def test_center_point(self):

        ##################### A0 ######################
        AlgoA0 = DiGraphAlgo()
        AlgoA0.load_from_json("..\\..\\data\\A0.json")
        distA0 = AlgoA0.centerPoint()
        resA0 = (7, 6.806805834715163)
        self.assertEqual(distA0, resA0)

        ##################### A1 ######################

        AlgoA1 = DiGraphAlgo()
        AlgoA1.load_from_json("..\\..\\data\\A1.json")
        distA1 = AlgoA1.centerPoint()
        resA1 = (8, 9.925289024973141)
        self.assertEqual(distA1, resA1)

        # ##################### A2 ######################

        AlgoA2 = DiGraphAlgo()
        AlgoA2.load_from_json("..\\..\\data\\A2.json")
        distA2 = AlgoA2.centerPoint()
        resA2 = (0, 7.819910602212574)
        self.assertEqual(distA2, resA2)

        # ##################### A3 ######################

        AlgoA3 = DiGraphAlgo()
        AlgoA3.load_from_json("..\\..\\data\\A3.json")
        distA3 = AlgoA3.centerPoint()
        resA3 = (2, 8.182236568942237)
        self.assertEqual(distA3, resA3)

        # ##################### A4 ######################

        AlgoA4 = DiGraphAlgo()
        AlgoA4.load_from_json("..\\..\\data\\A4.json")
        distA4 = AlgoA4.centerPoint()
        resA4 = (6, 8.071366078651435)
        self.assertEqual(distA4, resA4)

        # ##################### A5 ######################

        AlgoA5 = DiGraphAlgo()
        AlgoA5.load_from_json("..\\..\\data\\A5.json")
        distA5 = AlgoA5.centerPoint()
        resA5 = (40, 9.291743173960954)
        self.assertEqual(distA5, resA5)

    def test_connected(self):
        Algo = DiGraphAlgo()
        Algo.load_from_json("..\\..\\data\\A0.json")
        self.assertTrue(Algo.connected())
        Algo.get_graph().remove_node(7)
        Algo.get_graph().remove_node(10)
        self.assertFalse(Algo.connected())

    def test_BFS(self):
        Algo = DiGraphAlgo()
        Algo.load_from_json("..\\..\\data\\A0.json")
        Algo.BFS(0)
        Algo.get_graph().remove_node(7)
        Algo.get_graph().remove_node(10)
        Algo.BFS(0)

    def test_plot_graph(self):
        assert True

    def test_TSP(self):
        Algo = DiGraphAlgo()
        Algo.load_from_json("..\\..\\data\\A0.json")
        dist = Algo.TSP([Algo.get_graph().get_all_v()[0], Algo.get_graph().get_all_v()[2]])
        comp = [Algo.get_graph().get_all_v()[0], Algo.get_graph().get_all_v()[1], Algo.get_graph().get_all_v()[2]]
        self.assertEqual(dist, comp)
