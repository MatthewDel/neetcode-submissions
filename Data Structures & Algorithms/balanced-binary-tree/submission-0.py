# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root: 
                return 0
            
            res_left = dfs(root.left)
            res_right = dfs(root.right)

            if res_left == -1 or res_right == -1 or abs(res_left - res_right) > 1:
                return -1
            else:
                return max(res_left , res_right) + 1
        
        if dfs(root) == -1:
            return False
        else:
            return True 