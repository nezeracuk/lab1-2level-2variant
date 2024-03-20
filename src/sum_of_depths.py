class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def sum_of_depths(root: TreeNode, depth=0) -> int:
    if root is None:
        return 0
    else:
        depth_left = depth + sum_of_depths(root.left, depth + 1)
        depth_right = sum_of_depths(root.right, depth + 1)
        final_depth = depth_left + depth_right

        return final_depth


