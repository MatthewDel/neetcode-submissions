# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def helper(root, sub):
            if (not root and sub) or (root and not sub) or (sub and root and (sub.val != root.val)):
                return False
            if(not root and not sub):
                return True 
            return helper(root.left, sub.left) and helper(root.right, sub.right)

        def dfs(root):
            if root is None:
                return False
            if root.val == subRoot.val:
                if(helper(root, subRoot)):
                    return True 
            return dfs(root.left) or dfs(root.right)
        
        return dfs(root)