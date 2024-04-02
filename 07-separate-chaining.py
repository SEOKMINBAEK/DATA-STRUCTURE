'''
체이닝은 각 버킷이 값이 아닌 연결 리스트를 가지고 있다.
개방 주소법이 빈 곳을 찾아 테이블을 순차적으로 순회했다면,
체이닝은 새로운 값을 연결 리스트에 추가한다.
'''

# ./04-singly-linked-list.py module
singly_linked_list = __import__('04-singly-linked-list')

LinkedList = singly_linked_list.LinkedList

class HashMap:
  def __init__(self, size):
    self.size = size
    self.buckets = [LinkedList() for _ in range(self.size)]
  
  def hash_func(self, key):
    return hash(key) % self.size
  
  def set(self, key, value):
    idx = self.hash_func(key)
    self.buckets[idx].insert((key, value))
  
  def get(self, key):
    idx = self.hash_func(key)
    cur = self.buckets[idx].head.next
    
    while cur is not None:
      if cur.val[0] == key:
        return cur.val[1]
      cur = cur.next
    
    return None
  
  def remove(self, key):
    idx = self.hash_func(key)
    cur = self.buckets[idx].head.next
    
    while cur is not None:
      if cur.val[0] == key:
        target = cur.val
        self.buckets[idx].remove(target)
        return
      cur = cur.next
    
    return None
  
  def traverse(self):
    for i in range(self.size):
      cur = self.buckets[i].head.next
      
      while cur is not None:
        print(f'Key: {cur.val[0]}, Value: {cur.val[1]}')
        cur = cur.next
  

hash_map = HashMap(5)

'''
체이닝은 데이터 저장에 제한이 없고 메모리 소모가 적은 편이다.
하지만 충돌이 빈번히 일어나는 곳에서 계속 데이터가 늘어나게 되면,
한 버킷 내에서만 데이터가 저장되는 쏠림현상이 일어날 수 있다.
'''