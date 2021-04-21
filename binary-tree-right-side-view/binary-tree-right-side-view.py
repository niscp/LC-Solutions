# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        my_queue = deque()
        result_list = []
        if root is None:
            return result_list
        my_queue.append(root)
        while my_queue:
            level_size = len(my_queue)
            r = []
            for item in range(level_size):
                node_pop = my_queue.popleft()
                r.append(node_pop.val)
                if node_pop.left:
                    my_queue.append(node_pop.left)
                if node_pop.right:
                    my_queue.append(node_pop.right) 
            result_list.append((r[-1]))
        return result_list