# Problem: Serialize and Deserialize Binary Tree
# Difficulty: Hard
# URL: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# Runtime: 90 ms
# Memory: 22.7 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        vals = []
        def preorder(node):
            if node:
                vals.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
            else:
                vals.append('#')
        preorder(root)
        return ','.join(vals)

    def deserialize(self, data):
        vals = iter(data.split(','))
        def build():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = build()
            node.right = build()
            return node
        return build()