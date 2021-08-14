class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        count = 0
        graph = {i:[] for i in range(n)}
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        visited = [False for _ in range(n)]
        for node in range(n):
            if visited[node] == False:
                self.dfs(graph, visited, node)
                count += 1
        return count

    def dfs(self, graph, visited, start):
        tracker = collections.deque()
        tracker.append(start)
        
        while tracker:
            node = tracker.popleft()
            connected_nodes = graph.get(node)
            for cnode in connected_nodes:
                if visited[cnode]:
                    continue
                tracker.append(cnode)
                visited[cnode] = True
            
            
        
            
        