# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getLonelyNodes(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        nodes_queue = deque()
        nodes_queue.append(root)
        
        result_list = []
        while nodes_queue:
            node_data = nodes_queue.popleft()
            if node_data.left and not node_data.right:
                result_list.append(node_data.left.val)
                nodes_queue.append(node_data.left)

            if not node_data.left and node_data.right:
                result_list.append(node_data.right.val)
                nodes_queue.append(node_data.right)

            if node_data.left and node_data.right:
                nodes_queue.append(node_data.left)
                nodes_queue.append(node_data.right)

        return result_list
