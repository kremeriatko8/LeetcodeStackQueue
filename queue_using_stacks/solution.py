'''
lab 1. task 1
Implementing Queue using Stacks.
'''
class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def push(self, item):
        '''
        Adds element to top of the stack.
        '''
        new_node = Node(item)
        new_node.next = self._top
        self._top = new_node
        self._size += 1

    def pop(self):
        '''
        Returns and deletes the last element that comes to stack.
        '''
        if self._top is None:
            return 'Stack is empty.'
        value = self._top.data
        self._top = self._top.next
        self._size -= 1
        return value

    def peek(self):
        '''
        Returns the front element without removing it.
        '''
        if self._top is None:
            return 'Stack is empty.'
        return self._top.data

    def is_empty(self):
        '''
        Returns True/False whether the stack is empty ot not.
        '''
        return self._top is None

    def size(self):
        '''
        Returns the size of the stack.
        '''
        return self._size


class MyQueue:
    def __init__(self):
        self.incoming = Stack()
        self.ready_to_go = Stack()

    def push(self, x: int) -> None:
        '''
        Adds element to Queue.
        '''
        self.incoming.push(x)

    def pop(self) -> int:
        '''
        Removes and returns the element from the front of the queue.
        '''
        if self.ready_to_go.is_empty():
            while not self.incoming.is_empty():
                self.ready_to_go.push(self.incoming.pop())
        return self.ready_to_go.pop()

    def peek(self) -> int:
        '''
        Gets the value of the front element.
        '''
        if self.ready_to_go.is_empty():
            while not self.incoming.is_empty():
                self.ready_to_go.push(self.incoming.pop())
        return self.ready_to_go.peek()

    def empty(self) -> bool:
        '''
        Returns True if the queue is empty, False otherwise.
        '''
        return self.incoming.is_empty() and self.ready_to_go.is_empty()



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
