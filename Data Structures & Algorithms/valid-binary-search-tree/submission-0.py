# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(root, max_value, min_value):
            if not root:
                return True 
            if max_value > root.val > min_value:
                return check(root.left, root.val, min_value) and check(root.right, max_value, root.val)
            else:
                return False
        return check(root, float('inf'), float('-inf'))
            