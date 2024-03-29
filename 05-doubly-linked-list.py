'''
이중 연결 리스트는 단일 연결 리스트와 비슷하지만 두가지 차이점이 있다.

먼저 이중 연결 리스트의 노드는 값과, 
이전 노드의 링크 정보를 지닌 prev 포인터, 다음 노드의 링크 정보를 지닌 next 포인터로 구성된다.

또한 데이터가 없는 head 노드와 tail 노드를 구현하여, 앞뒤 어디에서든 탐색할 수 있다.
'''

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None
    self.prev =  None

class LinkedList:
  def __init__(self):
    self.head = Node(None)
    self.tail = Node(None)
    self.head.next = self.tail
    self.tail.prev = self.head
  
  def insert(self, val):
    node = Node(val)
    self.head.next.prev = node
    node.next = self.head.next
    self.head.next = node
    node.prev = self.head
  
  def remove(self, val):
    pre = self.head
    cur = self.head.next
    
    while cur:
      if cur.val == val:
        pre.next = cur.next
      pre = cur
      cur = cur.next
  
  def traverse(self):
    cur = self.head.next
    
    while cur != self.tail:
      print(cur.val, end=' ')
      cur = cur.next
  
  def searchFromHead(self, val):
    node = self.head.next
    cnt = 0
    
    while node:
      if node.val == val:
        print('index is', cnt)
        return
      cnt += 1
      node = node.next
    
    print('not found')
  
  def searchFromTail(self, val):
    node = self.tail.prev
    cnt = -1
    
    while node:
      if node.val == val:
        print('index is', cnt)
        return
      cnt += -1
      node = node.prev
    
    print('not found')

linked_list = LinkedList()