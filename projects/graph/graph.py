"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

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
        else:
            print(f"{vertex_id} vert has already exist in a graph")

        
        

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

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = Queue()
        queue.enqueue(starting_vertex)
        #set for tracking visited verticies
        visited_verts = set()

        while queue.size() > 0:
            curr_vert =  queue.dequeue()
            if curr_vert not in visited_verts:
                visited_verts.add(curr_vert)
                print(curr_vert)
                for e in self.get_neighbors(curr_vert):
                    queue.enqueue(e)




    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        stack.push(starting_vertex)
        visited_verts = set()

        while stack.size() > 0:
            curr_vert = stack.pop()
            if curr_vert not in visited_verts:
                visited_verts.add(curr_vert)
                print(curr_vert)
                for e in self.get_neighbors(curr_vert):
                    stack.push(e)



    def dft_recursive(self, starting_vertex, visited_verts = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        
        if visited_verts == None:
            visited_verts = set()
        visited_verts.add(starting_vertex)
        print(starting_vertex)

        for e in self.get_neighbors(starting_vertex):
            if e not in visited_verts:
                self.dft_recursive(e, visited_verts)


        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = Queue()
        queue.enqueue([starting_vertex])
       
        visited_verts = set()
        while queue.size() > 0:
            path = queue.dequeue()
            print("path",path)
            curr_vert = path[-1]
            if curr_vert not in visited_verts:
                if curr_vert == destination_vertex:
                    return path
                
                visited_verts.add(curr_vert)

                #Queue up new paths wiht each neighbor
                for e in self.get_neighbors(curr_vert):
                    #make a copy of a path
                   
                    new_path = list(path)
                    
                    new_path.append(e)
                    print("append new_path e:",new_path)
                    queue.enqueue(new_path)
                    print("queue",queue)
        return None





    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        stack.push([starting_vertex])
        visited_verts = set()
        while stack.size() > 0:
            path = stack.pop()
            curr_vert = path[-1]
            if curr_vert not in visited_verts:
                if curr_vert == destination_vertex:
                    return path
                
                visited_verts.add(curr_vert)

                #Queue up new paths wiht each neighbor
                for e in self.get_neighbors(curr_vert):
                    #make a copy of a path
                    new_path = list(path)
                    new_path.append(e)
                    stack.push(new_path)
        return None

    def dfs_recursive(self, starting_vertex, destination_vertex, visited_verts=None, path = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited_verts == None:
            visited_verts = set()
        if starting_vertex not in visited_verts:
            visited_verts.add(starting_vertex)

        if path is None:
            path = []

        #Create a new path by adding current path and the starting_vartex
        path = path + [starting_vertex]

        #Check if we have reached the destination - return path
        if starting_vertex == destination_vertex:
            return path

        for e in self.get_neighbors(starting_vertex):
            if e not in visited_verts:
                new_path = self.dfs_recursive(e, destination_vertex,visited_verts, path )
                if new_path is not None:
                    return new_path

        #Base case: all neighbors have been visited
        return None

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("*"*10, "dft","*"*10)
    graph.dft(1)
    print("*"*10, "dft_recursive","*"*10)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("*"*10, "bfs","*"*10)
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("*"*10, "dfs","*"*10)
    print(graph.dfs(1, 6))
    print("*"*10, "dfs_recursive","*"*10)
    print(graph.dfs_recursive(1, 6))
