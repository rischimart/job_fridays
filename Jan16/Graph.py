from collections import defaultdict
import Queue
from sys import argv

class Graph:

    def __init__(self, filename):
        self.adj = defaultdict(list)
        self.build_graph_from_file(filename)
        
    def build_graph_from_file(self, filename):
        with open(filename, 'r') as input_file:
            for line in input_file:
                src, dest = line.strip().split(' ')
                self.adj[src].append(dest)
                self.adj[dest].append(src)
            input_file.close()


    def backtrack(self, dest, src, upstream_table):
        path = [dest]
        while True:
            last = path[-1]
            if last == src:
                return path[::-1]
            path.append(upstream_table[last])
        
        
    def shortest_path(self, src, dest):
        if (src not in self.adj) or (dest not in self.adj):
            raise ValueError("Invalid input!")
            
        queue = Queue.Queue()
        queue.put(src)
        visited = set()
        upstream = dict()
        while not queue.empty():
            node = queue.get()
            if node == dest:
                return self.backtrack(node, src, upstream)
 
            for neighbor in self.adj[node]:
                if neighbor not in visited:
                    upstream[neighbor] = node
                    queue.put(neighbor)
            visited.add(node)
        return []

if __name__ == '__main__':
    graph = Graph(argv[1])
    print graph.shortest_path(argv[2], argv[3])
