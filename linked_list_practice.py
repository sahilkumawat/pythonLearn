# Merge 2 Linked Lists
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    head3 = None
    tail3 = None
    def fib(self, n):
        if n == 0 or n == 1:
            return n
        else:
            return self.fib(n - 1) + self.fib(n - 2)

    def mergeTwoLists(self, list1, list2):
        curr1 = list1.head
        curr2 = list2.head
        if curr1 and curr2:
            if curr1.val > curr2.val:
                node = ListNode(curr1.val)
                if self.head3 is None:
                    self.head3 = node
                else:
                    self.head3.next = node
                    self.mergeTwoLists(curr1.next, curr2)
            else:
                node = ListNode(curr2.val)
                if self.head3 is None:
                    self.head3 = node
                else:
                    self.head3.next = node
                    self.mergeTwoLists(curr1, curr2.next)

    def isPowerOfFour(self, n):
        if n == 1:
            return True
        elif n < 3:
            return False
        else:
            return self.isPowerOfFour(n // 3) if n % 3 == 0 else False


test = Solution()
print(test.isPowerOfFour(2))



class LinkedList(object):
    head = None
    tail = None

    def __init__(self, list):
        i = 0
        while i < len(list):
            node = ListNode(list[i])
            self.append(node)
            i += 1

    def append(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def ret(self):
        return self.head


# Intersection and Union of 2 Linked Lists
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    head1 = None
    tail1 = None
    head2 = None
    tail2 = None
    head3 = None
    tail3 = None

    def intersectionofTwoLL(self, list1, list2):
        node1 = list1.ret()
        intersection_list = LinkedList([])

        while node1:
            node2 = list2.ret()
            while node2:
                if node1.val == node2.val:
                    intersection_list.append(ListNode(node2.val))
                node2 = node2.next
            node1 = node1.next

        return intersection_list

    def unionofTwoLL(self, list1, list2):
        node1 = list1.ret()
        union_list = LinkedList([])
        check = True
        while node1:
            node2 = list2.ret()
            while node2:
                if node1.val == node2.val:
                    check = False
                node2 = node2.next
            if check:
                union_list.append(ListNode(node1.val))
            node1 = node1.next
            check = True

        node2 = list2.head

        while node2:
            node1 = list1.ret()
            while node1:
                if node1.val == node2.val:
                    check = False
                node1 = node1.next
            if check:
                union_list.append(ListNode(node2.val))
            node2 = node2.next
            check = True

        return union_list

    def makeLinkedList(self, list):
        linked_list = LinkedList(list)
        return linked_list

    def printList(self, linked_list):
        current = linked_list.ret()
        while current:
            print(current.val)
            current = current.next


test = Solution()
list1 = test.makeLinkedList([0, 1, 2, 3, 5])
list2 = test.makeLinkedList([1, 2, 3, 4, 6])
union_list = test.unionofTwoLL(list1, list2)
test.printList(union_list)


# Check if a Linked List has a cycle
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    head = None
    tail = None

    def hasCycle(self, head):
        node_slow = self.head
        node_fast = self.head
        while node_slow and node_slow.next:
            node_slow = node_slow.next.next
            node_fast = node_fast.next
            if node_slow == node_fast:
                return True
        return False


    def createCycle(self, head):
        if self.head is None:
            return
        self.tail.next = self.head

    def append(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        print(self.tail.val)

    def makeLinkedList(self, list):
        i = 0
        while i < len(list):
            self.append(list[i])
            i += 1

        return self.head

    def printList(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next

test = Solution()
listHead = test.makeLinkedList([])
print(test.hasCycle(listHead))
test.createCycle(listHead)
print(test.hasCycle(listHead))


# Merge Node Problem
class LinkedList(object):
    head = None
    tail = None
    prev = None

    def __init__(self, lst):
        i = 0
        while i < len(lst):
            node = ListNode(lst[i])
            self.append(node)
            i += 1

    def append(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def return_head(self):
        return self.head

    def return_tail(self):
        return self.tail


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    head = None
    tail = None
    sum_head = None
    sum_tail = None

    def mergeNodes(self, head):
        sum_list = LinkedList([])
        current = head

        while current:
            if current.val == 0:
                sum_val, next_node = self.calculate_sum(current.next)
                sum_list.append(ListNode(sum_val))
                current = next_node
            else:
                current = current.next

        self.printList(sum_list.return_head())

    def calculate_sum(self, start):
        sum_val = 0
        while start and start.val != 0:
            sum_val += start.val
            start = start.next
        return sum_val, start


    def makeLinkedList(self, lst):
        linked_list = LinkedList(lst)
        return linked_list

    def append(self, data):
        new_node = ListNode(data)
        if self.sum_head is None:
            self.sum_head = new_node
        else:
            self.sum_tail.next = new_node
        self.sum_tail = new_node

    def printList(self, head):
        current = head
        while current:
            print(current.val)
            current = current.next

test = Solution()
list = test.makeLinkedList([0,1,2,0,1,0])
sum_list1 = test.mergeNodes(list.head)


# Find the middle Link
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    head = None
    tail = None

    def middleLink(self, head):
        slow_node = self.head
        fast_node = self.head

        while fast_node and fast_node.next:
            slow_node = slow_node.next
            fast_node = fast_node.next.next

        return slow_node.val

    def append(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def makeLinkedList(self, list):
        i = 0
        while i < len(list):
            self.append(list[i])
            i += 1

        return self.head

test = Solution()
lst = test.makeLinkedList([1,2,3,4,5,6])
print(test.middleLink(lst))

class TreeNode(object):
    def __init__(self, val="", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Convert Morse to Alphabet and vice versa
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

class LinkedList(object):
    head = None
    tail = None
    prev = None

    def __init__(self, list):
        i = 0
        while i < len(list):
            node = ListNode(list[i])
            self.append(node)
            i += 1

    def append(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def return_head(self):
        return self.head

    def return_tail(self):
        return self.tail

# Check if Linked List is a palindrome
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class Solution(object):
    head = None
    tail = None
    prev = None

    def isPalindrome(self, list):
        ls = list.return_head()
        rs = list.return_tail()

        while ls and ls != rs and rs:
            if ls.val != rs.val:
                return False
            ls = ls.next
            rs = rs.prev

        return True

    def makeLinkedList(self, list):
        linked_list = LinkedList(list)
        return linked_list


test = Solution()
list1 = test.makeLinkedList([1, 2, 3, 2, 1])
print(test.isPalindrome(list1))

# Remove Duplicates from a Linked List
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    head = None
    tail = None

    def deleteDuplicates(self, head):
        self.makeLinkedList(head)

        current_item = ListNode(self.head.val, self.head.next)
        while current_item.next:
            if current_item.val == current_item.next.val:
                self.deleteItem(current_item.val)
            current_item = current_item.next
            #self.printList()

    def append(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def deleteItem(self, item):
        current_item = self.head
        if current_item.val == item:
            self.head = current_item.next
            return
        while current_item.next:
            if current_item.next.val == item:
                if current_item.next is self.tail:
                    self.tail = current_item
                    self.tail.next = None
                    return
                current_item.next = current_item.next.next
            current_item = current_item.next

    def makeLinkedList(self, list):
        i = 0
        while i < len(list):
            self.append(list[i])
            i += 1

    def printList(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next

test = Solution()
test.deleteDuplicates([1,1,2,3,3,4,4,5])
test.printList()


# Remove Nth node from the end of a Linked List
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    head = None
    tail = None

    def removeNthFromEnd(self, head, n):
        self.deleteItem(self.recurs_func(head, n))
        #self.printList()

    def recurs_func(self, head, n):
        if head.next != self.tail:
            self.recurs_func(head.next, )

    def deleteItem(self, item):
        current_item = self.head
        if current_item.val == item:
            self.head = current_item.next
            return
        while current_item.next:
            if current_item.next.val == item:
                if current_item.next is self.tail:
                    self.tail = current_item
                    self.tail.next = None
                    return
                current_item.next = current_item.next.next
            current_item = current_item.next

    def append(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def makeLinkedList(self, list):
        i = 0
        while i < len(list):
            self.append(list[i])
            i += 1

        return self.head

    def printList(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next


test = Solution()
lst = test.makeLinkedList([1, 2, 3, 4, 5])
test.removeNthFromEnd(lst, 3)

# Reverse a Linked List
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    head = None
    tail = None
    rhead = None
    rtail = None

    def reverse_list(self, head):
        self.recurs_list(head)
        self.printList(self.rhead)


    def recurs_list(self, head):
        if head is None:
            return
        else:
            self.recurs_list(head.next)
        self.append2(head.val)


    def printList(self, head):
        current = head
        while current:
            print(current.val)
            current = current.next

    def append2(self, data):
        new_node = ListNode(data)
        if self.rhead is None:
            self.rhead = new_node
        else:
            self.rtail.next = new_node
        self.rtail = new_node


    def append(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def makeLinkedList(self, list):
        i = 0
        while i < len(list):
            self.append(list[i])
            i += 1

        return self.head

test = Solution()
lst = test.makeLinkedList([1,2,3,4,5])
test.reverse_list(lst)
