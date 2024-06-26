# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getTreeNodesArr(self, root: TreeNode):
        stack = [root]
        arr = []

        while (len(stack) > 0):
            curr_node = stack.pop()

            if (curr_node.left):
                stack.append(curr_node.left)

            if (curr_node.right):
                stack.append(curr_node.right)

            arr.append(curr_node)

        arr.sort(key=lambda x: x.val)

        return arr

    def balanceBST(self, root: TreeNode, left=0, right=-1, arr=None) -> TreeNode:
        # use a recursive solution
        # find each next node for the current, left, and right
        # then repeat for the left and right subtrees
        if (arr == None):
            arr = Solution.getTreeNodesArr(self, root)

        # print(arr)

        if (right == -1):
            right = len(arr) - 1

        # print(left, right)

        if (left == right):
            result = arr[left]
            result.left, result.right = None, None
            return result

        mid = (left + right) // 2
        new_root = arr[mid]
        new_root.left, new_root.right = None, None

        # mid_left = (left + mid) // 2
        if (left <= mid - 1):
            # new_root.left = arr[mid_left]
            # new_root.left.left, new_root.left.right = None, None
            new_root.left = Solution.balanceBST(
                self, new_root, left, mid - 1, arr)

        mid_right = (mid + right) // 2
        if (mid + 1 <= right):
            # new_root.left = arr[mid_left]
            # new_root.left.left, new_root.left.right = None, None
            new_root.right = Solution.balanceBST(
                self, new_root, mid + 1, right, arr)

        return new_root
