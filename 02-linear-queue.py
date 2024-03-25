'''
큐는 먼저 들어온 자료가 먼저 나가게 되는 선입선출(First-in First-out, FIFO) 자료구조이다.
대기열 개념으로, 표를 사기 위해 줄을 서는 사람들과 같은 개념이다.
'''

class LinearQueue:
  def __init__(self):
    self.data = []
  
  def enqueue(self, el):
    self.data.insert(0, el)
  
  def dequeue(self):
    if not self.data:
      return -1 # Fail
    return self.data.pop()
  
  def size(self):
    return len(self.data)
  
  def empty(self):
    if not self.data:
      return 1 # True
    return 0 # False
  
  def peek(self):
    if not self.data:
      return -1 # Fail
    return self.data[0]

linear_queue = LinearQueue()

'''
선형 큐에 자료를 추가하거나 획득할 때 기존에 저장된 자료가 이동해야하므로,
큐가 클수록 자료가 이동해야 하는 수로고움이 커진다.
N개의 원소를 저장할 수 있는 큐의 경우 값 하나를 추가하거나 획득하는데 O(N)의 연산 시간이 소비된다.
'''