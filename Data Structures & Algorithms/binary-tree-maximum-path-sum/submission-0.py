# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        sol = float('-inf')

        def helper(root):
            nonlocal sol

            if not root:
                return 0 

            left = helper(root.left)
            right = helper(root.right)
            left_path = max(0, left)
            right_path = max(0, right)

            sol = max(sol, root.val + left_path + right_path)

            return max(left_path + root.val, right_path + root.val)
        
        helper(root)
        return sol