class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        visited = [0 for _ in range(len(isConnected))]
        count = 0
        for i in range(len(visited)):
            if visited[i] == 0:
                count += 1
                dfs(isConnected, visited, i)
        
        return count

def dfs(graph, visited, idx):
    for index in range(len(graph)):
        if graph[idx][index] == 1 and visited[index] == 0:
            visited[index] = 1
            dfs(graph, visited, index)
        