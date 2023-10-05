class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory(object):
    head = None
    prev = None
    curr = None

    def __init__(self, homepage):
        self.visit(homepage)

    def visit(self, url):
        new_node = ListNode(url)
        if self.head is None:
            self.head = new_node
        else:
            self.prev = self.curr
            self.curr.next = new_node
            new_node.prev = self.curr
        self.curr = new_node

    def back(self, steps):
        while steps > 0 and self.curr.prev:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.val

    def forward(self, steps):
        while steps > 0:
            if self.curr.next:
                self.curr = self.curr.next
            steps -= 1
        return self.curr.val

    def printBrowserHistory(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next

# Your BrowserHistory object will be instantiated and called as such:
obj = BrowserHistory("leetcode.com")
obj.visit("google.com")
obj.visit("youtube.com")
print(obj.back(2))
print(obj.forward(1))
obj.visit("wilcox.com")
print()
obj.printBrowserHistory()
