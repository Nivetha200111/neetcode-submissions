# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode],lo=float("-inf"), hi=float("inf")) -> bool:
        if not root:
            return True
        if root.val >= hi: 
            return False
        if root.val <= lo:
            return False
        return self.isValidBST(root.left,lo,root.val) and self.isValidBST(root.right,root.val,hi)