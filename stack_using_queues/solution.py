'''
lab 1. task 2
Implementing Stack using Queues.
'''
class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class Queue:
    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

    def add(self, item):
        '''
        Adds element to the end of Queue.
        '''
        new_node = Node(item)
        if self._rear is None:
            self._front = new_node
            self._rear = new_node
        else:
            self._rear.next = new_node
            self._rear = new_node
        self._size += 1

    def popleft(self):
        '''
        Removes the front element of the internal queue.
        '''
        if self._front is None:
            return 'Queue is empty.'
        value = self._front.data
        self._front = self._front.next
        if self._front is None:
            self._rear = None
        self._size -= 1
        return value

    def peek(self):
        '''
        Returns the front element without removing it.
        '''
        if self._front is None:
            return 'Queue is empty.'
        return self._front.data

    def is_empty(self):
        '''
        Returns True/False whether the stack is empty ot not.
        '''
        return self._front is None

    def size(self):
        '''
        Returns size of Queue.
        '''
        return self._size

class MyStack:
    def __init__(self):
        self.stack_storage = Queue()
        self.buffer = Queue()

    def push(self, x: int) -> None:
        '''
        Pushes element x onto the stack by reordering elements to maintain LIFO.
        '''
        self.buffer.add(x)
        while not self.stack_storage.is_empty():
            self.buffer.add(self.stack_storage.popleft())
        self.stack_storage, self.buffer = self.buffer, self.stack_storage

    def pop(self) -> int:
        '''
        Removes and returns the element on the top of the stack.
        '''
        return self.stack_storage.popleft()

    def top(self) -> int:
        '''
        Gets the top element of the stack without removing it.
        '''
        return self.stack_storage.peek()

    def empty(self) -> bool:
        '''
        Returns whether the stack is empty.
        '''
        return self.stack_storage.is_empty()
