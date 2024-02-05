import numpy as np
import heapq
from typing import Union

class Graph:

    def __init__(self, adjacency_mat: Union[np.ndarray, str]):
        """
    
        Unlike the BFS assignment, this Graph class takes an adjacency matrix as input. `adjacency_mat` 
        can either be a 2D numpy array of floats or a path to a CSV file containing a 2D numpy array of floats.

        In this project, we will assume `adjacency_mat` corresponds to the adjacency matrix of an undirected graph.
    
        """
        if type(adjacency_mat) == str:
            self.adj_mat = self._load_adjacency_matrix_from_csv(adjacency_mat)
        elif type(adjacency_mat) == np.ndarray:
            self.adj_mat = adjacency_mat
        else: 
            raise TypeError('Input must be a valid path or an adjacency matrix')
        self.mst = None

    def _load_adjacency_matrix_from_csv(self, path: str) -> np.ndarray:
        with open(path) as f:
            return np.loadtxt(f, delimiter=',')

    def construct_mst(self):
        """
    
        TODO: Given `self.adj_mat`, the adjacency matrix of a connected undirected graph, implement Prim's 
        algorithm to construct an adjacency matrix encoding the minimum spanning tree of `self.adj_mat`. 
            
        `self.adj_mat` is a 2D numpy array of floats. Note that because we assume our input graph is
        undirected, `self.adj_mat` is symmetric. Row i and column j represents the edge weight between
        vertex i and vertex j. An edge weight of zero indicates that no edge exists. 
        
        This function does not return anything. Instead, store the adjacency matrix representation
        of the minimum spanning tree of `self.adj_mat` in `self.mst`. We highly encourage the
        use of priority queues in your implementation. Refer to the heapq module, particularly the 
        `heapify`, `heappop`, and `heappush` functions.

        """
        #initialize mst as empty
        self.mst = np.zeros(self.adj_mat.shape)

        #nodelist = [(np.inf, node, None) for node in list(range(self.adj_mat.shape[0]))]
        heap = [(0, 0, None)] # (edgeweight, to, from)
        heapq.heapify(heap)
        visited = []
        print(heap)

        while heap and len(visited) < self.adj_mat.shape[0]:
            smallest = heapq.heappop(heap)
            to = smallest[1]
            origin = smallest[2]
            # because heapq doesnt have an efficient way to search the heap, old nodes are still in there
            if to in visited:
                continue
            # add node/edge to mst
            visited.append(to)
            if origin != None:
                self.mst[origin, to] = self.adj_mat[origin, to]
                self.mst[to, origin] = self.adj_mat[origin, to]
            # add children to the heap
            for i in range(self.adj_mat.shape[1]):
                if i not in visited and self.adj_mat[to, i] != 0:
                    heapq.heappush(heap, (self.adj_mat[to, i], i, to))











