![Minimal_Chart_01](https://user-images.githubusercontent.com/92322613/147286414-a95a193b-e4c0-4d78-8e38-a174583092d5.gif)


# Directed & Weighted Graphs - EX3_OOP

This project is based on a previous assigment of ***Directed and Weighted Graphs*** but for this one we need to implement on *Python*. This exercise is composed of two main parts, the first is to implement the two main interfaces GraphInterface and GraphAlgoInterface in order to create all the elements that form a graph. The second part is the GUI, which will allow us to really visualize the graph and all its parameters and options. 

<br />

## External Sources 🔎

- Explanation about the *Dijkstra Algorithm* on this [Youtube](https://www.youtube.com/watch?v=XB4MIexjvY0&list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O&index=45) video, detailling
 all the process in examples with the drawbacks and analysing the time complexity.
 
 - Inofrmation about the famous problem of [Travelling salesman problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem).This optimization problem which consists in determining, given a list of cities and the distances between all the pairs of cities, the shortest circuit that passes through every town once and only once.

- Tutorial on the [*BFS Algorithm*](https://www.programiz.com/dsa/graph-bfs).This algorithm is used to calculate the distances of all the nodes from a source node in an  graph directed or not directed.

- Website of [Matplotlib](https://matplotlib.org/) to learn about all the components and function to create a GUI in Pyhton.

## Interfaces & Classes 🎯

There are 5 classes defined in this project, the interfaces are in the ```api``` package and their implementations can be found in ```classes``` package. Their properties and 
methods are detailed below.

### <ins>***1 - Node***<ins> 

This class is a simple representation of a vertex on a directed weighted graph and implement a set of different operations.

Each ```Node``` contains five attributes:

  - ```key```: This is the ID associated to each node.
  - ```location```: This is the position of the node in a 3D dimension with 3 coordinates(x,y,z).
  - ```tag```: This is an Integer value used to calculate several algorithms initialized to 0.
  - ```info```: This is a string corresponding to node’s meta data which helps us to calculate various functions initialized to "White".
  - ```_in```: This is a dictionary that contains all the edges incoming to this node.
  
  <br />
  
  | **Functions**      |    **Explanation**        |
|-----------------|-----------------------|
| `_init__(self, location=Geolocation(), key=0)` | Initialize a new Node set 0 as default key |
| `get_key(self) -> int` | Returns the key associated to a specific node |
| `set_key(self, new_key) -> None` | Change the key of the node to new_key |
| `get_Location(self) -> Geolocation` | Returns the location (3D) of this node |
| `set_location(self, new_loc) -> None` | Changes the location of the node as *new_loc*  |
| `get_info(self) -> str` | Returns the meta data associated with this node |
| `set_info(self, new_info) -> None` | Changes the meta data of the node as *new_info* |
| `get_tag(self) -> int` | Returns the tag value of the node |
| `set_tag(self, new_tag) -> None` | Changes the tag value of the node to *new_tag* |
| `get_in(self) -> dict` | Return a dictionary of incoming edges of the node |
| `get_out(self) -> dict`| Return a dictionary of outgoing edges of the node |
| `add_in(self, new_key, weight) -> None` | Add a new node as the destination of a new edge |
| `remove_in(self, node_data: int) -> bool` | Return true iff,succeed to remove the node_data from the _in |
| `remove_out(self, node_data: int) -> bool` | Return true iff,succeed to remove the node_data from the _out |
  
> Test on this class: *TestNode.py*
  
<br />

### <ins>***2 - Edge***<ins>
  
 This class designes all the characteristics and operations applicable on a directional edge defined by its source and destination in a directional weighted graph.

  An ```Edge``` is discribed by five fields:
  
  - ```src```: This integer represents the source node of the edge.
  - ```dest```: This integer represents the destination node of the edge.
  - ```weight```: This is a double variable used as edge's weight, must be positive. 
  
<br />
  
  | **Functions**      |    **Explanation**        |
|-----------------|-----------------------|
| `__init__(self, source=0, destination=0, weight=0.0)` | Initialize a new Edge set its parameters to 0 as default value |
| `get_source(self) -> int` | Returns the id of the source node of this edge |
| `set_source(self, new_source) -> None` | Change the source of the edge as *new_source* |
| `get_destination(self) -> int` | Return the destination of the edge |
| `set_destination(self, new_destination) -> None` | Change the destination of the edge as *new_destination* |
| `get_weight(self) -> float` | Return the weight of the edge |
| `set_weight(self, new_weight) -> None` | Change the weight of the edge as *new_weight* |
  
> Test on this class: *TestEdge.py*
  
<br />
  
  ### <ins>***3 - GeoLocation***<ins>
  
 This class contains all the elements needed for a point 3D visualization in a directed weighted graph.
  
 Only three coordonates constitute a ```GeoLocation``` in a 3D space:
  
  - ```x```: the node’s value on the x axis.
  - ```y```: the node’s value on the y axis.
  - ```z```: the node’s value on the z axis.

    <br />

| **Methods**      |    **Explanation**        |
|-----------------|-----------------------|
| `__init__(self, x=0, y=0, z=0)` |  Initialize a new Geolocation set its parameters to 0 as default value |
| `distance(self, loc) -> float` | Returns the distance location between two nodes |
| `x()` | Returns the x axis value |
| `y()` | Returns the y axis value |
| `z()` | Returns the z axis value |
  
> Test on this class: *TestGeolocation.py*
  
  <br />
  
  ### <ins>***4 - DiGraph***<ins>
  
  
  DiGraph implemented by GraphInterface, this class gathers all the necessary components and features in order to build a Directed and Weighted Graph.
  
  The essential elements for the configuration of the ```DiGraph``` are:
  
  - ```number_of_node```: This Integer represents the amount of nodes in the graph.
  - ```number_of_edges```: This Integer represents the amount of edges in the graph.
  - ```mc```: This Integer is a counter that increments by one for any change in the graph. 
  - ```nodes```:  This a dictionary containing all the nodes in the graph.
  - ```edges```: This a dictionary containing all the edges in the graph..

| **Main methods**      |    **Explanation**        |
|-----------------|-----------------------|
| `__init__(self)` | Initialize a new Directed Graph |
| `v_size(self) -> int` | Return the amount of nodes of the graph |
| `e_size(self) -> int` | Return the amount of edges of the graph |
| `get_mc(self) -> int` | Return the mode counter (amount of changes) of the graph |
| `get_all_v(self) -> dict` | Return a dictionary of all the nodes in the graph |
| `all_in_edges_of_node(self, id1: int) -> dict` | Return a dictionary of all the nodes connected to this node in the graph|
| `all_out_edges_of_node(self, id1: int) -> dict` | Return a dictionary of all the nodes connected from this node in the graph |
| `add_edge(self, id1: int, id2: int, weight: float) -> bool` | Add an edge to the graph |
| `add_node(self, node_id: int, pos: tuple = None) -> bool` | Add a node to the graph |
| `remove_node(self, node_id: int) -> bool` | Remove the node_id from the graph |
| `remove_edge(self, node_id1: int, node_id2: int) -> bool` | Remove the edge (source: id1, dest: id2) from the graph |

> Test on this class: *TestDiGraph.py*
  
  <br />
  
   ### <ins>***5 - DiGraphAlgo***<ins>
  
  Implemented by GraphAlgoInterface, DiGraphAlgo is the most important class that does the most "hardest job". Indeed, it will use certain algorithms and import external libraries which will allow us to perform several actions on the DiGraph.
  
  `DiGraphAlgo` is characterized by only one object: a `DiGraph`.

  <br />

| **Main methods**      |    **Explanation**  | 
|-----------------|-----------------------|
| ` __init__(self, DWG: DiGraph = None)` | Initialize a new Directed Graph |
| `get_graph(self) -> GraphInterface` | Returns the directed graph on which the algorithm works on |
| `load_from_json(self, file_name: str) -> bool` | Loads a `DiGraph` to this `DiGraphAlgo` from a **JSON** format |
| `save_to_json(self, file_name: str) -> bool` | Saves this `DiGraph` to the given file name in a **JSON** format |
| `shortest_path(self, id1: int, id2: int) -> (float, list)` |  Returns the nodes in the shortest path between src to dest in a list, using `Dijkstra` |
| `centerPoint(self) -> (int, float)` | Returns the node which minimizes the max distance to all the other nodes, that means the min of all max shortest path over all nodes |
| `TSP(self, node_lst: List[int]) -> (List[int], float)` | Finds the shortest path that visits all the nodes in the list |
| `plot_graph(self) -> None` | Plots the graph in a gui |
  
> Test on this class: *TestDiGraphAlgo.py* 

  <br /> 
  
  
  <br />
  
  ## UML Diagram 📊
 <br />
  
