class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree(object):
    root = None

    def add(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._add_recursive(data, self.root)

    def _add_recursive(self, data, current_node):
        if data < current_node.val:
            if current_node.left is None:
                current_node.left = TreeNode(data)
            else:
                self._add_recursive(data, current_node.left)
        else:
            if current_node.right is None:
                current_node.right = TreeNode(data)
            else:
                self._add_recursive(data, current_node.right)

    def testsearch(self, val):
        print(self.searchBST(self.root, val))

    def searchBST(self, root, val):
        if root is None:
            return False

        if root.val == val:
            return True

        if root.left and self.searchBST(root.left, val):
            return True

        if root.right and self.searchBST(root.right, val):
            return True

        return False


    def printTree(self):
        self.printInorder(self.root)

    def printInorder(self, root):
        if root:
            # First recur on left child
            self.printInorder(root.left)
            # Then print the data of node
            print(root.val)
            # Now recur on right child
            self.printInorder(root.right)


number_tree = BinaryTree()
number_tree.add(5)
number_tree.add(2)
number_tree.add(7)
number_tree.add(1)
number_tree.add(9)
number_tree.add(3)
number_tree.printTree()

number_tree.testsearch(5)
number_tree.testsearch(4)
number_tree.testsearch(9)

boolean_tree = BinaryTree()
boolean_tree.add(True)
boolean_tree.add(False)
boolean_tree.printTree()
