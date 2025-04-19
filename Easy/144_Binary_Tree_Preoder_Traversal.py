# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        ans = []
        if root is None:
            return []
        else:
            self.helper(root, ans)
        return ans
    def helper(self, root, ans):
        if root is None:
            return
        ans.append(root.val)
        self.helper(root.left, ans)
        self.helper(root.right, ans)

