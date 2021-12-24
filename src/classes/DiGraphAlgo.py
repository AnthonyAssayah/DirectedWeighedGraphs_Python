import sys
from collections import ChainMap
from queue import PriorityQueue
import json
import heapq

import numpy as np

from src.classes.Geolocation import Geolocation
from src.classes.Gui import Gui
from src.classes.Node import Node
from src.interfaces.GraphAlgoInterface import GraphAlgoInterface
from src.interfaces.GraphInterface import GraphInterface
from src.classes.DiGraph import DiGraph


class DiGraphAlgo(GraphAlgoInterface):

    def __init__(self, DWG: DiGraph = None):

        self.djkhelper = {}

        if DWG is None:
            self.DWG = DiGraph()
        else:
            self.DWG = DWG

    def get_graph(self) -> GraphInterface:
        return self.DWG

    def load_from_json(self, file_name: str) -> bool:

        try:
            loaded_graph = DiGraph()
            with open(file_name) as json_file:
                data = json.load(json_file)

            for node in data['Nodes']:
                values = np.fromstring(node['pos'], dtype=float, sep=',')
                loc = Geolocation(values[0], values[1], values[2])

                loaded_graph.add_node(node['id'], loc)

            for edge in data['Edges']:
                loaded_graph.add_edge(edge['src'], edge['dest'], edge['w'])
            self.DWG = loaded_graph
            return True

        except FileNotFoundError or FileExistsError or OSError:
            print("Cannot read the file")
            return False

    def save_to_json(self, file_name: str) -> bool:

        data = {'Edges': [], 'Nodes': []}
        vertice = self.DWG.get_all_v()
        for edge in vertice:
            v = vertice[edge]
            if v.location:
                data['Nodes'].append({
                    'id': v.key,
                    'pos': v.location
                })
            else:
                data['Nodes'].append({
                    'id': v.key
                })
            for index in v._out:
                data['Edges'].append({
                    'src': vertice.get_key(),
                    'dest': index,
                    'w': vertice.get_out[index].weight,
                })
        try:
            with open('HII', 'w') as file:
                json.dump(data, file, indent=4, sort_keys=True)

        except FileNotFoundError or FileExistsError or OSError:
            print("Cannot read the file")
            return False

    def shortest_path(self, src, dest) -> (float, list):
        self.dijkstra(self.DWG.get_all_v()[src])
        path = []
        cur = dest
        while cur != src and self.djkhelper[cur] != None:
            path.append(self.DWG.get_all_v()[cur])
            cur = self.djkhelper[cur]
        path.append(self.DWG.get_all_v()[src])
        path.reverse()
        return path

    def center(self) -> Node:

        maxv = {}

        for n in self.DWG.get_all_v().values():
            distance = self.dijkstra(n)
            maxd = sys.float_info.min

            for key in distance.keys():
                d = distance[key]
                if d < maxd:
                    maxd = d

            maxv[n.get_key()] = maxd
        minv = sys.float_info.max
        min_key = 0
        for key in maxv.keys():
            if minv > maxv[key]:
                minv = maxv[key]
                min_key = key

        return self.DWG.get_all_v()[min_key]

    def connected(self):

        if self.DWG.v_size() == 0 or 1:
            return True

        for n in self.DWG.get_all_v():
            n.set_tag(-1)

        flag = True
        my_q = []
        finish = []

        if n in self.DWG.get_all_v().values():
            cur = n
        else:
            return False

        second = False
        k = 0

        while flag:
            while flag:
                flag = False
                if self.DWG.get_out(cur.get_key()) == None:
                    return False

                cur_edges = dict(ChainMap(cur.get_in(), cur.get_out()))

                if cur_edges:
                    return False

                for e in cur_edges:
                    if self.DWG.get_all_v()[e.get_destination].get_tag() != k:
                        self.DWG.get_all_v()[e.get_destination].set_tag(k)
                        my_q.append(self.DWG.get_all_v()[e.get_destination])
                    elif not second:
                        finish.append(cur)

                if not my_q:
                    cur = my_q.pop()
                    flag = True

            if not finish:
                cur = finish.pop()
                second = True
                flag = True

            for n in self.DWG.get_all_v().values():
                if n.get_tag() != k:
                    return False
            k += 1

        return True

        # if len(self.DWG.get_all_v()) == 0 or 1:
        #     return True
        #
        # flipped_edges = DiGraph()
        #
        # for n in self.DWG.get_all_v().values():
        #     flipped_edges.add_node(n.get_key(), n.get_location())
        #
        # for n in self.DWG.get_all_v().values():
        #     for e in n.get_out().values():
        #         flipped_edges.add_edge(e.get_source(), e.get_destination(), e.get_weight())
        #
        # # checks if the bfs had been to all the nodes by comparing the size of the list returned from the bfs with the size of the nodes dict from DWG
        # this_graph_bfs = self.BFS(self.DWG.get_all_v()[self.DWG.get_all_v().keys[0]]) == len(self.DWG.get_all_v())
        # temp = self.DWG
        # self.DWG = flipped_edges
        # this_graph_transpose_bfs = self.BFS(self.DWG.get_all_v()[self.DWG.get_all_v().keys[0]]) == len(self.DWG.get_all_v())
        # self.DWG = temp
        #
        # return this_graph_bfs and this_graph_transpose_bfs

    def plot_graph(self):
        Gui(self)

    def TSP(self, node_list):
        if node_list is None:
            return None

        priority = []  # contains nodes
        unhandled = []  # contains ints

        for n in node_list:
            unhandled.append(n.get_key())

        cur = node_list[0]

        priority.append(self.DWG.get_all_v()[unhandled[0]])

        unhandled.remove(0)

        while unhandled:
            shortest_dist = sys.float_info.max

            id_short = sys.float_info.min
            location = sys.float_info.min

            for i in range(len(unhandled)):
                key = unhandled[i]
                temp = self.shortest_path_dist(cur.get_key(), key)

                if temp < shortest_dist:
                    shortest_dist = temp
                    id_short = key
                    location = i

            shortest_path = self.shortest_path(cur.get_key(), id_short)
            shortest_path.remove(shortest_path[0])

            while shortest_path:
                priority.append(shortest_path[0])
                shortest_path.remove(shortest_path[0])

            node_id = unhandled[location]
            cur = self.DWG.get_all_v()[node_id]
            unhandled.remove(unhandled[location])

        if len(priority) == 1:
            return None
        else:
            return priority
#    def BFS(self, node) -> {}:  # Returns array of nodes

        # for n in self.DWG.get_all_v().values():
        #     n.set_tag(0)
        #
        # q = []
        #
        # node.set_tag(1)
        #
        # counter = 1
        # q.append(node)
        # while q:
        #     cur = q.pop()
        #     for n in self.DWG.get_all_v().values():
        #         for e in n.get_out().values():
        #             dest = self.DWG.get_all_v()[e.get_destination()]
        #             if dest.get_tag == 0:
        #                 dest.set_tag(1)
        #                 q.append(dest)
        #                 counter += 1
        #
        # return counter  # == self.DWG.v_size()

    def shortest_path_dist(self, src, dest):

        if not self.connected():
            return -1

        dist = self.dijkstra(self.DWG.get_all_v()[src]).get(dest)
        return dist

    def connected(self):

        DGA_trans = DiGraphAlgo(self.getTranspose())
        DGA_BFS = self.BFS(list(self.DWG.get_all_v().values())[0].get_key())
        DGA_trans_BFS = DGA_trans.BFS(list(self.DWG.get_all_v().values())[0].get_key())
        return DGA_BFS == DGA_trans_BFS == self.DWG.v_size()

    def getTranspose(self):
        g = DiGraph()

        for n in self.DWG.get_all_v().values():
            g.add_node(n.get_key(), n.get_location())

        for n in self.DWG.get_all_v().values():
            for e in n.get_out().values():
                g.add_edge(e.get_destination(), e.get_source(), e.get_weight())

        return g

    def BFS(self, src):

        for n in self.DWG.get_all_v().values():
            n.set_info("white")

        q = []

        self.DWG.get_all_v()[src].set_info("gray")
        q.append(self.DWG.get_all_v()[src])

        counter = 1

        while q:
            cur = self.DWG.get_all_v()[q.pop().get_key()]
            if cur.get_info() == "gray":
                cur.set_info("black")
                for e in cur.get_out().values():
                    if self.DWG.get_all_v()[e.get_destination()].get_info() == "white":
                        q.append(self.DWG.get_all_v()[e.get_destination()])
                        self.DWG.get_all_v()[e.get_destination()].set_info("gray")
                        counter += 1
        return counter


    # Input(graph,int),Output(hashmap:int-double)
    # Uses priority queue to oreder nodes by their wights
    def dijkstra(self, src) -> dict:  # hashmap from int -> float
        # hashmap:int-double
        distance = {}
        for n in self.DWG.get_all_v().values():
            distance[n.get_key()] = sys.float_info.max
        pq = PriorityQueue(len(distance))
        pq.put(Node(Geolocation(), 0), src.get_key())
        distance[src.get_key()] = 0.0
        self.djkhelper[src.get_key()] = -1
        settled = set()
        while len(settled) != len(self.DWG.get_all_v()):
            if pq.empty():
                return distance
            u = pq.get().get_key()
            if u in settled:
                continue
            settled.add(u)

            for e in self.DWG.all_out_edges_of_node(u).values():
                dest = self.DWG.get_all_v()[e.get_destination()]
                if dest.get_key() not in settled:

                    edge_distance = e.get_weight()
                    new_distance = distance[u] + edge_distance

                    if new_distance < distance[dest.get_key()]:
                        distance[dest.get_key()] = new_distance
                        self.djkhelper[dest.get_key()] = u
                    n2 = Node(Geolocation(), dest.get_key())
                    n2.set_tag(distance[dest.get_key()])
                    pq.put(n2)

        return distance
