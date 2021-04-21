# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        stack = [root]
        parent_map = {root:None}
        
        while p not in parent_map or q not in parent_map:
            node = stack.pop()
            
            if node.left:
                parent_map[node.left] = node
                stack.append(node.left)
                
            if node.right:
                parent_map[node.right] = node
                stack.append(node.right)
        
        parent_list = set()
        
        while p:
            parent_list.add(p)
            p = parent_map[p]
        
        while q not in parent_list:
            q = parent_map[q]
        
        return q
            
        