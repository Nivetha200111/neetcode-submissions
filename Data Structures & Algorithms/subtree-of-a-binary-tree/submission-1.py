# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if root.val == subroot.val and self.same(root,subroot):
            return True
        return self.isSubtree(root.left,subroot) or self.isSubtree(root.right,subroot)

    def same(self,a,b):
        if not a and not b:
            return True
        if not a or not b or a.val!=b.val:
            return False
        return self.same(a.left,b.left) and self.same(a.right,b.right)
        