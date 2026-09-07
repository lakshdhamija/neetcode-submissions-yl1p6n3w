# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]
        def dfs(node, pathMaxVal):
            if not node: return
            if node.val >= pathMaxVal: res[0] += 1
            pathMaxVal = max(pathMaxVal, node.val)
            dfs(node.left, pathMaxVal)
            dfs(node.right, pathMaxVal)
        dfs(root, float('-inf'))
        return res[0]
