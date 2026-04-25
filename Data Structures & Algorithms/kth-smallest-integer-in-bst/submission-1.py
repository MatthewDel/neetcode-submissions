# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.curr = 1
        self.val = -1 
        def helper(root):
            if not root:
                return 
            helper(root.left) 
            if self.curr == k:
                self.val = root.val 
                self.curr += 1
                return
            self.curr += 1
            helper(root.right)
        helper(root)
        return self.val 
        
