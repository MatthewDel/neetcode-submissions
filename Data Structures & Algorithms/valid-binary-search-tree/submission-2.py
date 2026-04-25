# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, left, right):
            if root is None:
                return True 
            if root.val >= left or root.val <= right:
                return False
            return helper(root.left,root.val,right) and helper(root.right, left, root.val)
        return helper(root, float('inf'), float('-inf'))
        
        