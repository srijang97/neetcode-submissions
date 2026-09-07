# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        maxDia = 0

        def dfs(root):
            nonlocal maxDia
            if root is None:
                return 0
            if root.left is None and root.right is None:
                return 0

            rightDia = leftDia = 0    
            thisDia = 0

            if root.left:
                leftDia = dfs(root.left) + 1
                thisDia += leftDia
            
            if root.right:
                rightDia = dfs(root.right) + 1
                thisDia += rightDia

            maxDia = max(maxDia, thisDia)

            return max(leftDia, rightDia)

        dfs(root)
        return maxDia




            



        