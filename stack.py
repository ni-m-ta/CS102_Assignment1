
'''
class Stack():
    def __init__(self):
        self.vals = []
    def push(self, val):
        self.vals.append(val)
    def pop(self):
        self.vals.pop()

MyStack = Stack()

MyStack.push(1)
MyStack.push(2)
MyStack.push(3)
MyStack.pop()
'''

class Class():
    # constructor
    def __init__(self):
        store = []
        tos = 0
    def push(self, val):
        self.store.append(val)
        self.tos = self.tos + 1
    
    def pop(self):
        if self.tos == 0:
            print("Stack is empty")
            return None
        self.tos = self.tos - 1
        return self.store.pop()

s1 = Class()
