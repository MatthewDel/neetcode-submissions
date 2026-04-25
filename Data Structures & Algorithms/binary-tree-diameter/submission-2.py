# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.sol = 0

        def helper(root):
            if root is None:
                return 0 
            left = helper(root.left)
            right = helper(root.right)
            calc = left + right
            if calc > self.sol:
                self.sol = calc 
            return max(left, right) + 1
        
        helper(root)
        return self.sol