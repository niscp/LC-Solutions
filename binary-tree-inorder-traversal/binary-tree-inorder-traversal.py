# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result_list = []
        if root is None:
            return result_list
        self.inorderTraversal_recur(root, result_list)
        return result_list
    
    def inorderTraversal_recur(self, root, result_list):
        if root is None:
            return
        self.inorderTraversal_recur(root.left, result_list)
        result_list.append(root.val)
        self.inorderTraversal_recur(root.right, result_list)
        
        
        