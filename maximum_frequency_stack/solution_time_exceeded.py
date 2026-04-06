from collections import deque

class FreqStack:
    def __init__(self):
        self.stack = deque()

    def push(self, val: int) -> None:
        '''
        Adds element to stack.
        '''
        self.stack.append(val)

    def pop(self) -> int:
        '''
        In two for-passes, first determined the highest
        frequency and then found these elements.
        '''
        max_freq = 0
        for item in self.stack:
            freq = 0
            for other in self.stack:
                if other == item:
                    freq += 1
            if freq > max_freq:
                max_freq = freq

        for i in range(len(self.stack) - 1, -1, -1):
            freq = 0
            for item in self.stack:
                if item == self.stack[i]:
                    freq += 1
            if freq == max_freq:
                val = self.stack[i]
                del self.stack[i]
                return val
