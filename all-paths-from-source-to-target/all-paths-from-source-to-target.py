class Solution:
    def __init__(self):
        self.result = []
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        path = collections.deque([0])
        target= len(graph) - 1
        self.traverse_recur(0, path, target, graph)
        return self.result
    
    def traverse_recur(self, currNode, path, target, graph):
        if currNode == target:
            self.result.append(list(path))
            return
        
        for nextNode in graph[currNode]:
            path.append(nextNode)
            self.traverse_recur(nextNode, path, target, graph)
            path.pop()
            
            
        