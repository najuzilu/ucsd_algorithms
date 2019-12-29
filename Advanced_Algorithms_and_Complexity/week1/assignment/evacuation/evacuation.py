# python3
import queue
import sys
import copy

class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0

# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)] # keeps track of len of ingoing and outgoing edges per node

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow

def read_data():
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, capacity)
    return graph

def shortest_path_distance(graph, s, t):
    # Initialize queue
    L = queue.Queue(maxsize = len(graph.edges))
    # Initialize distance list
    distance = [len(graph.edges) for _ in range(len(graph.edges))]
    # Initialize previous to nil
    previous = [None for _ in range(len(graph.edges))]
    # Set starting node distance to 0
    distance[s] = 0
    # Add starting node to queue
    L.put(s)
    # Initialize min_flow array
    min_flow = [None for _ in range(graph.size())]

    # While queue is not empty
    while not L.empty():
        # Take the first element
        dequeue_node = L.get()
        for node in graph.get_ids(dequeue_node):
            edge = graph.get_edge(node)
            if distance[edge.v] == len(graph.edges):
                L.put(edge.v)
                # print(edge.u, '-', edge.v, ';', edge.flow, ',', edge.capacity)
                min_flow[edge.v] = edge.flow
                distance[edge.v] = distance[dequeue_node] + 1
                previous[edge.v] = dequeue_node
    return distance, previous, min_flow

def deconstruct_path(graph, from_, to, previous, min_flow):
    """
        Deconstructs path and returns str of path and 
    """
    path = [to]

    while to:
        if to == from_:
            path = [previous[to]] + path
            break

        path = [previous[to]] + path
        to = previous[to]

    min_value = []
    for i in range(1, len(path)):
        min_value.append(min_flow[i])
    return path, min(min_value)

def residual_graph(graph, s, t):
    residual_graph = copy.copy(graph)

    L = queue.Queue(maxsize = len(residual_graph.edges))
    distance = [len(residual_graph.edges) for _ in range(len(residual_graph.edges))]
    distance[s] = 0
    L.put(s)

    while not L.empty():
        dequeue_node = L.get()
        for node in residual_graph.get_ids(dequeue_node):
            edge = residual_graph.get_edge(node)
            edge.flow = edge.capacity
            # print(edge.u, '-', edge.v, ';', edge.flow, ',', edge.capacity)
            if distance[edge.v] == len(residual_graph.edges):
                L.put(edge.v)
                distance[edge.v] = distance[dequeue_node] + 1

    return residual_graph

def max_flow(graph, from_, to):
    if len(graph.edges) == 0:
        return 0

    flow = 0
     # Compute residual graph by placing capacity to flow
    g_f = residual_graph(graph, from_, to)
    distance, previous, min_flow = shortest_path_distance(g_f, from_, to)
    print(">>>", deconstruct_path(g_f, from_, to, previous, min_flow))



    
    # Have successfully computed shortest path
    # distance, previous = shortest_path_distance(graph, from_, to)
    # print(">>>", deconstruct_path(from_, to, distance, previous, graph))

    # # # Basic idea of Ford-Fulkerson Algorithm
    # # while True:
    # #     compute G_f
    # #     find shortest path from_->to path P in G_f
    # #     if no path: return flow
    # #     X -> min edge in shortest path
    # #     g flow with g_e = X for edge in P
    # #     f <- f + g

    return flow


if __name__ == '__main__':
    graph = read_data()
    print(max_flow(graph, 0, graph.size() - 1))
