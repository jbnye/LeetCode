from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # Searching for the min depth
        # BFS will perform better than DFS, except for worst case

        # Base case: Empty tree
        if root is None:
            return 0

        deq = deque([(root, 1)])
        
        while deq:
            curr_node, curr_level = deq.popleft()
            
            # Check if is a leaf
            if curr_node.right is None and curr_node.left is None:
                return curr_level
            if curr_node.left:
                deq.append((curr_node.left,  curr_level+1))
            if curr_node.right:
                deq.append((curr_node.right, curr_level+1))
    

# my soultion
# class Solution(object):
#     def minDepth(self, root):
#         if root is None:
#             return 0
#         if root.left is None:
#             return 1 + self.minDepth(root.right)
#         if root.right is None:
#             return 1 + self.minDepth(root.left)
#         return 1 + min(self.minDepth(root.left), self.minDepth(root.right))