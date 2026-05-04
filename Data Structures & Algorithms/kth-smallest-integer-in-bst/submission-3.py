# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        count = k
        def helper(root):
            nonlocal count 
            if not root or count < 0:
                return root
            
            left = helper(root.left)
            if left:
                return left 

            count -= 1
            if count == 0:
                return root

            return helper(root.right)
        return helper(root).val
