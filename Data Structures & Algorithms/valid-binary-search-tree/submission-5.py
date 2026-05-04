# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, arr):
            if not root:
                return arr
            
            helper(root.left, arr)
            arr.append(root.val)
            helper(root.right, arr)

            return arr
        
        results = helper(root, [])
        for i in range(1, len(results)):
            if results[i] <= results[i-1]:
                return False
        
        return True
