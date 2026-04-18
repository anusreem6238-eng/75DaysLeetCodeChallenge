# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        
        # If it's a leaf node, check if remaining sum equals node value
        if not root.left and not root.right:
            return targetSum == root.val
        
        # Recur on left and right subtrees
        remaining_sum = targetSum - root.val
        
        return (self.hasPathSum(root.left, remaining_sum) or
                self.hasPathSum(root.right, remaining_sum))