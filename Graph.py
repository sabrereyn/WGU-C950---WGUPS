class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.distance_weight = {}

    def add_point(self, new_point):
        """ Adds an address as a vertex

        :param new_point: address
        :return: if address is already in the list, return
        """
        if new_point in self.adjacency_list:
            return
        else:
            self.adjacency_list[new_point] = []

    def add_directed_route(self, start_point, end_point, distance=1.0):
        """ Adds a route from one address to another

        :param start_point: an address
        :param end_point: an address
        :param distance: the distance between the two addresses
        """
        self.distance_weight[(start_point, end_point)] = distance
        self.adjacency_list[start_point].append(end_point)

    def add_undirected_route(self, point_a, point_b, distance=1.0):
        """ Adds a route from one address to another, both ways.

        :param point_a: an address
        :param point_b: an address
        :param distance: the distance between the two addresses
        """
        self.add_directed_route(point_a, point_b, distance)
        self.add_directed_route(point_b, point_a, distance)

    def search(self, current, destination):
        """ Search the list using the two addresses as key and return the value or distance.

        :param current: starting address
        :param destination: destination address
        :return: distance between the two addresses
        """
        return [v for k, v in self.distance_weight.items() if k[0] == current and k[1] == destination]
