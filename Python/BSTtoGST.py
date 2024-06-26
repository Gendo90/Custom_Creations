# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode, total=0) -> TreeNode:
        # add node to sum of right subtree nodes to get new node value
        # then run recursively on left and right children, respectively
        # post order traversal
        # print(root)
        if (not (root.left or root.right)):
            root.val += total
            return root

        # right, node, left
        if (root.right):
            Solution.bstToGst(self, root.right, total)
            total = root.right.val
            leftmost_val_above = root.right.left
            while (leftmost_val_above):
                total = leftmost_val_above.val
                leftmost_val_above = leftmost_val_above.left

        root.val += total
        # print(root.val)

        if (root.left):
            Solution.bstToGst(self, root.left, root.val)
            total = root.left.val

        return root
