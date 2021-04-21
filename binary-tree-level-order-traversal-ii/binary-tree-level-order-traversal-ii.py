# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        level_node = deque()
        if not root:
            return []
        level_node.append(root)
        result = []
        while level_node:
            level_size = len(level_node)
            r = []
            for _ in range(level_size):
                node = level_node.popleft()
                r.append(node.val)
                if node.left:
                    level_node.append(node.left)
                if node.right:
                    level_node.append(node.right)
            result.append(r)
        return reversed(result)
        