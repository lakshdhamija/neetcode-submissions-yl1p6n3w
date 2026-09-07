# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, pathMaxVal):
            if not node: return 0
            isGoodNode = 1 if node.val >= pathMaxVal else 0
            pathMaxVal = max(pathMaxVal, node.val)
            return isGoodNode + dfs(node.left, pathMaxVal) + dfs(node.right, pathMaxVal)
        return dfs(root, float('-inf'))
