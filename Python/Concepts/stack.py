# Stack Theory

# A stack is a linear data structure that follows the Last In, First Out (LIFO) principle.
# This means that the last element added to the stack is the first one to be removed.
# Common operations include:
# - push: Add an element to the top of the stack.
# - pop: Remove the top element of the stack.
# - peek (or top): View the top element without removing it.
# - is_empty: Check if the stack is empty.
# Stacks are used in various applications like undo mechanisms, expression evaluation, and recursion handling.

class Stack:
    def __init__(self):
        self.items=[]

    def push(self,element):
        self.items.append(element)

    def pop(self):
        if len(self.items)==0:
            raise Exception('No elements in stack to pop')
        self.items.pop()

    def peek(self):
        if len(self.items)==0:
            raise Exception('No elements in stack to pop')
        return self.items[-1]

    def is_empty(self):
        return len(self.items)==0

    def size(self):
        return len(self.items)

    def print(self):
        return self.items


if __name__=='__main__':
    stack=Stack()
    stack.push(3)
    stack.push(18)
    stack.push(654)
    stack.push(87)
    print("Initial Stack ->",stack.print())
    print("Popping Stack ->", stack.pop())
    print("After pop Stack ->", stack.print())
    print("Peeking Stack ->", stack.peek())
    print("After peekingStack ->", stack.print())
    print("Is empty Stack ->", stack.is_empty())
    print("Size of Stack ->", stack.size())
    stack.pop()
    stack.pop()
    stack.pop()
    print("Size of Stack ->", stack.size())
    #stack.pop() #POINT OF EXCEPTION
