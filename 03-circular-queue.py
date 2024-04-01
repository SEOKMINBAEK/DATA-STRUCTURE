'''
선형 큐의 비효율을 제거하기 위해 고안된 것이 바로 원형 큐이다.
원형 큐는 선형 큐와 같이 1차원 리스트로 구현하지만,
논리적으로 리스트의 시작과 끝이 연결되어 있는 원형으로 간주하는 것.

front와 rear라는 2개의 포인터를 활용해 자료를 추가하거나 획득한다.
rear 포인터를 통해 자료를 추가, front 포인터를 통해 자료를 획득한다.

따라서 실질적으로 자료를 추가, 획득 시 기존에 저장된 자료들이 이동하지 않는다.

원형 큐는 공백과 포화상태를 구분하기 위해 1개의 공간을 buffer(여분)로 추가 할당한다.
'''

class CircularQueue:
  def __init__(self, size):
    self.max_size = size + 1
    self.data = [None] * self.max_size
    self.front = 0
    self.rear = 0
  
  def is_empty(self):
    return self.front == self.rear
  
  def is_full(self):
    return self.front == (self.rear + 1) % self.max_size
  
  def enqueue(self, el):
    if self.isFull():
      return False
    
    self.data[self.rear] = el
    self.rear = (self.rear + 1) % self.max_size
  
  def dequeue(self):
    if self.isEmpty():
      return False
    
    value = self.data[self.front]
    self.data[self.front] = None
    self.front = (self.front + 1) % self.max_size
    return value

circular_queue = CircularQueue(3)

'''
원형 큐는 리스트의 고정 크기를 가정해야 사용할 수 있다.
'''