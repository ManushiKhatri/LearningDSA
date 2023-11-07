from random import randint

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.val)


class LinkedList:
    def __init__(self, vals=None):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

    def __str__(self):
        vals = [str(x.val) for x in self]
        return ' -> '.join(vals) + '-> ' + ' None'

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result
    #insertion 
    def add(self, val):
        if self.head is None:
            newNode = Node(val)
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next
        return self.tail
    def delete(self,x):
        if self.head is None:
            return self.head 
        curr = self.head 
        while curr.next:
            if curr.val == x

    def generate(self, n):
        self.head = None
        self.tail = None
        for i in range(1, n+1):
            self.add(i)
            # self.add(i)
        return self
    
ll = LinkedList()
print(ll.generate(10))

