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

# Evaluate a Condition Tree
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def evaluateTree(self, root):
        if root is None:
            return False

        if root.left is None and root.right is None:
            return bool(root.val)

        left_result = self.evaluateTree(root.left)
        right_result = self.evaluateTree(root.right)

        if root.val == 2:
            return left_result or right_result
        elif root.val == 3:
            return left_result and right_result


# Create the binary tree
root = TreeNode(3)
root.left = TreeNode(2)
root.right = TreeNode(1)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)

# Create an instance of Solution
solution = Solution()
print(solution.evaluateTree(root))


# Invert a Binary Tree
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def invertTree(self, root):
        if root:
            self.invertTree(root.left)
            self.invertTree(root.right)
            temp = root.left
            root.left = root.right
            root.right = temp
            return root

    def printTree(self, root):
        if root:
            print(root.val)
            self.printTree(root.left)
            self.printTree(root.right)
        return root

tree = TreeNode(4)
tree.left = TreeNode(2)
tree.left.left = TreeNode(1)
tree.left.right = TreeNode(3)
tree.right = TreeNode(7)
tree.right.left = TreeNode(6)
tree.right.right = TreeNode(9)

test = Solution()
test.invertTree(tree)
test.printTree(tree)

# Find the range of Sums Binary Tree
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def rangeSumBST(self, root, low, high):
        if root is None:
            return 0

        sum_value = 0

        if low <= root.val <= high:
            sum_value += root.val

        sum_value += self.rangeSumBST(root.left, low, high)
        sum_value += self.rangeSumBST(root.right, low, high)

        return sum_value

root = TreeNode()
root.left = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right = TreeNode(10)
root.right.right = TreeNode(18)

test = Solution()
print(test.rangeSumBST(root, 7, 15))

# Check if Leafs are similar
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def leafSimilar(self, root1, root2):
        leaves1, leaves2 = [], []
        self.traversal(root1, leaves1)
        self.traversal(root2, leaves2)
        return leaves1 == leaves2

    def traversal(self, root, leaves):
        if root:
            if root.left is None and root.right is None:
                leaves.append(root.val)

            self.traversal(root.left, leaves)
            self.traversal(root.right, leaves)
        return leaves

test = Solution()
tree1 = TreeNode(5)
tree1.left = TreeNode(3)
tree1.left.left = TreeNode(2)
tree1.left.right = TreeNode(4)
tree1.left.left.left = TreeNode(1)
tree1.left.right.left = TreeNode(3)
tree1.left.right.right = TreeNode(7)
tree1.right = TreeNode(9)
tree1.right.left = TreeNode(6)
tree1.right.right = TreeNode(5)

tree2 = TreeNode(1)
tree2.left = TreeNode(1)
tree2.left.left = TreeNode(3)
tree2.left.right = TreeNode(7)
tree2.left.left.left = TreeNode(1)
tree2.left.left.right = TreeNode(3)
tree2.right = TreeNode(1)
tree2.right.left = TreeNode(6)
tree2.right.right = TreeNode(5)


print(test.leafSimilar(tree1, tree2))

# Calculate the sum of nodes from root to leaf
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def pathSum(self, root):
        binary_paths = []
        self.sumRootToLeaf(root, binary_paths)
        print(binary_paths)
        self.binCalculate(binary_paths)

    def sumRootToLeaf(self, root, paths):
        if root:
            if root.left is None and root.right is None:
                paths.append(root.val)
                paths.append(2)
            else:
                paths.append(root.val)
                self.sumRootToLeaf(root.left, paths)
                self.sumRootToLeaf(root.right, paths)
        return root

    def binCalculate(self, paths):
        i = 0
        while i < len(paths):

            i += 1

tree = TreeNode(1)
tree.left = TreeNode(0)
tree.left.left = TreeNode(0)
tree.left.right = TreeNode(1)
tree.right = TreeNode(1)
tree.right.left = TreeNode(0)
tree.right.right = TreeNode(1)

test = Solution()
test.pathSum(tree)


# Convert from Morse code To alphabet using Binary Tree
class TreeNode(object):
    def __init__(self, val="", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Converter(object):
    root = TreeNode()
    root.left = TreeNode("E")
    root.left.left = TreeNode("I")
    root.left.right = TreeNode("A")
    root.left.left.left = TreeNode("S")
    root.left.left.right = TreeNode("U")
    root.left.left.left.left = TreeNode("H")
    root.left.left.left.right = TreeNode("V")
    root.left.left.right.left = TreeNode("F")
    root.left.right = TreeNode("A")
    root.left.right.left = TreeNode("R")
    root.left.right.left.left = TreeNode("L")
    root.left.right.right = TreeNode("W")
    root.left.right.right.left = TreeNode("P")
    root.left.right.right.right = TreeNode("J")

    root.right = TreeNode("T")
    root.right.left = TreeNode("N")
    root.right.left.left = TreeNode("D")
    root.right.left.left.left = TreeNode("B")
    root.right.left.left.right = TreeNode("X")
    root.right.left.right = TreeNode("K")
    root.right.left.right.left = TreeNode("C")
    root.right.left.right.right = TreeNode("Y")
    root.right.right = TreeNode("M")
    root.right.right.left = TreeNode("G")
    root.right.right.left.left = TreeNode("Z")
    root.right.right.left.right = TreeNode("Q")
    root.right.right.right = TreeNode("O")

    def printTree(self, root):
        if root:
            self.printTree(root.left)
            print(root.val)
            self.printTree(root.right)

    def morseToAlphabet(self, sentence):
        alphabet_sentence = ""
        for character in sentence:
            alphabet_sentence += self.morseRecursion(character)
        return alphabet_sentence

    def morseRecursion(self, character):
        if character == " ":
            return " "
        node = self.root
        for beep in character:
            if beep == ".":
                node = node.left
            else:
                node = node.right
        return node.val


test = Converter()
print(test.morseToAlphabet(["....", ".", "._..", "._..", "___", " ", ".__", "___", "._.", "._..", "_.."]))
