class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.distance_weight = {}

    def add_point(self, new_point):
        if new_point in self.adjacency_list:
            return
        else:
            self.adjacency_list[new_point] = []

    def add_directed_route(self, start_point, end_point, distance=1.0):
        self.distance_weight[(start_point, end_point)] = distance
        self.adjacency_list[start_point].append(end_point)

    def add_undirected_route(self, point_a, point_b, distance=1.0):
        self.add_directed_route(point_a, point_b, distance)
        self.add_directed_route(point_b, point_a, distance)

    def print_graph(self):
        # print(self.distance_weight)
        # res = [ele for key in self.distance_weight for ele in key]
        # print(res)
        # for vertex in self.adjacency_list:
        # print(vertex)
        for location, v in self.distance_weight.keys():
            print(v)

    def search(self, current, destination):
        return [v for k, v in self.distance_weight.items() if k[0] == current and k[1] == destination]
