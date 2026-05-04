# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        max_value = float('-inf')

        def helper(root, max_value):
            if not root:
                return 0

            if root.val >= max_value:
                return 1 + helper(root.left, root.val) + helper(root.right, root.val)
            return helper(root.left, max_value) + helper(root.right, max_value)
        
        return helper(root, max_value)


