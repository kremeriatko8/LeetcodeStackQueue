'''
lab 1. task 3
'''
from collections import deque, defaultdict

class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(deque)
        self.max_freq = 0

    def push(self, val: int) -> None:
        '''
        Pushes an integer value onto the frequency stack.
        Updates the frequency of val and groups it by frequency.
        Updates max_freq if the frequency of val exceeds the current maximum.
        '''
        self.freq[val] += 1
        frequency = self.freq[val]
        self.group[frequency].append(val)
        self.max_freq = max(self.max_freq, frequency)

    def pop(self):
        '''
        Removes and returns the most frequent element in the stack.
        '''
        elem = self.group[self.max_freq].pop()
        self.freq[elem] -= 1
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return elem
