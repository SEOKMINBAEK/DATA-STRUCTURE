'''
원형 큐는 고정크기를 가정하기 때문에 고정 크기로 해결하지 못하는 문제가 많다.
이때 쓰이는 자료구조가 연결 리스트로써, 원소를 추가하는 만큼 크기가 커지는 것이 특징이다.

단일 연결 리스트는 노드라는 원소에 값과 다음 노드의 링크 정보를 담은 next 포인터로 구성되어 있다.
통상 단일 연결 리스트는 첫번째 노드에 데이터가 없는 head 노드를 구현한다.
'''

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = Node(None)
  
  def insert(self, val):
    node = Node(val)
    node.next = self.head.next
    self.head.next = node
  
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
    
    while cur:
      print(cur.val, end=' ')
      cur = cur.next

linked_list = LinkedList()

'''
일반적인 배열 리스트는 물리적인 메모리 주소가 연속적이지만,
연결 리스트는 next 포인터를 통해 연결되기 때문에 메모리 주소가 랜덤이다.

연결리스트는 배열 리스트와 반대로 삽입/삭제는 O(1)이 걸리지만(데이터 이동이 필요없음),
연속적인 메모리 주소가 아니기 때문에 모든 노드를 거쳐서 탐색해야 한다.(O(n))
'''