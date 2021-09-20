# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def serialize_recur(root, string):
            if root is None:
                string += "None,"
            else:
                string += str(root.val) + ","
                string = serialize_recur(root.left, string)
                string = serialize_recur(root.right, string)
            return string
        
        return serialize_recur(root, "")
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def deserialize_recur(data_list):
            if data_list[0] =="None":
                data_list.pop(0)
                return None
            root = TreeNode(data_list[0])
            data_list.pop(0)
            
            root.left = deserialize_recur(data_list)
            root.right = deserialize_recur(data_list)
            return root
        
        data_list = data.split(",")
        root = deserialize_recur(data_list)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))