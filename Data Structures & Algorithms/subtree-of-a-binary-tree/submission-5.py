
class Solution:   
    def isSame(self, s, t):
        if not s and not t: return True
        if not s or not t: return False
        if s.val != t.val: return False
        return self.isSame(s.left, t.left) and self.isSame(s.right, t.right)

    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if not root: return False
        if self.isSame(root, subroot): return True
        return self.isSubtree(root.left, subroot) or self.isSubtree(root.right, subroot)