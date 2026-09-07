# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs_subtree(tree1, tree2):
            if not tree1 and not tree2:
                return True
            if tree1 and tree2 and tree1.val == tree2.val:
                return dfs_subtree(tree1.left, tree2.left) and dfs_subtree(tree1.right, tree2.right)
            else:
                return False
            
        found = False
        
        def dfs(root):
            nonlocal found

            if root is None:
                return

            if root.val == subRoot.val:
                if dfs_subtree(root, subRoot):
                    found = True

            dfs(root.left)
            dfs(root.right)

            return

        dfs(root)
        return found
            
