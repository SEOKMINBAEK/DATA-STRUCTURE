'''
스택은 대표적인 후입선출(last-in first-out, LIFO)즉,
가장 나중에 들어간 자료가 먼저 출력되는 자료구조이다.
'''

class Stack:
  def __init__(self):
    self.data = []
  
  def push(self, el):
    self.data.append(el)
  
  def pop(self):
    if not self.data:
      return -1 # Fail
    return self.data.pop()

  def size(self):
    return len(self.data)

  def empty(self):
    if not self.data:
      return 1 # True
    return 0 # False

  def top(self):
    if not self.data:
      return -1 # Fail
    return self.data[-1]

stk = Stack()