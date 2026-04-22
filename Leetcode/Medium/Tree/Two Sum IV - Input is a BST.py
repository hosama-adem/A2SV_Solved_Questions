# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        ans = []
        def dfs(node):
            if node:
                dfs(node.left)
                ans.append(node.val)
                dfs(node.right)
            
        dfs(root)
        
        for i in ans:
            if k - i in ans:
                if k - i == i and ans.count(i) < 2:  
                    return False
                    
                return True
            
        return False

        
        
