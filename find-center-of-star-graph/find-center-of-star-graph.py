class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if len(edges) < 1:
            return -1
        fp = edges[0][0]
        sp = edges[0][1]
        res = None
        
        for edge in edges[1:2]:
            if edge[0] == fp:
                res = fp
            elif edge[0] == sp:
                res = sp
            elif edge[1] == fp:
                res = fp 
            elif edge[1] == sp:
                res = sp
        return res
            
        