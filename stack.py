#!python

from linkedlist import LinkedList

"""STARTER CODE FROM NEPTUNIUS"""
# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        if self.list.is_empty(self):
            return True
        return False

    def length(self):
        """Return the number of items in this stack."""
        return self.list.size()

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) – Why? Because we don't have to traverse through the whole thing"""
        self.list.prepend(self, item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        if !self.list.is_empty(self):
            return self.list.head.data
        return None

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) – Why? No need to traverse list"""
        if !self.list.is_empty(self):
            self.list.next = self.list.head
            return
        raise ValueError('Stack is empty!')


# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        if self == None:
            return True
        return False

    def length(self):
        """Return the number of items in this stack."""
        return len(self)

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) – Why? Doesn't have to move data"""
        self.push(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        self.list[0]

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(n) – Why? Because all items must be moved down array"""
        self.pop(self.list[0])


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
Stack = LinkedStack
# Stack = ArrayStack
