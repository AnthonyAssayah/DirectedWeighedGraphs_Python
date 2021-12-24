from typing import List
import json
import heapq
from src.classes.Geolocation import Geolocation
from src.classes.Node import Node
from src.interfaces.GraphAlgoInterface import GraphAlgoInterface
from src.interfaces.GraphInterface import GraphInterface
from src.classes.DiGraph import DiGraph


class DiGraphAlgo(GraphAlgoInterface):

    def __init__(self, DWG: DiGraph = None):

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
                loaded_graph.add_node(node['id'],Geolocation(','.split(node['pos'])))

            for edge in data['Edges']:
                loaded_graph.add_edge(edge['src'], edge['dest'], edge['w'])
            self.DWG = loaded_graph
            return True

        except FileNotFoundError or FileExistsError or OSError:
            print("Cannot read the file")
            return False

    def save_to_json(self, file_name: str) -> bool:


        # nodes = self.D.get_all_v()
        #
        # data = {'Edges': [], 'Nodes': []}
        #
        # for n in nodes:
        #     node = nodes[n]
        #     if node.pos:
        #         data['Nodes'].append({
        #             'id': node.key,
        #             'pos': node.pos
        #         })
        #     else:
        #         data['Nodes'].append({
        #             'id': node.key
        #         })
        #
             # for o in node.out_edges:
        #         data['Edges'].append({
        #             'src': node.key,
        #             'dest': o,
        #             'w': node.out_edges[o].weight
        #         })

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
                json.dump(data, file)

        except FileNotFoundError or FileExistsError or OSError:
            print("Cannot read the file")
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):

        n1 = self.DWG.nodes.get(id1)
        n2 = self.DWG.nodes.get(id2)

        if n1 is None or n2 is None:
            raise Exception("n1 or n2 doesn't exist in the graph")

        if id1 == id2:
            return 0, [id1]

        allNodes = self.DWG.get_all_v()

        dist = {node: float("inf") for node in allNodes}
        parent = {id1: -1}
        dist[id1] = 0
        prior_q = [(dist[id1], id1)]

        while prior_q:
            curr = heapq.heappop(prior_q)
            if dist[curr] == "inf":
                break
            for adj, edge in self.DWG.all_out_edges_of_node(curr):    # curr.get_key()
                shortest = dist[curr] + edge.get_weight()
                if dist[adj] > shortest:
                    dist[adj] = shortest
                    parent[adj] = curr
                    heapq.heappush(prior_q, (dist[adj], adj))
                    # if curr == id2:
                    #     break

        path, tmp = [], n2
        if dist[id2] == "inf":
            return "inf", []
        while tmp != -1 and tmp != id1:
            path.insert(0, tmp)
            tmp = parent[tmp]

        return dist[id2], path

    def TSP(self, node_lst: List[int]) -> (List[int], float):

        tsp_path = []
        curr_list = []

        for i in range(node_lst.__len__()):
            curr_list.append(node_lst.index(i))

        tmp = Node(node_lst.index(0))
        tsp_path.append(self.DWG.nodes(curr_list.index(0)))
        curr_list.remove(0)

        while curr_list:

            shortest = float("inf")
            node_id = -1
            index = -1

            for i in range(curr_list):
                key = curr_list.index(i)
                if shortestPathDist(tmp.get_key() < shortest):
                    shortest = shortestPathDist(tmp.get_key(), key)
                    node_id = key
                    index = i

            short_list = []
            short_list = shortest_path(tmp.get_key(), node_id)
            short_list


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
    def BFS(self, s):

        # Mark all the vertices as not visited
        visited = [False] * (max(self.DWG) + 1)

        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print(s, end=" ")

            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.DWG[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


    def centerPoint(self) -> (int, float):
        pass

    def plot_graph(self) -> None:
        pass
