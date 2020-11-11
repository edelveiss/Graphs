from collections import deque


#-------------------Graph Class----------------------
class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set() # O(1)
        # else:
        #     print(f"{vertex_id} vert has already exist in a graph")

        
        

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id] # O(1)


#-------------------earliest_ancestor function----------------------
def earliest_ancestor(ancestors, starting_node):
    
    graph = Graph()
 
    for parent, child in ancestors:
        #adding vertecies
        graph.add_vertex(parent)
        graph.add_vertex(child)
         #adding edges
        graph.add_edge(child, parent)


    #using dfs for searching the earliest ancestor. Return the longest path of ansestors
    def find_earliest_ancestor(child):
        # s = Stack()
        s = deque()
        s.append([child])
        # s.push([child])
        visited = set()
        res_ancestor = -1
        path_len = 0

        #If the input individual has no parents, the function returns -1.
        if len(graph.get_neighbors(child)) == 0:
            return res_ancestor

        # while s.size() > 0:
        while len(s) > 0:
            #pop the first parth
            path = s.pop()
            #grab the last vertex from the path
            v = path[-1]

            #check if the vertex has not been visited
            if v not in visited:
                visited.add(v)
                if  len(graph.get_neighbors(v)) == 0:
                    #If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID.
                    if (path_len < len(path) or (path_len == len(path) and res_ancestor > v)):
                        path_len = len(path)
                        res_ancestor = v
                   

                for next_v in graph.get_neighbors(v):
                    path_copy = list(path)
                    path_copy.append(next_v)
                    s.append(path_copy)

        return res_ancestor



 
    return find_earliest_ancestor(starting_node)
    



test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 2))
    