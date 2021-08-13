class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if len(prerequisites) < 1:
            return True
        indegreeMap = {}
        vertexMap = {}
        for idx in range(numCourses):
            indegreeMap[idx] = 0

        for idx in range(numCourses):
            vertexMap[idx] = []
        
        for edge in prerequisites:
            parent = edge[1]
            child = edge[0]
            
            indegreeMap[child] += 1
            vertexMap[parent].append(child)
        
        source = deque()
        for k, v in indegreeMap.items():
            if v == 0:
                source.append(k)
        
        sorted_order = []
        while source:
            node = source.popleft()
            sorted_order.append(node)
            child_list = vertexMap[node]
            for child in child_list:
                if child in indegreeMap:
                    indegreeMap[child] -= 1
                    if indegreeMap[child] == 0:
                        source.append(child)
                        del indegreeMap[child]
        
        return len(sorted_order) == numCourses
                
        
        
        
        
        