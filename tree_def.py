


class TreeNode:
    def __init__(self, value):
        # |_left_|_Value_|_right_|
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value is None:
            return TreeNode(value)
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

    def display_tree(self):
        if self.left:
            self.left.display_tree()
        print(self.value)
        if self.right:
            self.right.display_tree()

    def search_tree(self, target):
        if self.value == target:
            return 1
        if self.value > target:
            return self.search_tree(self.left, target)
        else:
            return self.search_tree(self.right, target)
        return -1

values = [10, 5, 15, 3, 7, 12]
root = 11
t = TreeNode(root)
for val in values:
    t.insert(val)

t.display_tree()
