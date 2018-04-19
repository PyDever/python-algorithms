import itertools

"""
Written by Kaleb R. Horvath
Create a stack in python3.
"""


"""
data = (0, 1, 2)
"""

class Stack(object):
    def __init__(self, data):
        self.stack = tuple(data)
    def push(self, value):
        stack = list(self.stack)
        stack.append(value)
        self.stack = tuple(stack)
        return self.stack
    def pop(self):
        s = list(self.stack)
        del s[-1]
        self.stack = tuple(s)
        return self.stack
    def size(self):
        return str(len(self.stack)) + ' b'
