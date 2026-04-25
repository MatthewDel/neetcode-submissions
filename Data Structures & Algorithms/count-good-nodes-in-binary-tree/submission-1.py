# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def goodNodes(self, root: TreeNode) -> int:
        def check(root, max_value):
            if not root:
                return 0
            new_value = max(max_value, root.val)
            if root.val >= max_value:
                return 1 + check(root.left, new_value) + check(root.right, new_value)
            else:
                return check(root.left, new_value) + check(root.right, new_value)
        return check(root, float('-inf'))