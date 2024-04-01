'''
해시맵은 키와 값으로 구성된 자료구조 이며 해시테이블, 딕셔너리 라고도 부른다. 
해시함수를 통해 주어진 키를 해시값(ex. 고정된 길이의 자연수)로 변환하여,
버킷이라는 공간에 데이터를 저장하고 내부 인덱스를 통해 데이터에 접근할 수 있게 한다.

하지만 해시함수의 입력은 무한하지만 출력은 유한하기 때문에,
서로 다른 키에 동일한 해시값으로 변환하는 해시충돌이 발생할 수 있다.

개방 주소법은 해시충돌이 발생하면 충돌한 버킷부터 선형적으로 순차 증가하여 비어있는 버킷을 찾는다.
리니어 프로빙(linear probing)혹은 선형 탐사라고도 한다.
'''

class HashMap:
  def __init__(self, size):
    self.size = size
    self.buckets = [None] * size
    self.cnt = 0
  
  def hash_func(self, key):
    return hash(key) % self.size
  
  def is_full(self):
    return self.cnt >= self.size
  
  def is_empty(self):
    return self.cnt == 0
  
  def set(self, key, value):
    if self.is_full():
      raise Exception('HashMap is full')
    
    idx = self.hash_func(key)
    
    while self.buckets[idx] is not None:
      idx = (idx + 1) % self.size
    
    self.buckets[idx] = (key, value)
    self.cnt += 1
  
  def get(self, key):
    if self.is_empty():
      raise Exception('HashMap is full')
    
    idx = self.hash_func(key)
    
    for _ in range(self.size):
      if self.buckets[idx] and self.buckets[idx][0] == key:
        return self.buckets[idx][1]
      idx = (idx + 1) % self.size
    
    return None
  
  def remove(self, key):
    if self.is_empty():
      raise Exception('HashMap is empty')
    
    idx = self.hash_func(key)
    
    for _ in range(self.size):
      if self.buckets[idx] and self.buckets[idx][0] == key:
        self.buckets[idx] = None
        self.cnt -= 1
        return
      idx = (idx + 1) % self.size
    
    return None
  
  def traverse(self):
    for idx in range(self.size):
      if self.buckets[idx] is not None:
        print(f'Key: {self.buckets[idx][0]}, Value: {self.buckets[idx][1]}')

hash_map = HashMap(5)

'''
개방 주소법은 빈 곳을 빠르게 찾지 못하면 많은 시간을 소모할 수 있는데다,
자료의 개수를 예측하고 미리 버킷을 준비해야 하기 때문에 예측 가능한 입력에만 효과적으로 대응할 수 있다.
'''