# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# class Solution:
#     def maxPathSum(self, root: Optional[TreeNode]) -> int:
#         def dfs(node) -> int:
#             if not node: return 0
#             leftMax = max(0, dfs(node.left))
#             rightMax = max(0, dfs(node.right))
#             return max(leftMax, rightMax, leftMax + node.val, rightMax + node.val, leftMax + rightMax + node.val)
#         return dfs(root)

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize with a real integer value from the root node
        # This guarantees our final answer is an int, not a float
        self.max_sum = root.val

        def dfs(node) -> int:
            if not node: 
                return 0 # An empty node contributes 0 to the path sum
            
            # Calculate the max path sum from left and right subtrees.
            # If a subtree returns a negative sum, we ignore it by taking max(..., 0)
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)
            
            # Price of a new path: current node acts as the highest turning point
            current_path_sum = node.val + left_gain + right_gain
            
            # Update our global maximum integer
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # For the parent node, we can only continue down ONE branch
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return self.max_sum
