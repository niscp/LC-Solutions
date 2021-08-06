"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        result = []
        que = collections.deque([root])
        while que:
            level = []
            for _ in range(len(que)):
                node = que.popleft()
                level.append(node.val)
                que.extend(node.children)
            result.append(level)
        return result
        