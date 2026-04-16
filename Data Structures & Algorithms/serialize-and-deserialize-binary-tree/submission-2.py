# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        st = ""
        if root is None:
            return "n"
        st+=str(root.val)+','+self.serialize(root.left)+','+self.serialize(root.right)
        return st

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = deque(data.split(","))
        def build():
            val = vals.popleft()
            if val == "n":
                return None
            node = TreeNode(int(val))
            node.left = build()
            node.right = build()
            return node
        return build()

