class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        
        connections.sort(key = lambda x:x[2])
        uf = UnionFind(n)
        cost = 0
        vertices = set()
        for parent, child, c in connections:
            vertices.add(parent)
            vertices.add(child)
            if uf.union(parent, child):
                cost += c
        
        if len(vertices) != n:
            return -1
        
        conn = set()
        for i in range(1, n):
            conn.add(uf.find(i))
        
        return cost if len(conn) == 1 else -1 
    
            
class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size+1)]

    def union(self, parent, child):
        rootX = self.find(parent)
        rootY = self.find(child)
        if rootX == rootY:
            return False
        self.parent[rootX] = rootY
        return True
    
    def find(self, node):
        root = node
        
        while root != self.parent[root]:
            root = self.parent[root]
        
        p = node
        while p!= root:
            parent = self.parent[p]
            self.parent[p] = root
            p = parent
        return root
                