# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        level_node = deque()
        if not root:
            return []
        level_node.append(root)
        result_list = []
        flag = False
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
            flag = not flag
            if flag:
                result_list.append(r)
            else:
                result_list.append(reversed(r))
        return result_list
                
                    