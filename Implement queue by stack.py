from collections import deque

class MyQueue(object):

    def __init__(self):
        self.queue = deque()

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        return self.queue.popleft()

    def peek(self):
        return self.queue[0]

    def empty(self):
        return not self.queue
