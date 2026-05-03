# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def helper(self, rootOne, rootTwo):
        if not rootOne and not rootTwo:
            return True 

        if (not rootOne and rootTwo) or (rootOne and not rootTwo) or (rootOne.val != rootTwo.val):
            return False 
        
        return self.helper(rootOne.left, rootTwo.left) and self.helper(rootOne.right, rootTwo.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if root.val == subRoot.val and self.helper(root, subRoot):
            return True 
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


            

