from src.classes.Edge import Edge
from src.classes.Geolocation import Geolocation


class Node:

    # Initialize a new node
    def __init__(self, location=Geolocation(), key=0):
        self.key = key
        self.location = location
        self.info = ""
        self.tag = 0

        self._in = {}
        self._out = {}

    # Return the location of the node
    def get_Location(self) -> Geolocation:
        return self.location

    # Change the location of the node to new_loc
    def set_location(self, new_loc) -> None:
        self.location = new_loc

    # Return the key of the node
    def get_key(self) -> int:
        return self.key

    # Change the key of the node to new_key
    def set_key(self, new_key) -> None:
        self.key = new_key

    # Return the info of the node
    def get_info(self) -> str:
        return self.info

    # Change the info of the node to new_key
    def set_info(self, new_info) -> None:
        self.info = new_info

    # Return the tag of the node
    def get_tag(self) -> int:
        return self.tag

    # Change the tag of the node to new_key
    def set_tag(self, new_tag) -> None:
        self.tag = new_tag

    # Return a dictionary of incoming edges of the node
    def get_in(self) -> dict:
        return self._in

    # Return a dictionary of outgoing edges of the node
    def get_out(self) -> dict:
        return self._out

    # Add a new node as the destination of a new edge
    def add_in(self, new_key, weight) -> None:
        self._in[new_key] = Edge(new_key, self.key, weight)

    # Add a new node as the source of a new edge
    def add_out(self, new_key, weight) -> None:
        self._out[new_key] = Edge(self.key, new_key, weight)

    # Return true iff,succeed to remove the node_data from the _in
    def remove_in(self, node_data: int) -> bool:
        if self._in.__contains__(node_data):
            self._in.pop(node_data)
            return True
        else:
            return False

    # Return true iff,succeed to remove the node_data from the _out
    def remove_out(self, node_data: int) -> bool:
        if self._out.__contains__(node_data):
            self._out.pop(node_data)
            return True
        else:
            return False
