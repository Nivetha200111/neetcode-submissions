# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "#"
        l = self.serialize(root.left)
        r = self.serialize(root.right)
        return f"{root.val},{l},{r}"

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # if data[]
        # root = TreeNode(data[0])
        # left = desirialize(data[1:])
        # curr = TreeNode(0)
        it = iter(data.split(','))
        # for c in it:
        #     if c == '#':
        #         return None
        #     curr.val = c
        #     l = self.deserialize
            
        def build():
            t = next(it)
            if t == '#':
                return None
            node = TreeNode(int(t))
            node.left = build()
            node.right = build()
            return node
        return build()        
        
        