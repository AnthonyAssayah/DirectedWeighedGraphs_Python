import sys
from collections import ChainMap
from queue import PriorityQueue
import json
import heapq
from typing import List

import numpy as np

from src.classes.Geolocation import Geolocation
from src.classes.Gui import Gui
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
                if 'pos' in node:
                    values = np.fromstring(node['pos'], dtype=float, sep=',')
                    loc = Geolocation(values[0], values[1], values[2])
                else:
                    loc = Geolocation(0, 0, 0)

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
        vertices = self.DWG.get_all_v()
        for n in vertices:
            v = vertices[n]
            if v.location is not None:
                data['Nodes'].append({
                    'pos': "" + str(v.location.x) + "," + str(v.location.y) + "," + str(v.location.z) + "",
                    'id': v.key
                })
            else:
                data['Nodes'].append({
                    'id': v.key
                })
            for o in v._out:
                data['Edges'].append({
                    'src': v.key,
                    'dest': o,
                    'w': v.get_out()[o].weight

                })
        try:
            with open(file_name, 'w') as file:
                json.dump(data, file, indent=2, sort_keys=True)
                return True

        except FileNotFoundError or FileExistsError or OSError:
            print("Cannot read the file")
            return False



    def shortest_path(self, src, dest) -> (float, list):
        djk = self.dijkstra(src)[0]
        path = []
        cur = dest
        if cur not in djk:
            return -1, []
        while cur != src:
            path.append(self.DWG.get_all_v()[cur])
            cur = djk[cur]
        path.append(self.DWG.get_all_v()[src])
        path.reverse()
        return self.dijkstra(src)[1].get(dest), path

    def centerPoint(self) -> (int, float):

        max_lengths = dict.fromkeys(self.DWG.get_all_v().keys(), 0)

        for n in self.DWG.get_all_v().values():
            dist = self.dijkstra(n.get_key())[1]
            temp_max = max(dist.values())
            if temp_max > max_lengths[n.get_key()]:
                max_lengths[n.get_key()] = temp_max

        min = sys.float_info.max
        ret_key = 0

        for key in max_lengths.keys():
            if max_lengths[key] < min:
                min = max_lengths[key]
                ret_key = key
        return ret_key, min

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

    def plot_graph(self):
        Gui(self)

    def TSP(self, node_list: List[int]) -> (List[int], float):

        tsp_path = []
        curr_list = node_list

        temp = node_list[0]
        tsp_path.append(self.DWG.get_all_v()[curr_list[0]])
        curr_list.pop()

        while curr_list:

            shortest_path = sys.float_info.max
            node_id = -1
            node_index = -1

            for i in range(len(curr_list)):

                key = curr_list[i]
                if self.shortest_path_dist(temp, key) < shortest_path:

                    shortest_path = self.shortest_path_dist(temp, key)
                    node_id = key
                    node_index = i
            print(str(temp) + " " + str(node_id))
            short_list = self.shortest_path(temp, node_id)[1]
            short_list.remove(0)
            while short_list:
                tsp_path.append(short_list.get(0))
                short_list.remove(0)
            node = curr_list.get(node_index)
            temp = self.DWG.get_all_v()[node]
            curr_list.remove(curr_list.get(node_index))

        return tsp_path





        # if node_list is None:
        #     return None
        #
        # priority = []  # contains nodes
        # unhandled = []  # contains ints
        #
        # for n in node_list:
        #     unhandled.append(n)
        #
        # cur = node_list[0]
        #
        # priority.append(self.DWG.get_all_v()[unhandled[0]])
        #
        # unhandled.remove(unhandled[0])
        #
        # while unhandled:
        #     shortest_dist = sys.float_info.max
        #
        #     id_short = sys.float_info.min
        #     location = sys.float_info.min
        #
        #     for i in range(len(unhandled)):
        #         key = unhandled[i]
        #         temp = self.shortest_path_dist(cur, key)
        #
        #         if temp < shortest_dist:
        #             shortest_dist = temp
        #             id_short = key
        #             location = i
        #
        #     shortest_path = self.shortest_path(cur, id_short)
        #     shortest_path.remove(shortest_path[0])
        #
        #     while shortest_path:
        #         priority.append(shortest_path[0])
        #         shortest_path.remove(shortest_path[0])
        #
        #     node_id = unhandled[location]
        #     cur = self.DWG.get_all_v()[node_id]
        #     unhandled.remove(unhandled[location])
        #
        # if len(priority) == 1:
        #     return None
        # else:
        #     return priority

    def shortest_path_dist(self, src, dest):

        if not self.connected():
            return -1

        dist = self.dijkstra(src)[1].get(dest)
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
    def dijkstra(self, start_node):
        unvisited_nodes = list(self.DWG.get_all_v().keys())

        shortest_path = {}

        previous_nodes = {}

        max_value = sys.maxsize
        for node in unvisited_nodes:
            shortest_path[node] = max_value
        shortest_path[start_node] = 0

        while unvisited_nodes:
            current_min_node = None
            for node in unvisited_nodes:
                if current_min_node == None:
                    current_min_node = node
                elif shortest_path[node] < shortest_path[current_min_node]:
                    current_min_node = node

            neighbors = self.DWG.get_all_v()[current_min_node].get_out()
            for neighbor in neighbors:
                tentative_value = shortest_path[current_min_node] + self.DWG.get_all_v()[current_min_node].get_out()[neighbor].get_weight()
                if tentative_value < shortest_path[neighbor]:
                    shortest_path[neighbor] = tentative_value
                    previous_nodes[neighbor] = current_min_node

            unvisited_nodes.remove(current_min_node)

        return previous_nodes, shortest_path

    def __str__(self):
        return self.DWG.get_all_v().keys()