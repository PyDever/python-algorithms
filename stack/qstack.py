class QStack(object):
    def __init__(self, data):
        self.stack = tuple(data)
    def push(self, value):
        stack = list(self.stack)
        stack.append(value)
        self.stack = tuple(stack)
        return self.stack
    def pop(self, i):
        s = list(self.stack)
        del s[-1]
        self.stack = tuple(s)
        return self.stack, i
    def size(self):
        return str(len(self.stack)) + ' b'
    def query(self, pos, query):
        s = list(self.stack)
        data = s[pos]
        results = []
        for X in data:
          if X==query:
            results.append(X)
        return pos, data, results
    def copy(self):
        return list(self.stack)
