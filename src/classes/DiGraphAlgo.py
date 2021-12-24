import sys
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

    # def TSP(self, node_lst: List[int]) -> (List[int], float):
    #
    #     tsp_path = []
    #     curr_list = []
    #
    #     for i in range(node_lst.__len__()):
    #         curr_list.append(node_lst.index(i))
    #
    #     tmp = Node(node_lst.index(0))
    #     tsp_path.append(self.DWG.nodes(curr_list.index(0)))
    #     curr_list.remove(0)
    #
    #     while curr_list:
    #
    #         shortest = float("inf")
    #         node_id = -1
    #         index = -1
    #
    #         for i in range(curr_list):
    #             key = curr_list.index(i)
    #             if shortestPathDist(tmp.get_key() < shortest):
    #                 shortest = shortestPathDist(tmp.get_key(), key)
    #                 node_id = key
    #                 index = i
    #
    #         short_list = []
    #         short_list = shortest_path(tmp.get_key(), node_id)
    #         short_list

    #         List<NodeData> short_list = shortestPath(tmp.getKey(), node_id);
    #         short_list.remove(0);
    #
    #         while ( !short_list.isEmpty()) {
    #             tsp_path.add(short_list.get(0));
    #             short_list.remove(0);
    #         }
    #         int node = curr_list.get(index);
    #         tmp = this.DWG.getNode(node);
    #         curr_list.remove(curr_list.get(index));
    #     }
    #
    #     return tsp_path;
    # }
    def BFS(self, s) -> {}:  # Returns array of nodes

        # Mark not visited
        visited = [False] * (max(self.DWG) + 1)

        # Create a queue
        queue = []

        # Create an array
        array = []

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue a vertex from queue and save to array
            s = queue.pop(0)
            array.append(s)

            # Get all neighbors vertices of the dequeued vertex s
            # If a neighbor has not been visited, then mark it visited and enqueue it
            for n in self.DWG.get_all_v():
                if visited[n] == False:
                    queue.append(n)
                    visited[n] = True

        return array

    def shortest_path_dist(self, src, dest):
        # check if graph is connected first!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        dist = self.dijkstra(self.DWG.get_all_v()[src]).get(dest)
        return dist

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
