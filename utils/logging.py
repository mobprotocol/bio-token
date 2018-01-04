import sys

class ShortLog(object):
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.terminal = sys.stdout

    def write(self, message):
        self.count += 1
        if self.count < self.n:
            self.terminal.write(message)
